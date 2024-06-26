import os
from dotenv import load_dotenv

load_dotenv()

# Input 
FILE_PATH = os.getenv('FILE_PATH')
IMAGES_DIR = os.getenv('IMAGES_DIR')
VIDEOS_DIR = os.getenv('VIDEOS_DIR')

# Prepared
DATA_DIRECTORY_PATH = os.getenv('DATA_DIRECTORY_PATH')
ANNOTATION_DIR = os.getenv('ANNOTATION_DIR')
IMAGES_OUTPUT_DIRECTORY_PATH = os.getenv('IMAGES_OUTPUT_DIRECTORY_PATH')
ANNOTATION_PATH= os.getenv('ANNOTATION_PATH')
CLEANED_IMAGES_PATH = os.getenv('CLEANED_IMAGES_PATH')
TRAINING_CLS_DATA = os.getenv('TRAINING_CLS_DATA')
