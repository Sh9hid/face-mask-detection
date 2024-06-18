import os
from dotenv import load_dotenv


load_dotenv()

FILE_PATH = os.getenv('FILE_PATH')
IMAGES_DIR = os.getenv('IMAGES_DIR')
VIDEOS_DIR = os.getenv('VIDEOS_DIR')
