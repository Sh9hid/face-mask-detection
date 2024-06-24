import os
import sys
import pandas as pd
from config.config import FILE_PATH, IMAGES_DIR, VIDEOS_DIR, ANNOTATION_PATH, CLEANED_IMAGES_PATH, TRAINING_CLS_DATA
from utils.clean import create_clean_csv, process_images
from utils.prepare import split_and_copy_images
from utils.train import train_model
from utils.inference import infer


def main():
    # Step 1: Clean the data
    # 1.1 : Load the dataset
    data = pd.read_csv(FILE_PATH)

    # 1.2: Fix our data: Apply create_clean_csv
    clean_csv = create_clean_csv(data)

    # 1.3: Process images for training
    process_images(data, IMAGES_DIR)

    # Step 2:  Split data into 80/20 train and val sets respectively.
    split_and_copy_images(ANNOTATION_PATH, CLEANED_IMAGES_PATH)
 
    # Step 3: Train the model 
    # 3.1: Select any model of your choice
    model = 'yolov8n-cls.pt'

    # 3.2: Train model
    trained_model = train_model(model)

    # Step 4: Infer videos on your last best-checkpoint
    videos_dir = VIDEOS_DIR

    for video_file in os.listdir(VIDEOS_DIR):
        video_path = os.path.join(VIDEOS_DIR, video_file)
        print(f'Starting inference on {video_path}')

        # Perform inference
        infer(video_path, trained_model)

    print("Outputs saved to runs/classify/ directory successfully!")

if __name__ == "__main__":
    main()