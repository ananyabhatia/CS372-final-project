from sklearn.metrics import f1_score
import torch 

# The majority of the code in this file was AI Generated: ChatGPT-5, 11/25/25

def evaluate(model, loader, device, threshold=0.5):
    model.eval()
    preds, trues = [], []

    with torch.no_grad():
        for imgs, labels in loader:
            imgs = imgs.to(device)
            labels = labels.to(device)

            outputs = model(imgs)
            outputs = torch.sigmoid(outputs)

            preds.append(outputs.cpu())
            trues.append(labels.cpu())

    # Concatenate all batches
    preds = torch.cat(preds)
    trues = torch.cat(trues)

    # Threshold into binary predictions
    preds_bin = (preds > threshold).int().numpy()
    trues_bin = trues.int().numpy()

    # Compute metrics
    micro_f1 = f1_score(trues_bin, preds_bin, average="micro", zero_division=0)
    macro_f1 = f1_score(trues_bin, preds_bin, average="macro", zero_division=0)
    return micro_f1, macro_f1