import os
from PIL import Image

def convert_jpeg_to_png(directory):
    for filename in os.listdir(directory):
        img_path = os.path.join(directory, filename)
        # Check if the file is an image
        if filename.lower().endswith(('.jpeg', '.jpg', '.png')):
            with Image.open(img_path) as img:
                # Get DPI value
                dpi = img.info.get('dpi', 'DPI information not available')
                print(f"DPI of {img_path}: {dpi}")
        
            

if __name__ == "__main__":
    directory = "/Users/song-geunbong/Documents/tesseract_prac"
    convert_jpeg_to_png(directory)
