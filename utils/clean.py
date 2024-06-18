import os
from config import *
import pandas as pd
import shutil
from sklearn.model_selection import train_test_split


def create_clean_csv(data):
    """
    This function takes a dataset, cleans it, and saves it to a new CSV file.

    Steps:
    1. Handle duplicate entries
    2. Resolve conflicts by choosing 'face_with_mask' over others
    3. Categorize into relevant classnames
    4. Drop rows where 'classname' is None
    """

    # Exploratory Data Analysis
    unique_class_names = data['classname'].unique()

    # # Step 1: Handle duplicate entries
    # data = data.drop_duplicates()

    # # Step 2: Resolve conflicts by choosing 'face_with_mask' over others
    # def resolve_conflict(group):
    #     if 'face_with_mask' in group['classname'].values:
    #         return group[group['classname'] == 'face_with_mask']
    #     else:
    #         return group.iloc[:1]

    # Step 3: Categorize into relevant classnames
    def map_classnames(classname):
        if classname in ['face_with_mask', 'mask_colorful', 'mask_surgical',
                         'face_other_covering', 'scarf_bandana']:
            return 'mask'
        elif classname in ['face_no_mask']:
            return 'no_mask'

    # Apply map_classnames function
    data['classname'] = data['classname'].apply(map_classnames)

    # Apply resolve conflicts function and group by name
    data = data.groupby('name').apply(resolve_conflict).reset_index(drop=True)

    # Step 4: Drop rows where 'classname' is None (if any)
    data = data.dropna(subset=['classname'])

    # Save the cleaned dataset to a new CSV file
    output_path = 'data/cleaned_data.csv'
    data.to_csv(output_path, index=False)

    print(f"Data processed successfully and saved to {output_path}")

# Load the dataset
data = pd.read_csv(FILE_PATH)

# Fix our data: Apply create_clean_csv
create_clean_csv(data)


# Get useful images from the dataset for training. 
def process_images(data, IMAGES_DIR):
    """
    This function selects useful images from the entire-dataset for training.

    Steps:
    1. Create a list of images.
    2. Find useful images from the dataset for training.
    3. Copy useful images to /data/images for training.
    """

    # Step 1: Create a list of images.
    images_list = list(data['name'])

    # Step 2: Prepare the output directory for the images.
    IMAGES_OUTPUT_DIRECTORY_PATH = 'data/images'
    if not os.path.exists(IMAGES_OUTPUT_DIRECTORY_PATH):
        os.makedirs(IMAGES_OUTPUT_DIRECTORY_PATH)

    # Step 3: Copy useful images from the dataset to /data/images for training.
    for image in images_list:
        image_path = os.path.join(IMAGES_DIR, image)
        try:
            # Copy the image to the output directory.
            shutil.copy(image_path, IMAGES_OUTPUT_DIRECTORY_PATH)
            print(f"Processed {image} to {IMAGES_OUTPUT_DIRECTORY_PATH}")
        except Exception as e:
            # Handle any exceptions that occur during the copying process.
            print(f"Error processing {image}: {str(e)}")


# Process images for training
process_images(data, IMAGES_DIR)


