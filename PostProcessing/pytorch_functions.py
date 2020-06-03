import torch
import torchvision
from torchvision import models
import torchvision.transforms as transforms
import torch.nn as nn
import torch.nn.functional as F
import cv2
import numpy as np
from PIL import Image

class MODEL(nn.Module):
    def __init__(self, num_classes):
        super().__init__()
        self.network = models.resnet18(pretrained=True)
        self.classifier = nn.Sequential(
            nn.Dropout()
            , nn.Linear(1000, num_classes)
            , nn.Sigmoid()
        )
    def forward(self, x):
        x = self.network(x)
        return self.classifier(x)
        
class Inference():
    def __init__(self,
    _path_to_model = "./PyTorch_Classification_Model.pt",
    _path_to_label = "./label_map.txt"
    ):
        self.transform_info = transforms.Compose([
        transforms.Resize(size=(224, 224))
        , transforms.ToTensor()])
        self.label_map = np.loadtxt(_path_to_label, str, delimiter='\t')
        self.model = MODEL(len(self.label_map))
        self.model.load_state_dict(torch.load(_path_to_model, map_location=torch.device('cpu')))
        self.model.eval()
        dummy_x = torch.rand(1, 3, 224, 224)
        _ = self.model(dummy_x)
        
    def print_result(self, inference_result):
        class_text = self.label_map[np.argmax(inference_result)]
        class_prob = inference_result[0][np.argmax(inference_result)]
        print(class_text, class_prob)
        return class_text,class_prob

    def inference_image(self, opencv_image):
        image = Image.fromarray(opencv_image)
        image_tensor = self.transform_info(image)
        image_tensor = image_tensor.unsqueeze(0)
        inference_result = self.model(image_tensor)
        inference_result = inference_result.detach().numpy()
        return inference_result

