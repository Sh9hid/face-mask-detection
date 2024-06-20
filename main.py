import os
import sys
import pandas as pd
from config.config import FILE_PATH, IMAGES_DIR, VIDEOS_DIR
from utils.clean import create_clean_csv, process_images
from utils.prepare import split_and_copy_images
from utils.train import train_model
from utils.inference import infer


def main():
    # Step 1: Clean the data
    # 1.1 : Load the dataset
    data = pd.read_csv(FILE_PATH)

    print("Cleaning the data...")

    # 1.2: Fix our data: Apply create_clean_csv
    clean_csv = create_clean_csv(data)

    # 1.3: Process images for training
    process_images(data, IMAGES_DIR)

    # Step 2: Prepare data for training
    # 2.1 : Load useful annotations and data from dataset
    annotation_path = 'data/cleaned_data.csv'
    images_path = 'data/images'

    output_path = 'data/data'

    # 2.2: Apply split and copy images to respective paths 
    split_and_copy_images(annotation_path, images_path, output_path)

    # Step 3: Train the model
    
    trained_model = train_model('yolov8n-cls.pt') # Here we are using classification nano for obvious compute reasons
   
    # Step 4:# Infer with your best-checkpoint.
    videos_dir = VIDEOS_DIR
    for video_file in os.listdir(videos_dir):
        video_path = os.path.join(videos_dir, video_file)
        infer(video_path, trained_model)

    print("Outputs saved to runs/classify/ directory successfully!")

if __name__ == "__main__":
    main()