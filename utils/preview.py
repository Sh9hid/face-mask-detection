import os
import pandas as pd
import cv2

def draw_centered_bounding_boxes(csv_file_path, images_folder_path):
    """
    This function takes in csv files, 

    """


    # Read the data from the CSV file
    data = pd.read_csv(csv_file_path)

    # Create a dictionary to group bounding boxes by image
    image_boxes = {}
    for index, row in data.iterrows():
        image_path = os.path.join(images_folder_path, row['name'])
        x1, y1, x2, y2, label = row['x1'], row['y1'], row['x2'], row['y2'], row['classname']
        if image_path not in image_boxes:
            image_boxes[image_path] = []
        image_boxes[image_path].append((x1, y1, x2, y2, label))

    # Function to find the encompassing bounding box and center it
    def find_encompassing_box(image_width, image_height, boxes):
        min_x1 = image_width
        min_y1 = image_height
        max_x2 = 0
        max_y2 = 0

        for x1, y1, x2, y2, label in boxes:
            min_x1 = min(min_x1, x1)
            min_y1 = min(min_y1, y1)
            max_x2 = max(max_x2, x2)
            max_y2 = max(max_y2, y2)

        # Calculate the center of the encompassing bounding box
        center_x = (min_x1 + max_x2) // 2
        center_y = (min_y1 + max_y2) // 2

        # Determine the size of the new bounding box
        new_width = int(image_width * 0.8)
        new_height = int(image_height * 0.8)

        # Calculate the new bounding box coordinates centered around the original center
        new_x1 = max(0, center_x - new_width // 2)
        new_y1 = max(0, center_y - new_height // 2)
        new_x2 = min(image_width, center_x + new_width // 2)
        new_y2 = min(image_height, center_y + new_height // 2)

        return [(new_x1, new_y1, new_x2, new_y2, label)]

    # Draw bounding boxes on images
    for image_path, boxes in image_boxes.items():
        image = cv2.imread(image_path)
        image_height, image_width, _ = image.shape
        
        # Find the encompassing bounding box and center it
        encompassing_box = find_encompassing_box(image_width, image_height, boxes)
        
        # Draw the bounding boxes
        for x1, y1, x2, y2, label in encompassing_box:
            color = (0, 255, 0)  # Green color for the bounding box
            thickness = 2  # Thickness of the bounding box
            cv2.rectangle(image, (x1, y1), (x2, y2), color, thickness)
            cv2.putText(image, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, color, 2)
        
        cv2.imshow('Image', image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

# Call the function
draw_centered_bounding_boxes('data/cleaned_data.csv', 'data/images')