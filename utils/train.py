import os
import torch 
from torch import load
import ultralytics
from ultralytics import YOLO

# verify imports
ultralytics.checks()


def train_model(model_path):
    
    # Step 1: Load model for training
    model = YOLO(model_path) # Ideal for training
    
    # Step 2: Train model on mask no-mask
    # Training 
    print('Starting model training.  ')
    results = model.train(data="data/data_cls", imgsz=800, batch=8, epochs=10, save = True, plots=True)
   
    # Step 3: Optional: Set model to evaluation mode
    model.eval()

    #Step 4: Optional: export to onnx format
    return  model.export(format="onnx") # or torch.save()


