import torch
import torch.nn as nn
from torchvision.models import resnet50, ResNet50_Weights

class TinyCNN(nn.Module):
    def __init__(self, num_classes):
        super().__init__()
        self.features = nn.Sequential(
            nn.Conv2d(3, 32, 3, padding="same"), nn.ReLU(), nn.MaxPool2d(2),
            nn.Conv2d(32, 64, 3, padding="same"), nn.ReLU(), nn.MaxPool2d(2),
        )
        self.classifier = nn.Sequential(
            nn.Flatten(),
            nn.Linear(64*56*56, 256), nn.ReLU(),
            nn.Dropout(0.3),
            nn.Linear(256, num_classes)
        )

    def forward(self, x):
        return self.classifier(self.features(x))

def build_baseline_model(num_classes):
    return TinyCNN(num_classes)

def build_resnet_model(num_classes):
    weights = ResNet50_Weights.DEFAULT
    model = resnet50(weights=weights)

    num_features = model.fc.in_features
    model.fc = nn.Linear(num_features, num_classes)

    return model