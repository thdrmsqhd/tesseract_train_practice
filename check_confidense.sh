#!/bin/bash

IMG_DIR="image"
OUTPUT="analysis_result.csv"

echo "filename,dpi,recognized_text,avg_confidence,box_count" > "$OUTPUT"

for img in "$IMG_DIR"/*.png; do
    filename=$(basename "$img")
    base="${filename%.*}"

    # DPI 확인
    dpi=$(identify -format "%x" "$img" | sed 's/[^0-9]*//g')

    # 텍스트 및 confidence 추출
    tesseract "$img" "$IMG_DIR/$base" --psm 7 --oem 1 -l traineddata/custom_finetuned \
      -c tessedit_char_whitelist=0123456789. \
      tsv > /dev/null 2>&1

    # 평균 confidence 계산
    confs=$(awk -F'\t' 'NR>1 && $10 ~ /^[0-9]+$/ {sum += $10; count++} END {if (count>0) print sum/count; else print 0}' "$IMG_DIR/$base.tsv")

    # 인식 결과 텍스트
    text=$(cat "$IMG_DIR/$base.txt" 2>/dev/null | tr '\n' ' ' | sed 's/"/""/g')

    # 박스 개수
    boxes=$(grep -c "^" "$IMG_DIR/$base.box" 2>/dev/null)

    echo "\"$filename\",$dpi,\"$text\",$confs,$boxes" >> "$OUTPUT"
done

echo "✅ 분석 결과가 $OUTPUT 에 저장되었습니다."
