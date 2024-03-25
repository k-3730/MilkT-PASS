import load_model  # load_model.py 임포트

# 데이터와 모델 미리 설정
HOME = load_model.load_model()

# 테스트
!python detect.py \
--img 640 --conf 0.1 --device 0 \
--weights /content/datasets/yolov9/runs/train/exp4/weights/best.pt \
--source /content/datasets/image_detection-1/test/images \
--save-txt

# test 결과 저장
!zip -r test_result_epoch100_240307.zip /content/datasets/yolov9/runs/detect/exp