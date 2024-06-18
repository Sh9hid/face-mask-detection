# # List of filenames with corrupt labels or images to ignore during training
# corrupt_files = [
#     "5150.jpg", "5155.jpg", "5185.jpg", "5186.jpg", "5194.jpg", "5249.jpg", 
#     "5253.jpg", "5254.jpg", "5255.jpg", "5259.jpg", "5347.jpg", "5392.jpg", 
#     "5440.jpg", "5495.jpg", "5499.jpg", "5503.png", "5529.png", "5546.jpeg", 
#     "5560.jpg", "5576.jpg", "5579.jpg", "5608.jpg", "5630.jpg", "5664.jpg", 
#     "5678.jpg", "5689.jpg", "5706.jpg", "5734.png", "5918.jpg", "5930.jpg", 
#     "6002.jpg", "6044.jpg", "6047.jpg", "6069.jpg", "6099.jpg", "6152.jpg", 
#     "6170.jpg", "6173.jpg", "6248.jpg", "6255.jpg", "6263.jpg", "6278.jpg", 
#     "6305.jpg", "6375.jpg", "6392.jpg", "6408.png", "6409.png", "4011.png", 
#     "4013.png", "4018.png", "4023.png", "4041.png", "4050.png", "4073.png", 
#     "4076.png", "4107.png", "4114.png", "4141.png", "4148.png", "4151.png", 
#     "4158.png", "4159.png", "4166.png", "4168.png", "4181.png", "4183.png", 
#     "4184.png", "4185.png", "4196.png", "4199.png", "4228.png", "4233.png", 
#     "4239.png", "4249.png", "4271.png", "4307.png", "4310.png", "4329.png", 
#     "4339.png", "4345.png", "4354.png", "4363.png", "4366.png", "4391.png", 
#     "4397.png", "4404.png", "4438.png", "4453.png", "4484.png", "4509.png", 
#     "4535.png", "4555.png", "4582.png", "4593.png", "4614.png", "4636.png", 
#     "4649.png", "4650.png", "4654.png", "4729.png", "4736.png", "4737.png", 
#     "4739.png", "4749.png", "4767.png", "4768.png", "4778.png", "4789.png", 
#     "4791.png", "4804.png", "4811.png", "4828.png", "4831.png", "4836.png", 
#     "4843.png", "4852.png", "4866.png", "4869.png", "4872.png", "4875.png", 
#     "4877.png", "4883.png", "4892.png", "4893.png", "4901.png", "4903.png", 
#     "4926.png", "4946.png", "4952.png", "4973.png", "4997.jpg", "5006.jpg", 
#     "5013.jpg", "5030.jpg", "5059.jpg", "5063.jpg", "5072.jpg", "5096.jpg", 
#     "2897.png", "2898.png", "2902.png", "2918.png", "2963.png", "2970.png", 
#     "2974.png", "2982.png", "2985.png", "3009.png", "3035.png", "3037.png", 
#     "3052.png", "3095.png", "3113.png", "3135.png", "3145.png", "3178.png", 
#     "3180.png", "3206.png", "3207.png", "3219.png", "3239.png", "3240.png", 
#     "3268.png", "3286.png", "3293.png", "3304.png", "3305.png", "3311.png", 
#     "3324.png", "3331.png", "3334.png", "3337.png", "3358.png", "3392.png", 
#     "3396.png", "3405.png", "3452.png", "3459.png", "3462.png", "3467.png", 
#     "3472.png", "3508.png", "3529.png", "3543.png", "3552.png", "3558.png", 
#     "3570.png", "3602.png", "3605.png", "3619.png", "3626.png", "3635.png", 
#     "3643.png", "3645.png", "3658.png", "3662.png", "3670.png", "3671.png", 
#     "3685.png", "3742.png", "3749.png", "3759.png", "3775.png", "3795.png", 
#     "3812.png", "3818.png", "3822.png", "3833.png", "3867.png", "3890.png", 
#     "3899.png", "3920.png", "3925.png", "3929.png", "3934.png", "3936.png", 
#     "3939.png", "3943.png", "3949.png", "3951.png", "3955.png", "3961.png", 
#     "3962.png", "3968.png", "3974.png", "3981.png", 
#     "2036.jpg", "2037.jpg", "2051.jpg", "2073.jpg", "2085.jpg", "2094.jpg", 
#     "2100.jpg", "2130.jpg", "2134.jpg", "2141.jpg", "2183.png", "2185.png", 
#     "2190.png", "2234.png", "2243.png", "2266.png", "2297.png", "2300.png", 
#     "2318.png", "2319.png", "2322.png", "2343.png", "2359.png", "2413.png", 
#     "2422.png", "2461.png", "2526.png", "2530.png", "2550.png", "2562.png", 
#     "2578.png", "2586.png", "2592.png", "2602.png", "2619.png", "2626.png", 
#     "2639.png", "2645.png", "2653.png", "2678.png", "2712.png", "2720.png", 
#     "2737.png", "2772.png", "2773.png", "2790.png", "2799.png", "2805.png", 
#     "2828.png", "2841.png", "2847.png", "2862.png", "2868.png", "2892.png", 
#     "2893.png", "2894.png", 
#     "1812.jpg", "1821.jpg", "1822.jpg", "1827.jpg", "1838.jpg", "1861.jpg", 
#     "1896.jpg", "1901.jpg", "1914.jpg", "1927.jpg", "1932.jpg", "1933.jpg", 
#     "1958.jpg", "1961.png", "1967.jpg", "1968.jpg", "2004.jpg", "2005.jpg", 
#     "2024.jpg",
#     "5006.jpg", "5013.jpg", "5030.jpg", "5059.jpg", "5063.jpg", "5072.jpg", 
#     "5096.jpg", "5150.jpg", "5155.jpg", "5185.jpg", "5186.jpg", "5194.jpg", 
#     "5249.jpg", "5253.jpg", "5254.jpg", "5255.jpg", "5259.jpg", "5347.jpg", 
#     "5392.jpg", "5440.jpg", "5495.jpg", "5499.jpg", "5503.png", "5529.png", 
#     "5546.jpeg", "5560.jpg", "5576.jpg", "5579.jpg", "5608.jpg", "5630.jpg", 
#     "5664.jpg", "5678.jpg", "5689.jpg", "5706.jpg", "5734.png", "5918.jpg", 
#     "5930.jpg", "6002.jpg", "6044.jpg", "6047.jpg", "6069.jpg", "6099.jpg", 
#     "6152.jpg", "6170.jpg", "6173.jpg", "6248.jpg", "6255.jpg", "6263.jpg", 
#     "6278.jpg", "6305.jpg", "6375.jpg", "6392.jpg", "6408.png", "6409.png", 
#     "4011.png", "4013.png", "4018.png", "4023.png", "4041.png", "4050.png", 
#     "4073.png", "4076.png", "4107.png", "4114.png", "4141.png", "4148.png", 
#     "4151.png", "4158.png", "4159.png"]




