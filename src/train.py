from torch.optim import Adam
import torch
import torch.nn as nn
from pathlib import Path

# The majority of the code in this file was AI Generated: ChatGPT-5, 11/25/25

def compute_pos_weights(df_train):
    pos_weight = torch.stack(df_train["label_vec"].tolist()).sum(dim=0)
    neg_weight = len(df_train) - pos_weight
    pos_weight = neg_weight / (pos_weight + 1e-5)
    return pos_weight

def train_baseline_model(model, train_loader, df_train, device, epochs=20, lr=1e-3, save_path=None):
    model = model.to(device)
    optimizer = Adam(model.parameters(), lr=1e-3)
    pos_weight = compute_pos_weights(df_train).to(device)
    criterion = nn.BCEWithLogitsLoss(pos_weight=pos_weight)
    for epoch in range(epochs):
        model.train()
        total_loss = 0
        for imgs, labels in train_loader:
            imgs, labels = imgs.to(device), labels.to(device)
            optimizer.zero_grad()
            outputs = model(imgs)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()
            total_loss += loss.item()
        print(f"Epoch {epoch+1} | Train Loss: {total_loss/len(train_loader):.4f}")
    
    if save_path is not None:
        Path(save_path).parent.mkdir(parents=True, exist_ok=True)
        torch.save(model.state_dict(), save_path)
        print(f"Baseline model saved to {save_path}")

def train_resnet_model(model, train_loader, df_train, device, epochs=20, lr=1e-3, save_path=None):
    model.to(device)

    optimizer = Adam(model.parameters(), lr=1e-3)
    pos_weight = compute_pos_weights(df_train).to(device)
    criterion = nn.BCEWithLogitsLoss(pos_weight=pos_weight)

    for epoch in range(epochs):
        model.train()
        total_loss = 0.0

        for imgs, labels in train_loader:
            imgs, labels = imgs.to(device), labels.to(device)

            optimizer.zero_grad()
            outputs = model(imgs)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()

            total_loss += loss.item()

        print(f"Epoch {epoch+1}/{epochs} - Loss: {total_loss/len(train_loader):.4f}")

    if save_path is not None:
        Path(save_path).parent.mkdir(parents=True, exist_ok=True)
        torch.save(model.state_dict(), save_path)
        print(f"Resnet model saved to {save_path}")
