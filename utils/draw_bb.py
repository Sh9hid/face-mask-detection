import pandas as pd
import cv2
import os

def draw_bbox(image_file):
    """
    Draw bounding boxes on an image based on the data in the cleaned_data.csv file.
    Opens a window to see the label. Waits for key press to close.

    Parameters:
    image_file (str): The path to the image file.

    Returns:
    None
    """
    # Load the file
    df = pd.read_csv('data/cleaned_data.csv')

    # Iterate over each row in the DataFrame
    for index, row in df.iterrows():
        filename = row['name']
        x1, y1, x2, y2 = int(row['x1']), int(row['y1']), int(row['x2']), int(row['y2'])
        classname = row['classname']

        # Check if the image file exists
        filepath = os.path.join('data', 'images', f'{filename}')
        if os.path.exists(filepath):
            img = cv2.imread(filepath)

            # Draw the bounding box
            cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)

            # Add the class name
            cv2.putText(img, classname, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

            # Display the image
            cv2.imshow('Image', img)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

            # Print a message after each image is processed
            print(f"Image {filename} processed.")
        else:
            print(f"Error: File {filename} does not exist.")