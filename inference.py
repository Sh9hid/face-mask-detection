import ultralytics
from ultralytics import YOLO
from config.config import VIDEOS_DIR



# Load your best-checkpoint. 
model = YOLO('models\best.pt') # check path, train2\ if this is your second run

# videos = VIDEOS_DIR
# print(videos)

# TODO: load vids from VIDEOS_DIR on model.predict()


# model.predict()