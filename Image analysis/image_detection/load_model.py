import os
import torch
import ultralytics
from roboflow import Roboflow

def load_model():
    # GPU에서 텐서 생성
    tensor_on_gpu = torch.tensor([1.0, 2.0, 3.0], device='cuda')
    print(tensor_on_gpu)

    # 임포트 확인
    ultralytics.checks()
    
    HOME = os.getcwd()
    # 데이터셋 디렉터리 생성
    datasets_folder = os.path.join(HOME, "datasets")
    os.makedirs(datasets_folder, exist_ok=True)

    # Roboflow에서 데이터 불러오기
    # api_key, model_id 입력
    rf = Roboflow(api_key="")
    project = rf.workspace("").project("")
    dataset = project.version(1).download("yolov9")

    # YOLOv9 모델 설치
    !git clone https://github.com/SkalskiP/yolov9.git
    !pip3 install -r /content/datasets/yolov9/requirements.txt -q
    
    weights_folder = os.path.join(HOME, "weights")
    os.makedirs(weights_folder, exist_ok=True)
    # 사전 훈련된 가중치 다운로드
    !wget -P {weights_folder} -q https://github.com/WongKinYiu/yolov9/releases/download/v0.1/yolov9-c.pt
    !wget -P {weights_folder} -q https://github.com/WongKinYiu/yolov9/releases/download/v0.1/yolov9-e.pt
    !wget -P {weights_folder} -q https://github.com/WongKinYiu/yolov9/releases/download/v0.1/gelan-c.pt
    !wget -P {weights_folder} -q https://github.com/WongKinYiu/yolov9/releases/download/v0.1/gelan-e.pt
    
    return HOME

# 함수 호출하여 모델 및 데이터 불러오기
HOME = load_model()
