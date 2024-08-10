import os
import shutil
from torchvision import datasets, transforms
from torch.utils.data import DataLoader

# Define paths
data_root = "C:/Users/Vlad Talpiga.VLR_PROJAMZ/OneDrive - Valrom Industrie SRL/Desktop/IAVA/Proiect/FoodClassifier/data/food-101/images"
train_dir = "C:/Users/Vlad Talpiga.VLR_PROJAMZ/OneDrive - Valrom Industrie SRL/Desktop/IAVA/Proiect/FoodClassifier/cross_validation/folder/train"
val_dir = "C:/Users/Vlad Talpiga.VLR_PROJAMZ/OneDrive - Valrom Industrie SRL/Desktop/IAVA/Proiect/FoodClassifier/cross_validation/folder/validation"

# Create train and validation directories if they don't exist
os.makedirs(train_dir, exist_ok=True)
os.makedirs(val_dir, exist_ok=True)

# Define partition ratios
val_ratio = 0.2
train_ratio = 0.8

# Loop through each class folder
for class_folder in os.listdir(data_root):
    class_path = os.path.join(data_root, class_folder)
    if os.path.isdir(class_path):
        images = os.listdir(class_path)
        num_val = int(len(images) * val_ratio)
        num_train = int(len(images) * train_ratio)
        
        # Split images into train and validation sets
        val_images = images[:num_val]
        train_images = images[num_val:num_val+num_train]
        
        # Move images to train directory
        for img in train_images:
            src = os.path.join(class_path, img)
            dst = os.path.join(train_dir, class_folder)
            os.makedirs(dst, exist_ok=True)
            shutil.copy(src, dst)
        
        # Move images to validation directory
        for img in val_images:
            src = os.path.join(class_path, img)
            dst = os.path.join(val_dir, class_folder)
            os.makedirs(dst, exist_ok=True)
            shutil.copy(src, dst)

# Define transformations
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406],
                         std=[0.229, 0.224, 0.225])
])

# Create datasets
train_dataset = datasets.ImageFolder(train_dir, transform=transform)
val_dataset = datasets.ImageFolder(val_dir, transform=transform)

# Create data loaders
train_loader = DataLoader(train_dataset, batch_size=32, shuffle=True)
val_loader = DataLoader(val_dataset, batch_size=32, shuffle=False)
