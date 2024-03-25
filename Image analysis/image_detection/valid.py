import load_model  # load_model.py 임포트

# 데이터와 모델 미리 설정
HOME = load_model.load_model()

# 검증
!python val.py \
--data "/content/datasets/image_detection-1/data.yaml" \
--weights "/content/datasets/yolov9/runs/train/exp4/weights/best.pt"

# valid 결과 저장
!zip -r vali_result.zip /content/datasets/yolov9/runs/val/exp