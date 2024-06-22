import os
import cv2
import pandas as pd
from PIL import Image

def read_data(csv_file_path):
    return pd.read_csv(csv_file_path)

def group_boxes_by_image( data, images_folder_path):
    """
    Create dictionary of images with their labels in x1, y1, x2, y2.
    :params 
    :returns dict key-value pairs of images and their label dimensions.
    """

    image_boxes = {}
    for index, row in data.iterrows():
        image_path = os.path.join(images_folder_path, row['name'])
        x1, y1, x2, y2, label = row['x1'], row['y1'], row['x2'], row['y2'], row['classname']
        if image_path not in image_boxes:
            image_boxes[image_path] = []   
        image_boxes[image_path].append((x1, y1, x2, y2, label))
    return image_boxes


def save_yolo_labels(image_path, boxes, yolo_labels_path):
    """
    Save new labels to yolo object detection format.
    :params path/to/images
    :params label boxes (new and enlarged)
    :params

    """
    image = Image.open(image_path)
    image_width, image_height = image.size
    filename, _ = os.path.splitext(os.path.basename(image_path))
    label_filename = f'{filename}.txt'
    label_file_path = os.path.join(yolo_labels_path, label_filename)

    with open(label_file_path, 'w') as label_file:
        
        # Calculate the center, width, and height of the bounding box
        for x1, y1, x2, y2, label in boxes:
            x_center = (x1 + x2) / 2.0
            y_center = (y1 + y2) / 2.0
            width = x2 - x1
            height = y2 - y1

            # Normalize coordinates by image dimensions
            x_center /= image_width
            y_center /= image_height
            width /= image_width
            height /= image_height

            class_id = 0 if label == 'mask' else 1

            label_file.write(f'{class_id} {x_center} {y_center} {width} {height}\n')


def draw_centered_bounding_boxes(csv_file_path, images_folder_path, yolo_labels_path):
    """

    """

    data = read_data(csv_file_path)
    image_boxes = group_boxes_by_image(data, images_folder_path)

    for image_path, boxes in image_boxes.items():
        image = cv2.imread(image_path)
        image_height, image_width, _ = image.shape

        encompassing_box = fix_labels(image_width, image_height, boxes)
        save_yolo_labels(image_path, encompassing_box, yolo_labels_path)

# Call the function with appropriate paths
draw_centered_bounding_boxes('data/cleaned_data.csv', 'data/images', 'data/data_od/labels')