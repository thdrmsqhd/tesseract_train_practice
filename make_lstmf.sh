#!/bin/bash

IMG_DIR="image"

echo "▶️ 이미지 + .box → .lstmf 파일 생성 시작..."

for img in "$IMG_DIR"/*.png; do
    filename="${img%.*}"

    if [[ -f "$filename.box" ]]; then
        echo "🧠 Processing: $img + $filename.box"
        tesseract "$img" "$filename" --psm 6 lstm.train
    else
        echo "⚠️  Skipping $img (box 파일 없음)"
    fi
done

echo "✅ 모든 .lstmf 파일 생성 완료!"
