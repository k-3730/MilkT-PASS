import load_model  # load_model.py 임포트

# 데이터와 모델 미리 설정
HOME = load_model.load_model()

# 학습 실행
!python train.py \
--batch 8 --epochs 100 --img 640 --device cuda:0 --min-items 0 --close-mosaic 15 \
--data /content/datasets/image_detection-1/data.yaml \
--weights /content/weights/yolov9-c.pt \
--cfg /content/datasets/yolov9/models/detect/gelan-c.yaml \
--hyp /content/datasets/yolov9/data/hyps/hyp.scratch-high.yaml

# train 결과 저장
!zip -r train_result.zip /content/datasets/yolov9/runs/train/exp4
