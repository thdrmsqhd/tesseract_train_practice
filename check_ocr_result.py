import os
import pytesseract
from PIL import Image
import csv

# image 폴더 경로
image_dir = "image"

# 폴더 내 이미지 파일 가져오기
image_files = [f for f in os.listdir(image_dir) if f.lower().endswith(".png")]

for image_file in sorted(image_files):
    image_path = os.path.join(image_dir, image_file)
    image = Image.open(image_path)

    # 텍스트 인식
    text = pytesseract.image_to_string(image, config="--psm 7 -l custom_finetuned")

    # TSV에서 confidence 가져오기
    tsv_data = pytesseract.image_to_data(image, config="--psm 7 -l custom_finetuned", output_type=pytesseract.Output.DICT)
    confs = [int(c) for c in tsv_data["conf"] if c != '-1'][-1]
    # avg_conf = round(sum(confs) / len(confs), 2) if confs else 0

    print(f"📄 파일: {image_file}")
    print(f"📝 인식 결과: {text.strip()}")
    print(f"✅ 평균 Confidence: {confs}%")
    print("-" * 50)
