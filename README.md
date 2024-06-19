# Face Mask Detection (You-Only-Look-Once v8)
Here's the link to the [Google Colab](https://colab.research.google.com/drive/1bnn0NgoFH7i2Aa0mad_mABcfYUbEqkkM?usp=sharing) notebook.

 ## Installation

 1. Create a new environment

```
python -m venv .venv
.venv/Scripts/activate # on windows
source .venv/bin/activate
```
2. Install Dependencies

```
pip install -r requirements.txt
```

3. Run app for training

```
python main.py  

```
or perform inference from the cli using,

```
yolo predict model='models\best.pt' source=' .mp4/.jpeg/etc'
```

## Summary
- Object Detection - Trained on YOLOv8n.pt (Model underfits, checkpoints not added till yet)
- Classification - Trained on YOLOv8n-cls.pt
- Mask, No Mask Detection and Classification.
- Custom Dataset (using CV). Labels corrected using OpenCV and observation.
- Trained on YOLOv8, locally for both classification and object-detection.
- Classification model available. Classes 0: Mask, 1: No-Mask
- Checkpoint for classification - models/best.pt', object detection - yet to converge.
- Helper functions for both classification and detection in utils/
- Output video directory -> output-vids/
  
## Roadmap

- More readability, more simplicity. Better code organisation.
- Better documentation.
- Deploy the model. 
- Find better data cleaning methods.
- Try and achieve better accuracy on the same dataset.
- Ask senior CV Engineers on the inaccurate label problem.
- Write down use cases and try and build niched down cv models.(Reverse blackbox approach)
