import torch
import torch.nn as nn
import torch.optim as optim
import matplotlib
matplotlib.use('Agg')  # 非交互模式
import matplotlib.pyplot as plt
import os
from torchvision import transforms, datasets, models
from torch.utils.data import DataLoader
from tqdm import tqdm
# 数据预处理
data_transforms = {
    'train': transforms.Compose([
        transforms.RandomResizedCrop(224),
        transforms.RandomHorizontalFlip(),
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
    ]),
    'valid': transforms.Compose([
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
    ]),
}


# 模型构建代码
def build_model():
    # 初始化模型
    model = models.resnet50(weights=models.ResNet50_Weights.IMAGENET1K_V1)
    # 冻结所有参数
    for param in model.parameters():
        param.requires_grad = False
    # 替换全连接层
    num_ftrs = model.fc.in_features
    model.fc = nn.Linear(num_ftrs, 102)  # 102个类别
    return model


# 模型训练代码
def train():
    # 设备配置
    device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

    # 加载数据
    data_dir = './data'
    image_datasets = {
        x: datasets.ImageFolder(os.path.join(data_dir, x), data_transforms[x])
        for x in ['train', 'valid']
    }
    dataloaders = {
        x: DataLoader(image_datasets[x], batch_size=32, shuffle=True, num_workers=0)
        for x in ['train', 'valid']
    }
    dataset_sizes = {x: len(image_datasets[x]) for x in ['train', 'valid']}
    class_names = image_datasets['train'].classes

    # 初始化模型
    model = build_model().to(device)

    # 定义损失函数和优化器
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.SGD(model.fc.parameters(), lr=0.001, momentum=0.9)

    # 训练循环
    best_acc = 0.0
    train_loss, train_acc = [], []
    val_loss, val_acc = [], []

    for epoch in range(10):
        print(f'Epoch {epoch}/9')
        print('-' * 10)

        for phase in ['train', 'valid']:
            if phase == 'train':
                model.train()
            else:
                model.eval()

            running_loss = 0.0
            running_corrects = 0

            for inputs, labels in tqdm(dataloaders[phase], desc=f'{phase} Epoch {epoch}'):
                inputs = inputs.to(device)
                labels = labels.to(device)

                optimizer.zero_grad()

                with torch.set_grad_enabled(phase == 'train'):
                    outputs = model(inputs)
                    _, preds = torch.max(outputs, 1)
                    loss = criterion(outputs, labels)

                    if phase == 'train':
                        loss.backward()
                        optimizer.step()

                running_loss += loss.item() * inputs.size(0)
                running_corrects += torch.sum(preds == labels.data)

            epoch_loss = running_loss / dataset_sizes[phase]
            epoch_acc = running_corrects.double().cpu().item() / dataset_sizes[phase]

            if phase == 'train':
                train_loss.append(epoch_loss)
                train_acc.append(epoch_acc)
            else:
                val_loss.append(epoch_loss)
                val_acc.append(epoch_acc)
                if epoch_acc > best_acc:
                    best_acc = epoch_acc
                    torch.save(model.state_dict(), 'best_model.pth')

            print(f'{phase} Loss: {epoch_loss:.4f} Acc: {epoch_acc:.4f}')

    # 保存训练结果
    plt.figure(figsize=(12, 4))
    plt.subplot(1, 2, 1)
    plt.plot(train_loss, label='Train Loss')
    plt.plot(val_loss, label='Val Loss')
    plt.legend()
    plt.subplot(1, 2, 2)
    plt.plot(train_acc, label='Train Acc')
    plt.plot(val_acc, label='Val Acc')
    plt.legend()
    plt.savefig('training_curve.png')
    print("Training completed. Model saved as best_model.pth")


if __name__ == '__main__':
    train()
