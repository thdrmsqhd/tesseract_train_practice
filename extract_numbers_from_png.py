import os
from PIL import Image
import pytesseract

def extract_numbers_from_png(directory):
    for filename in os.listdir(directory):
        if filename.lower().endswith('.png'):
            png_path = os.path.join(directory, filename)
            
            # Open the PNG file and extract text
            with Image.open(png_path) as img:
                text = pytesseract.image_to_string(img, config='--psm 6 digits')
                print(f"Extracted numbers from {png_path}:")
                print(text.strip())

if __name__ == "__main__":
    directory = "/Users/song-geunbong/Documents/tesseract_prac"
    extract_numbers_from_png(directory)
