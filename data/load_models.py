import torch
import torch.nn as nn
from torchvision.models import resnet50, ResNet50_Weights
from src.model import TinyCNN

# The majority of the code in this file was AI Generated: ChatGPT-5, 11/25/25

def load_resnet_model(weight_path, num_classes, device):
    # Load pretrained backbone
    base_weights = ResNet50_Weights.DEFAULT
    model = resnet50(weights=base_weights)

    # Replace classification layer with your fine-tuned output layer size
    in_features = model.fc.in_features
    model.fc = nn.Linear(in_features, num_classes)

    # Load fine-tuned weights
    state_dict = torch.load(weight_path, map_location=device)
    model.load_state_dict(state_dict)

    model = model.to(device)
    model.eval()
    return model

def load_tinycnn(weight_path, num_classes, device):
    """
    Reconstructs your TinyCNN architecture, loads pretrained weights,
    moves the model to the appropriate device, and sets it to eval mode.
    """
    # Rebuild architecture (must match training-time definition)
    model = TinyCNN(num_classes)

    # Load the saved state dict
    state = torch.load(weight_path, map_location=device)
    model.load_state_dict(state)

    # Move to device and eval mode
    model = model.to(device)
    model.eval()
    return model