def prepare_data(train_df, val_df):
    # Define directories for images and labels
    directories = {
        'TRAIN_IMAGES_DIR': 'data/data/images/train',
        'VAL_IMAGES_DIR': 'data/data/images/val',
        'TRAIN_LABELS_DIR': 'data/data/labels/train',    
        'VAL_LABELS_DIR': 'data/data/labels/val'
    }

    # Create directories if they do not exist
    for dir in directories.values():
        os.makedirs(dir, exist_ok=True)

    # Copy images to the corresponding directories
    for index, row in train_df.iterrows():
        filename = row['name']
        shutil.copy(f'data/images/{filename}', directories['TRAIN_IMAGES_DIR'])

    for index, row in val_df.iterrows():
        filename = row['name']

prepare_data(train_df, val_df)

def get_image_dimensions(image_path):
    with Image.open(image_path) as img:
        return img.size

def create_yolo_labels(df, dir):
    for index, row in df.iterrows():
        filename = row['name']
        image_path = os.path.join('data/images', f'{filename}')
        
        try:
            img_width, img_height = get_image_dimensions(image_path)
        except Exception as e:
            print(f"Error opening image {filename}: {e}. Skipping...")
            continue

        # Check if image dimensions are valid
        if img_width <= 0 or img_height <= 0:
            print(f"Invalid image dimensions for {filename}. Skipping...")
            continue

        x1, x2, y1, y2 = row['x1'], row['x2'], row['y1'], row['y2']

        # Check if bounding box coordinates are within image bounds
        if x1 < 0 or x2 < 0 or y1 < 0 or y2 < 0 or x2 > img_width or y2 > img_height or x1 >= x2 or y1 >= y2:
            print(f"Invalid bounding box coordinates for {filename}. Skipping...")
            continue

        # Calculate the center, width, and height of the bounding box
        x_center = (x1 + x2) / 2.0
        y_center = (y1 + y2) / 2.0
        width = x2 - x1
        height = y2 - y1

   `     # Normalize coordinates by image dimensions
        x_center /= img_width
        y_center /= img_height
        width /= img_width
        height /= img_height
`
        # Check if normalized coordinates are within valid range
        if not (0 <= x_center <= 1 and 0 <= y_center <= 1 and 0 <= width <= 1 and 0 <= height <= 1):
            print(f"Invalid normalized coordinates for {filename}. Skipping...")
            continue

        # Determine the class ID
        classname = row['classname']
        class_id = 0 if classname == 'mask' else 1

        # Save the label to a file
        label_path = os.path.join(dir, f'{os.path.splitext(filename)[0]}.txt')
        with open(label_path, 'w') as f:
            f.write(f'{class_id} {x_center} {y_center} {width} {height}\n')

# # Create YOLO labels for training and validation datasets
# create_yolo_labels(train_df, directories['TRAIN_LABELS_DIR'])
# create_yolo_labels(val_df, directories['VAL_LABELS_DIR'])
