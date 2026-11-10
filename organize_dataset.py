import os
import shutil
import pandas as pd

# Root directory of your unzipped Roboflow dataset
dataset_dir = r"F:\mini_project\tomato-leaf-disease-detection-1"

# Splits to process
splits = ['train', 'valid', 'test']

for split in splits:
    split_dir = os.path.join(dataset_dir, split)
    csv_path = os.path.join(split_dir, "_classes.csv")
    
    if not os.path.exists(split_dir):
        continue
        
    if not os.path.exists(csv_path):
        print(f"Skipping '{split}': _classes.csv not found in {split_dir}")
        continue
        
    print(f"Organizing '{split}' split from {csv_path}...")
    df = pd.read_csv(csv_path)
    
    # Strip whitespace from column headers
    df.columns = df.columns.str.strip()
    
    # Case 1: Roboflow One-Hot Encoded CSV (filename, Early Blight, Late Blight, ...)
    if 'filename' in df.columns and len(df.columns) > 2:
        class_columns = [col for col in df.columns if col != 'filename']
        moved_count = 0
        
        for _, row in df.iterrows():
            filename = str(row['filename']).strip()
            # Find the active disease class column (where value == 1)
            for cls_name in class_columns:
                if row[cls_name] == 1:
                    target_dir = os.path.join(split_dir, cls_name)
                    os.makedirs(target_dir, exist_ok=True)
                    
                    src_path = os.path.join(split_dir, filename)
                    dst_path = os.path.join(target_dir, filename)
                    
                    if os.path.exists(src_path):
                        shutil.move(src_path, dst_path)
                        moved_count += 1
                    break
        print(f"Successfully moved {moved_count} images into class folders for '{split}'.")
        
    # Case 2: Standard Single-Column CSV (filename, class)
    elif 'filename' in df.columns and ('class' in df.columns or 'label' in df.columns):
        class_col = 'class' if 'class' in df.columns else 'label'
        moved_count = 0
        
        for _, row in df.iterrows():
            filename = str(row['filename']).strip()
            cls_name = str(row[class_col]).strip()
            
            target_dir = os.path.join(split_dir, cls_name)
            os.makedirs(target_dir, exist_ok=True)
            
            src_path = os.path.join(split_dir, filename)
            dst_path = os.path.join(target_dir, filename)
            
            if os.path.exists(src_path):
                shutil.move(src_path, dst_path)
                moved_count += 1
        print(f"Successfully moved {moved_count} images into class folders for '{split}'.")

print("\nDataset organization complete!")