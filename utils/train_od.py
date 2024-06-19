import os
import torch 
from torch import load, save # for further training
import ultralytics
from ultralytics import YOLO

# Train the model for object-detection tasks

# Verify import 
ultralytics.checks()

# Step 1: Load model for training
model = YOLO('yolov8n.pt') # Nano model for training

# Step 2: Train model on mask no-mask. Change settings at ultralytics/settings.py 
results = model.train(data='mask_detection.yaml', epochs=20, plots=True)
 
# Step 3: Optional: Set model to evaluation mode
model.eval()

# Step 4: Optional: export to onnx format
success = model.export(format="onnx")

# # Step 5:Predict on videos
# model.predict('data/train/mask/1862.jpg', save = True, imgsz = 320, conf = 0.5)


