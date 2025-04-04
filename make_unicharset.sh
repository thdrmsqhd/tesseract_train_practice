#!/bin/bash

# 박스 파일들이 들어 있는 디렉토리
BOX_DIR="image"

# unicharset_extractor 명령을 모든 .box 파일에 대해 실행
echo "▶️ Extracting unicharset from all .box files in $BOX_DIR..."

unicharset_extractor "$BOX_DIR"/*.box

echo "✅ Done! unicharset 생성 완료 (결과 파일: ./unicharset)"
