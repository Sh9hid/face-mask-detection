import ultralytics
from ultralytics import YOLO
from config.config import VIDEOS_DIR

# TODO: set correct output VIDEOS_DIR on model.predict()
# !yolo predict model='models\best.pt' source='videos' 
def infer(video_path, model_checkpoint):
    return model.predict(source=video_path, save=True)


