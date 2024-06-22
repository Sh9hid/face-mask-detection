import os
from config.config import DATA_DIRECTORY_PATH, FILE_PATH, IMAGES_DIR, ANNOTATION_PATH, IMAGES_OUTPUT_DIRECTORY_PATH
import pandas as pd
import shutil
from sklearn.model_selection import train_test_split


def resolve_conflict(group):
    """
    This function priortizes 'face_with_mask' classname over others.
    """
    if 'face_with_mask' in group['classname'].values:
        return group[group['classname'] == 'face_with_mask']
    else:
        return group.iloc[:1]

def map_classnames(classname):
    """
    This function merges relevant classnames into 2 custom-classes
    that are more or less, masks or no masks.
    """
    if classname in ['face_with_mask', 'mask_colorful', 'mask_surgical','face_other_covering', 'scarf_bandana']:
        return 'mask'
    elif classname in ['face_no_mask']:
        return 'no_mask'

def create_clean_csv(data):
    """
    This function takes a csv file, cleans it, and saves it to a new CSV file.
    Steps:
    1. Handle duplicate entries
    2. Resolve conflicts by choosing 'face_with_mask' over others
    3. Categorize into relevant classnames.
    4. Drop rows where 'classname' is None.
    5. Save output as cleaned_csv to data directory.
    """
    # Skip if annotation already exists
    if os.path.exists(ANNOTATION_PATH):
        print(f'Annotations already exist at {ANNOTATION_PATH}')
        return

    print(f"Cleaning csv...")

    # Create output directory for our cleaned csv, if not yet exists.
    if not os.path.exists(DATA_DIRECTORY_PATH):
        os.makedirs(DATA_DIRECTORY_PATH)
   
    # Step 0: Exploratory Data Analysis
    unique_class_names = data['classname'].unique()

    # Step 1: Handle duplicate entries
    data = data.drop_duplicates()

    # Step 2: Resolve conflicts by choosing 'face_with_mask' over others
    data = data.groupby('name').apply(resolve_conflict).reset_index(drop=True)

    # Step 3: Categorize into relevant classnames
    data.loc[:,'classname'] = data['classname'].apply(map_classnames)

    # Step 4: Drop rows where 'classname' is None (if any)
    data = data.dropna(subset=['classname'])
    
    # Step 5: Save output file to our data directory
    data.to_csv(ANNOTATION_PATH, index=False)

    print(f"Data processed successfully and saved to {ANNOTATION_PATH}")

def process_images(data, IMAGES_DIR):
    """
    This function copies images from the csv from the entire-dataset for training.
    Steps:
    1. Create a list of images.
    2. Find useful images from the dataset for training.
    3. Copy useful images to /data/images for training.
    """

    # Skip if images directory already exists
    if os.path.exists(IMAGES_OUTPUT_DIRECTORY_PATH):
        print(f"Skipping images already processed at {IMAGES_OUTPUT_DIRECTORY_PATH}")
        return

    # Step 1: Create a list of images.
    images_list = list(data['name'])

    print(f'Processing {len(images_list)} images for training. Please hold on.. ')

    # Step 2: Prepare the output directory for the images, if not yet exist.
    if not os.path.exists(IMAGES_OUTPUT_DIRECTORY_PATH):
        os.makedirs(IMAGES_OUTPUT_DIRECTORY_PATH)

    # Step 3: Copy useful images from the dataset to /data/images for training.
    image_count=0
    for image in images_list:
        image_path = os.path.join(IMAGES_DIR, image)
        try:
            # Copy the image to the output directory.
            shutil.copy(image_path, IMAGES_OUTPUT_DIRECTORY_PATH)
            image_count +=1
        except Exception as e:
            # Handle any exceptions that occur during the copying process.
            print(f"Error processing {image}: {str(e)}")
    
    print(f"{ 'All' if image_count == len(images_list) else {image_count}} images processed using {ANNOTATION_PATH} and saved to {IMAGES_OUTPUT_DIRECTORY_PATH}!")



