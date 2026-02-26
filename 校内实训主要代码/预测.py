import torch
from torchvision import transforms, models
import torch.nn as nn
from PIL import Image, ImageTk
import os
import tkinter as tk
from tkinter import filedialog


class FlowerClassifier:
    def __init__(self, model_path):
        self.device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
        self.transform = transforms.Compose([
            transforms.Resize(256),
            transforms.CenterCrop(224),
            transforms.ToTensor(),
            transforms.Normalize(
                [0.485, 0.456, 0.406],
                [0.229, 0.224, 0.225]
            )
        ])
        self.model = models.resnet50(weights=None)
        num_ftrs = self.model.fc.in_features
        self.model.fc = nn.Linear(num_ftrs, 102)
        self.model.load_state_dict(
            torch.load(model_path, map_location=self.device)
        )
        self.model = self.model.to(self.device)
        self.model.eval()

    def predict(self, image_path):
        try:
            if not os.path.exists(image_path):
                raise FileNotFoundError(f"Image not found at {image_path}")
            image = Image.open(image_path).convert('RGB')
            input_tensor = self.transform(image)
            input_tensor = input_tensor.unsqueeze(0)
            input_tensor = input_tensor.to(self.device)
            with torch.no_grad():
                outputs = self.model(input_tensor)
                _, preds = torch.max(outputs, 1)
            return preds[0].item() + 1
        except Exception as e:
            print(f"Prediction failed: {str(e)}")
            return None


class FlowerClassifierGUI:
    def __init__(self, root, model_path):
        self.root = root
        self.root.title("Flower Classifier")
        self.classifier = FlowerClassifier(model_path)

        self.label = tk.Label(root, text="请选择一张花卉图片进行分类")
        self.label.pack(pady=20)

        self.select_button = tk.Button(root, text="选择图片", command=self.select_image)
        self.select_button.pack(pady=10)

        self.image_label = tk.Label(root)
        self.image_label.pack(pady=20)

        self.result_label = tk.Label(root, text="")
        self.result_label.pack(pady=20)

    def select_image(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            try:
                image = Image.open(file_path)
                image.thumbnail((300, 300))
                photo = ImageTk.PhotoImage(image)
                self.image_label.config(image=photo)
                self.image_label.image = photo

                result = self.classifier.predict(file_path)
                if result is not None:
                    self.result_label.config(text=f'预测的类别编号: {result}')
                else:
                    self.result_label.config(text="预测失败。")
            except Exception as e:
                self.result_label.config(text=f"发生错误: {str(e)}")


if __name__ == '__main__':
    root = tk.Tk()
    app = FlowerClassifierGUI(root, model_path='best_model.pth')
    root.mainloop()
