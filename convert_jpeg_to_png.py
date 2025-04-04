import os
from PIL import Image
import cv2
import numpy as np

# Get the list of all files in the current directory
for filename in os.listdir('./image'):
    # Check if the file has a .jpg extension
    if filename.lower().endswith('.jpg'):
        # Construct the full file path
        file_path = os.path.join('./image', filename)
        # Open the image file
        with Image.open(file_path) as img:
            # Convert the PIL image to a NumPy array
            img_array = np.array(img)

            # Resize the image using OpenCV
            scale_factor = 3
            new_size = (int(img.width * scale_factor), int(img.height * scale_factor))
            resized_img_array = cv2.resize(img_array, new_size, interpolation=cv2.INTER_LANCZOS4)

            # Convert the resized NumPy array back to a PIL image
            resized_img = Image.fromarray(resized_img_array)

            # Remove the .jpg extension and add .png
            png_filename = os.path.splitext(filename)[0] + '.png'

            # Save the resized image as a .png file in the same directory
            resized_img.save(os.path.join('./image', png_filename), 'PNG')
        # Remove the original .jpg file
        os.remove(file_path)

