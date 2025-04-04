### Docker Image build
`docker build -t tesseract-train-550 .`
---

### Docker conatainer
`docker run -it --name tess_train -v "C:\workspace\tesseract_train_practice:/data" tesseract-train-550`
---

### MakeBox
`tesseract image/00001.png image/00001 --psm 6 --oem 1 -l eng -c tessedit_char_whitelist=0123456789. batch.nochop makebox`
`./make_boxes.sh`
---

### 박스 수정
``
---

### unicharset 생성
`unicharset_extractor image/00001.box`
`./make_unicharset.sh`
---

### lstmf 파일 생성
`tesseract image/00001.png image/00001 --psm 6 lstm.train`
`./make_lstmf.sh`
---

### train_list 생성
`python generate_train_list.py`
---

### check point 생성
```
lstmtraining \
  --continue_from eng.lstm \
  --model_output checkpoints/custom \
  --traineddata eng.traineddata \
  --train_listfile train.list \
  --max_iterations 5000
```
---

### train data 생성
```
lstmtraining \
  --stop_training \
  --continue_from checkpoints/custom_checkpoint \
  --traineddata eng.traineddata \
  --model_output traineddata/custom_finetuned.traineddata
```
---

### traineddata를 이용해서 테스트 -> 결과가 output.txt로 출력됨
```
tesseract image/00001.png output_text \
  --tessdata-dir traineddata/ \
  --psm 7 \
  --oem 1 \
  -l custom_finetuned \
  -c tessedit_char_whitelist=0123456789.
```