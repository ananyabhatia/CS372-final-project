import pandas as pd
import torch
from datasets import load_dataset
import re
from tqdm import tqdm
from itertools import chain
from collections import Counter
from torch.utils.data import Dataset, DataLoader
from torchvision import transforms 

def load_hf_dataset():
    return load_dataset("cemoss17/hellofresh_image_ingredients")

def clean_ingredient(name: str) -> str:
    """Remove descriptors like ', raw' and lowercase."""
    name = name.lower()
    name = re.sub(r",.*", "", name)  # drop ', raw', ', uncooked', etc.
    name = re.sub(r"[^a-z\s]", "", name)  # remove digits/punctuation if present
    return name.strip()

def extract_meals(ds_split):
    records = []
    for sample in tqdm(ds_split, desc="Extracting meals"):
        try:
            # some samples may be missing the field
            item = sample["meal"]["items"][0]
            dish = item["name"]
            ingredients = [clean_ingredient(i["name"]) for i in item.get("ingredients", [])]
            img = sample["image"]
            if ingredients:
                records.append({"dish": dish, "ingredients": ingredients, "image": img})
        except Exception as e:
            # skip malformed entries
            continue
    return records


def build_records(dataset):
    train_records = extract_meals(dataset["train"])
    valid_records = extract_meals(dataset["validation"]) if "validation" in dataset else []
    test_records  = extract_meals(dataset["test"]) if "test" in dataset else []
    df_train = pd.DataFrame(train_records)
    df_val   = pd.DataFrame(valid_records)
    df_test  = pd.DataFrame(test_records)
    return df_train, df_val, df_test

def build_label_map(df):
    # Combine all ingredient lists into one big list
    all_ingredients = list(chain.from_iterable(df["ingredients"]))

    # Count occurrences
    ingredient_counts = Counter(all_ingredients)

    # (Optional) limit to the top N most frequent ingredients
    TOP_N = 400  # you can adjust based on dataset size
    most_common_ingredients = [ing for ing, _ in ingredient_counts.most_common(TOP_N)]

    # Create a mapping from ingredient → index
    label_map = {name: idx for idx, name in enumerate(most_common_ingredients)}
    inv_label_map = {idx: name for name, idx in label_map.items()}
    return label_map, inv_label_map

def encode_ingredients(ingredient_list, label_map):
    """Convert ingredient list → binary multi-hot vector"""
    vec = torch.zeros(len(label_map), dtype=torch.float32)
    for ing in ingredient_list:
        if ing in label_map:  # only keep ingredients in top-N vocab
            vec[label_map[ing]] = 1.0
    return vec

def encode_df(df, label_map):
    if df is None or len(df) == 0:
        return df
    df = df.copy()
    df["label_vec"] = df["ingredients"].apply(lambda lst: encode_ingredients(lst, label_map))
    return df

def get_dataloaders(df_train, df_val, df_test):
    # Transforms: resize, normalize, augment for training
    train_tfms = transforms.Compose([
        transforms.Resize((224,224)),
        transforms.RandomHorizontalFlip(),
        transforms.ColorJitter(brightness=0.2, contrast=0.2),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485,0.456,0.406],
                            std=[0.229,0.224,0.225])
    ])

    val_tfms = transforms.Compose([
        transforms.Resize((224,224)),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485,0.456,0.406],
                            std=[0.229,0.224,0.225])
    ])

    # Create dataset and dataloaders
    train_ds = FoodDataset(df_train, transform=train_tfms)
    val_ds   = FoodDataset(df_val,   transform=val_tfms)
    test_ds  = FoodDataset(df_test,  transform=val_tfms)

    train_loader = DataLoader(train_ds, batch_size=32, shuffle=True)
    val_loader   = DataLoader(val_ds,   batch_size=32, shuffle=False)
    test_loader  = DataLoader(test_ds,  batch_size=32, shuffle=False)
    return train_ds, val_ds, test_ds, train_loader, val_loader, test_loader

class FoodDataset(Dataset):
    def __init__(self, df, transform=None):
        self.df = df
        self.transform = transform

    def __len__(self):
        return len(self.df)

    def __getitem__(self, idx):
        row = self.df.iloc[idx]
        img = row["image"]
        if self.transform:
            img = self.transform(img)
        label = row["label_vec"]
        return img, label


