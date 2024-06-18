import os
import torch 
from torch import load
import ultralytics
from ultralytics import YOLO

# Verify import 
ultralytics.checks()


# Step 1: Load model for training
model = YOLO('yolov8n-cls.pt') # Ideal for training

# Step 2: Train model on mask no-mask
results = model.train(data="data/data_cls", imgsz=800, batch=8, epochs=10, save = True, plots=True)

# Step 3: Optional: Set model to evaluation mode
model.eval()

# Step 4: Optional: export to onnx format
success = model.export(format="onnx") # or torch.save()

# # Step 5:Inference on videos


# model.predict('data/train/mask/1862.jpg', save = True, imgsz = 320)
