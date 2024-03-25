# !pip install roboflow
# !pip install inference
# !pip install supervision

import os
import cv2
import json
import getpass
import supervision as sv
from roboflow import Roboflow
from inference import get_model
import matplotlib.pyplot as plt


# 모델 불러오기 - API키, model_id 입력
rf = Roboflow(api_key="")
ROBOFLOW_API_KEY = getpass.getpass()
model = get_model(model_id="", api_key=ROBOFLOW_API_KEY)


def process_video(input_video_path, output_folder_path, model, video_file):
    # 동영상 열기
    cap = cv2.VideoCapture(input_video_path)

    if not cap.isOpened():
        print(f"Error opening video file: {input_video_path}")
        return

    frame_rate = cap.get(cv2.CAP_PROP_FPS)
    frame_count = 0
    time_seconds = 0
    class_counts_per_second = {}

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # 동영상 1초당 프레임 추출(30프레임씩 넘어가기)    
        current_time = frame_count / frame_rate
        if int(current_time) > time_seconds:
            time_seconds = int(current_time)
            print(f"Processing frame {frame_count} at {time_seconds} seconds")

            # 이미지에서 신뢰도 0.2이상의 객체 검출
            result = model.infer(frame, confidence=0.2)[0]
            detections = sv.Detections.from_inference(result)

            # 라벨과 바운딩 박스 표기
            label_annotator = sv.LabelAnnotator(text_color=sv.Color.BLACK)
            bounding_box_annotator = sv.BoundingBoxAnnotator()

            annotated_image = frame.copy()
            annotated_image = bounding_box_annotator.annotate(scene=annotated_image, detections=detections)
            annotated_image = label_annotator.annotate(scene=annotated_image, detections=detections)

            # 결과 이미지 저장
            output_image_path = os.path.join(output_folder_path, f'{video_file[:-4]}_frame{time_seconds}.jpg')
            cv2.imwrite(output_image_path, annotated_image)

            # 클래스별 개수 세기
            class_counts = {}
            for detection_tuple in detections:
                detection = detection_tuple
                class_name = detection[-1]['class_name']
                class_counts[class_name] = class_counts.get(class_name, 0) + 1

            class_counts_per_second[time_seconds] = class_counts

        frame_count += 1
    
    # 이미지당 클래스별 개수 제이슨 파일에 저장 
    output_json_path = os.path.join(output_folder_path, f"{video_file[:-4]}_class_counts_per_second.json")
    with open(output_json_path, 'w') as json_file:
        json.dump(class_counts_per_second, json_file)

    cap.release()


def process_videos(input_folder, output_folder, model):
    # 입력 폴더에서 동영상 가져오기    
    video_files = [f for f in os.listdir(input_folder) if f.endswith('.mp4')]
    # 출력 폴더 생성 및 결과 저장
    for video_file in video_files:
        output_folder_name = f"{video_file[:-4]}_output"
        output_folder_path = os.path.join(output_folder, output_folder_name)
        os.makedirs(output_folder_path, exist_ok=True)

        input_video_path = os.path.join(input_folder, video_file)
        process_video(input_video_path, output_folder_path, model, video_file)

