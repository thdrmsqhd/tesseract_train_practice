#!/bin/bash

LSTMF_DIR="image"
OUTPUT_FILE="train.list"

echo "▶️ train.list (절대 경로) 생성 중..."

# 기존 파일 삭제
rm -f "$OUTPUT_FILE"

# 모든 .lstmf 파일에 대해 절대 경로로 기록
for file in "$LSTMF_DIR"/*.lstmf; do
    realpath "$file" >> "$OUTPUT_FILE"
done

echo "✅ 완료: 절대 경로로 $OUTPUT_FILE 생성됨!"
