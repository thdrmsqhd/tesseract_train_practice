#!/bin/bash

# 이미지가 들어 있는 디렉토리
IMG_DIR="/data/processed_image"

# tessdata 경로가 필요한 경우 설정
# export TESSDATA_PREFIX="/data/tessdata"

# 반복적으로 모든 PNG 파일 처리
for img in "$IMG_DIR"/*.png; do
    # 파일 이름에서 확장자 제거
    filename="${img%.*}"

    echo "▶️ Processing: $img"
    
    tesseract "$img" "$filename" \
        --psm 6 \
        --oem 1 \
        -l eng \
        -c tessedit_char_whitelist=0123456789. \
        batch.nochop makebox
done

echo "✅ All .box files generated!"
