from model.foods import class_labels

import torch
from torchvision import transforms
from PIL import Image
import torch.nn.functional as F
import matplotlib.pyplot as plt
from torchvision import transforms, models
import torch.nn as nn
from torchvision.models import ResNet50_Weights


class Model(nn.Module):
    def __init__(self):
        super(Model, self).__init__()
        
        resnet = models.resnet50(weights=ResNet50_Weights.IMAGENET1K_V1)
        resnet = nn.Sequential(*list(resnet.children())[:-1])
        for param in resnet.parameters():
            param.requires_grad = False


        self.model = nn.Sequential(
            resnet,
            nn.AdaptiveAvgPool2d((1, 1)),
            nn.Flatten(),
            nn.Linear(2048, 512),
            nn.ReLU(),
            nn.BatchNorm1d(512),
            nn.Dropout(0.25),
            nn.Linear(512, 128),
            nn.ReLU(),
            nn.BatchNorm1d(128),
            nn.Dropout(0.1),
            nn.Linear(128, 105)
        )

    def forward(self, x):
        return self.model(x)
    
# if __name__ == '__main__':

#     # image_path = "images/chicken_wings.jpg"
#     # image_path = "images/sp_bol.jpg"
#     image_path = "images/apple_pie.jpg"

#     model = Model()

#     output_class = classify_image(image_path, model)

#     print(output_class)
