# Face Mask Detection (You-Only-Look-Once v8)
Here's the link to the [Google Colab](https://colab.research.google.com/drive/1bnn0NgoFH7i2Aa0mad_mABcfYUbEqkkM?usp=sharing) notebook.

 ## Installation

 1. Create a new environment

```
python -m venv .venv
.venv/Scripts/activate # on windows
or
source .venv/bin/activate # on linux
```
2. Create a new .env file and edit file paths.

```
DATA_DIRECTORY_PATH = 'data/'   # path to root dataset directory
ANNOTATION_PATH = 'data/cleaned_data.csv'   # path to cleaned csv containing bboxes
IMAGES_OUTPUT_DIRECTORY_PATH = 'data/images'    # path to selected images from the entire dataset
CLEANED_IMAGES_PATH = 'data/images'     # path to cleaned images directory
TRAINING_CLS_DATA = 'data/data_cls'     # path to training classification data

# Set your paths here
FILE_PATH = 'path/to/your/CSV'
IMAGES_DIR ='path/to/your/images/directory'
VIDEOS_DIR = 'path/to/your/video/directory'

```

3. Install Dependencies

```
pip install -r requirements.txt
```

4. Run app for training

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
- FIX: Workflows -> Docker Build
