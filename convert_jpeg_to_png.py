import os
from PIL import Image

# Get the list of all files in the current directory
for filename in os.listdir('./image'):
    # Check if the file has a .jpg extension
    if filename.lower().endswith('.jpg'):
        # Construct the full file path
        file_path = os.path.join('./image', filename)
        # Open the image file
        with Image.open(file_path) as img:
            # Remove the .jpg extension and add .png
            png_filename = os.path.splitext(filename)[0] + '.png'
            # Save the image as a .png file in the same directory
            img.save(os.path.join('./image', png_filename), 'PNG')

