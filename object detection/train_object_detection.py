import os
import torch 
from torch import load, save # for further training
import ultralytics

# Train the model for object-detection tasks
results = model.train(data='mask_detection.yaml', epochs=20, imgsz=640)

# Verify import 
ultralytics.checks()

# Step 1: Load model for training
model = YOLO('yolov8n.pt') # Nano model ideal for training

# Step 2: Train model on mask no-mask
results = model.train(data="data/", imgsz=800, batch=8, epochs=10, save = True, plots=True)

# Step 3: Optional: Set model to evaluation mode
model.eval()

# Step 4: Optional: export to onnx format
success = model.export(format="onnx")

# Step 5:Predict on videos
model.predict('data/train/mask/1862.jpg', save = True, imgsz = 320, conf = 0.5)


