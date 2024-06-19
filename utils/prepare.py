import os
import pandas as pd
import shutil
from sklearn.model_selection import train_test_split
from PIL import Image

def split_and_copy_images(annotation_path, images_path, output_path):
    '''
    Split images into train and val sets 
    and set up directory in correct format 
    for classification training.
    :params annotation_path\csv
    :params path to all images for training
    :return
    '''
    # STEP 1: Load the CSV file.
    annotations = pd.read_csv(annotation_path)

    # STEP 2: Split data into 80/20 training and validation set respectively.
    train_df, val_df = train_test_split(annotations, test_size=0.2, random_state=42)

    # STEP 3: Set train and val paths
    TRAIN_IMAGES_DIR = os.path.join(output_path, 'train')
    VAL_IMAGES_DIR = os.path.join(output_path, 'val')

    # STEP 4: Make a list of images for copying from earlier split. 
    train_images = list(train_df['name'])
    val_images = list(val_df['name'])

    # STEP 5: Set up directory-path, key-value pairs for improving readability 
    directories = {
        'train_mask': os.path.join(TRAIN_IMAGES_DIR, 'mask'),
        'train_no_mask': os.path.join(TRAIN_IMAGES_DIR, 'no-mask'),
        'val_mask': os.path.join(VAL_IMAGES_DIR, 'mask'),
        'val_no_mask': os.path.join(VAL_IMAGES_DIR, 'no-mask')
    }

    # Create directories if they don't exist
    for dir_path in directories.values():
        os.makedirs(dir_path, exist_ok=True)

    # Process images
    for image_name in train_images + val_images:
        source_path = os.path.join(images_path, image_name)
        
        # Determine target directory based on split
        if image_name in train_images:
            split = 'train'
        elif image_name in val_images:
            split = 'val'
        else:
            print(f"Warning: Image {image_name} not found in train or val images.")
            continue
        
        # Determine class based on annotation
        found = False
        for index, row in annotations.iterrows():
            if row['name'] == image_name:
                found = True
                class_dir = directories[f'{split}_{row["classname"]}']
                break
        
        if not found:
            print(f"Warning: Image {image_name} not found in annotation.")
            continue
        
        target_path = os.path.join(class_dir, image_name)
        
        try:
            shutil.copy(source_path, target_path)
        except FileNotFoundError:
            print(f"Error: {source_path} not found.")

    print(f"Data split into training and validation sets and copied to {TRAIN_IMAGES_DIR} and {VAL_IMAGES_DIR} respectively.")


