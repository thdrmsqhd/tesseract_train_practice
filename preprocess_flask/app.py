from flask import Flask, render_template, send_from_directory, request, jsonify
import os
import cv2
import numpy as np

app = Flask(__name__)

# 고정된 경로로 이미지 디렉터리 지정
image_directory = '/data/image'
output_directory = '/data/processed_image'

app.config['IMAGE_FOLDER'] = image_directory
app.config['OUTPUT_FOLDER'] = output_directory

def get_image_list(directory, url_prefix=''):
    image_extensions = ('.png', '.jpg', '.jpeg', '.gif', '.bmp')
    return [f'{url_prefix}/{f}' for f in os.listdir(directory) if f.lower().endswith(image_extensions)]

@app.route('/')
def home():
    image_list = get_image_list(app.config['IMAGE_FOLDER'], '/images')[:5]
    processed_list = get_image_list(output_directory, '/processed_images')[:5]
    image_pairs = zip(image_list, processed_list)
    return render_template('index.html', image_list=image_list, processed_list=processed_list, image_pairs=image_pairs)

@app.route('/images/<path:filename>')
def serve_image(filename):
    return send_from_directory(app.config['IMAGE_FOLDER'], filename)

@app.route('/processed_images/<path:filename>')
def serve_processed_image(filename):
    return send_from_directory(output_directory, filename)

@app.route('/process', methods=['POST'])
def process_images():
    data = request.get_json()
    batch = data.get('batch', False)  # batch 모드 여부 (true이면 모든 이미지 처리)
    gaussian = int(data.get('gaussian', 0))
    if gaussian % 2 == 0 and gaussian > 0:
        gaussian += 1  # 홀수 값 보정

    median = int(data.get('median', 0))
    if median % 2 == 0 and median > 0:
        median += 1  # 홀수 값 보정

    threshold = int(data.get('threshold', 0))
    
    # 출력 디렉터리 생성 (없으면 생성)
    os.makedirs(app.config['OUTPUT_FOLDER'], exist_ok=True)
    
    # 전처리 파라미터를 txt 파일에 기록 (각 호출마다 파라미터와 현재 시간을 기록)
    import datetime
    params_text = f"{datetime.datetime.now()}: gaussian={gaussian}, median={median}, threshold={threshold}\n"
    params_file = os.path.join(app.config['OUTPUT_FOLDER'], 'processing_parameters.txt')
    with open(params_file, 'a') as f:
        f.write(params_text)
    
    processed_images = []
    
    # batch 모드이면 모든 이미지를, 아니면 UI에 보이는 첫 5개의 이미지만 처리
    all_images = [f for f in os.listdir(app.config['IMAGE_FOLDER']) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]
    image_list = all_images if batch else all_images[:5]
    
    for image_name in image_list:
        input_path = os.path.join(app.config['IMAGE_FOLDER'], image_name)
        output_path = os.path.join(app.config['OUTPUT_FOLDER'], image_name)
        image = cv2.imread(input_path)
        if image is None:
            continue

        if gaussian > 0:
            image = cv2.GaussianBlur(image, (gaussian, gaussian), 0)
        if median > 0:
            image = cv2.medianBlur(image, median)
        if threshold > 0:
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            _, image = cv2.threshold(gray, threshold, 255, cv2.THRESH_BINARY)
        cv2.imwrite(output_path, image)
        processed_images.append(f'/processed_images/{image_name}')
    
    return jsonify({'processed_image_urls': processed_images})



def initialize_output_directory():
    os.makedirs(output_directory, exist_ok=True)
    for image_name in get_image_list(image_directory, '/images'):
        source_path = os.path.join(image_directory, os.path.basename(image_name))
        destination_path = os.path.join(output_directory, os.path.basename(image_name))
        if not os.path.exists(destination_path):
            cv2.imwrite(destination_path, cv2.imread(source_path))

if __name__ == '__main__':
    initialize_output_directory()
    app.run(debug=True)
