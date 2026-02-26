import torch
from torchvision import transforms, models
import torch.nn as nn
from PIL import Image
import os


class FlowerClassifier:
    def __init__(self, model_path):
        # 初始化设备选择（GPU优先）
        self.device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

        # 定义图像预处理流程（必须与训练时保持一致）
        self.transform = transforms.Compose([
            transforms.Resize(256),  # 调整图像尺寸
            transforms.CenterCrop(224),  # 中心裁剪
            transforms.ToTensor(),  # 转换为张量
            transforms.Normalize(  # 标准化（ImageNet标准）
                [0.485, 0.456, 0.406],
                [0.229, 0.224, 0.225]
            )
        ])

        # 初始化ResNet50模型
        self.model = models.resnet50(weights=None)

        # 修改全连接层（必须与训练时的结构一致）
        num_ftrs = self.model.fc.in_features
        self.model.fc = nn.Linear(num_ftrs, 102)  # 输出102个类别（0 - 101）

        # 加载训练好的权重
        self.model.load_state_dict(
            torch.load(model_path, map_location=self.device)
        )

        # 将模型移动到指定设备
        self.model = self.model.to(self.device)

        # 设置为评估模式（关闭dropout等训练专用层）
        self.model.eval()

    def predict(self, image_path):
        try:
            # 检查文件是否存在
            if not os.path.exists(image_path):
                raise FileNotFoundError(f"Image not found at {image_path}")

            # 加载并预处理图像
            image = Image.open(image_path).convert('RGB')  # 确保RGB格式
            input_tensor = self.transform(image)  # 应用预处理
            input_tensor = input_tensor.unsqueeze(0)  # 添加batch维度（从CxHxW变为1xCxHxW）
            input_tensor = input_tensor.to(self.device)  # 移动数据到设备

            # 进行预测
            with torch.no_grad():  # 关闭梯度计算
                outputs = self.model(input_tensor)
                _, preds = torch.max(outputs, 1)  # 获取最大概率的类别索引

            # 返回类别数字（将0 - 101映射到1 - 102）
            return preds[0].item() + 1

        except Exception as e:
            print(f"Prediction failed: {str(e)}")
            return None


if __name__ == '__main__':
    # 初始化分类器（需要提供模型路径）
    classifier = FlowerClassifier(model_path='best_model.pth')

    # 示例预测（需修改为实际测试图片路径）
    test_image = './data/test/0/image_06736.jpg'

    # 执行预测
    result = classifier.predict(test_image)

    # 处理结果
    if result is not None:
        print(f'Predicted class number: {result}')
    else:
        print("Prediction failed.")
