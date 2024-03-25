import cv2
import mediapipe as mp
import numpy as np



def image_anal(video_path, target_video):

    # Mediapipe Hands 모듈 초기화
    mp_hands = mp.solutions.hands
    hands = mp_hands.Hands(static_image_mode=False, max_num_hands=2, min_detection_confidence=0.5)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_alt.xml")


    # 비디오 파일 경로
    video_path = f"{video_path}/{target_video}"
    print(video_path)
    # 비디오 캡처 객체 생성
    cap = cv2.VideoCapture(video_path)


    cap.set(cv2.CAP_PROP_FPS, cap.get(cv2.CAP_PROP_FPS) * 2)

    hand_mag = []
    i = 0

    ret, prev_frame = cap.read()
    prev_frame = cv2.cvtColor(prev_frame, cv2.COLOR_BGR2RGB)

    
    results = hands.process(prev_frame)

    # 감지된 손이 있을 경우
    if results.multi_hand_landmarks:
        # 감지된 각 손에 대해 처리
        for hand_landmarks in results.multi_hand_landmarks:
            x_min, y_min = prev_frame.shape[1], prev_frame.shape[0]
            x_max, y_max = 0, 0
            hand_landmark = [(lm.x, lm.y) for lm in hand_landmarks.landmark]
            # 손이 오른쪽에 있는지 왼쪽에 있는지 확인
            z_min = min(hand_landmark, key=lambda x: x[0])[0]
            for landmark in hand_landmarks.landmark:
                x, y = int(landmark.x * prev_frame.shape[1]), int(landmark.y * prev_frame.shape[0])
                if x < x_min:
                    x_min = x
                if x > x_max:
                    x_max = x
                if y < y_min:
                    y_min = y
                if y > y_max:
                    y_max = y
            prev_hand_image = prev_frame[y_min:y_max, x_min:x_max]

    else:
        prev_hand_image = []
    # 비디오 프레임 반복
    while cap.isOpened():

        # 비디오 프레임 읽기
        ret, frame = cap.read()
        if not ret:
            break

        video_inform2 = {
                'present_frame' : int(cap.get(cv2.CAP_PROP_POS_FRAMES)),
                'total_frame' : int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
            }

        # 프레임을 RGB로 변환
        curr_frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

        # 타임스탬프
        timestamp_ms = cap.get(cv2.CAP_PROP_POS_MSEC)
        timestamp_s = round(timestamp_ms/ 1000, 2)

        faces = face_cascade.detectMultiScale(curr_frame, 1.3, 5)

        # 손 감지
        results = hands.process(curr_frame)

        # 감지된 손이 있을 경우
        if len(faces) > 0 and results.multi_hand_landmarks:

            for (x, y, w, h) in faces:
                cv2.rectangle(curr_frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
            # 감지된 각 손에 대해 처리
            for hand_landmarks in results.multi_hand_landmarks:

                mp.solutions.drawing_utils.draw_landmarks(curr_frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

                x_min, y_min = curr_frame.shape[1], curr_frame.shape[0]
                x_max, y_max = 0, 0

                hand_landmark = [(lm.x, lm.y) for lm in hand_landmarks.landmark]

                for landmark in hand_landmarks.landmark:
                    x, y = int(landmark.x * curr_frame.shape[1]), int(landmark.y * curr_frame.shape[0])
                    if x < x_min:
                        x_min = x
                    if x > x_max:
                        x_max = x
                    if y < y_min:
                        y_min = y
                    if y > y_max:
                        y_max = y

                curr_hand_image = frame[y_min:y_max, x_min:x_max]
                if prev_hand_image is None or len(prev_hand_image) == 0:
                    prev_hand_image = curr_hand_image.copy()
                else:
                    motion_mag = extract_motion_mag(prev_hand_image, curr_hand_image)
                    hand_mag.append([timestamp_s, motion_mag])
                    prev_hand_image = curr_hand_image.copy()

                del curr_hand_image
        else:
            curr_hand_image = []
               
        cv2.imshow('Hand Tracking', curr_frame)
        # Exit when 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        i += 1
        if i%1000==0:
            print(video_inform2['present_frame'], video_inform2['total_frame'])

        if video_inform2['present_frame']  == video_inform2['total_frame']:
                break
    # 캡처 객체 해제
    cap.release()
    cv2.destroyAllWindows()

    # 모듈 종료
    hands.close()

    # 이미지 처리 후에 hand_image에 대한 메모리 해제


    return hand_mag


def extract_motion_mag(prev_frame, curr_frame):

    def frame_padding(prev_frame, curr_frame):

        # 이전 프레임과 현재 프레임의 크기 확인
        prev_height, prev_width = prev_frame.shape[:2]
        curr_height, curr_width = curr_frame.shape[:2]

        # 두 프레임의 크기를 맞추기 위한 최대 높이와 너비 계산
        max_height = max(prev_height, curr_height)
        max_width = max(prev_width, curr_width)

        # 패딩할 양 계산
        pad_height_prev = max_height - prev_height
        pad_width_prev = max_width - prev_width
        pad_height_curr = max_height - curr_height
        pad_width_curr = max_width - curr_width

        # 패딩 추가
        prev_frame_padded = cv2.copyMakeBorder(prev_frame, 0, pad_height_prev, 0, pad_width_prev, cv2.BORDER_CONSTANT, value=(0, 0, 0))
        curr_frame_padded = cv2.copyMakeBorder(curr_frame, 0, pad_height_curr, 0, pad_width_curr, cv2.BORDER_CONSTANT, value=(0, 0, 0))

        return prev_frame_padded, curr_frame_padded

    prev_frame, current_frame = frame_padding(prev_frame, curr_frame)
    if prev_frame is None or current_frame is None:
        return 0
    else:
        prev_frame = cv2.cvtColor(prev_frame, cv2.COLOR_BGR2GRAY)
        current_frame = cv2.cvtColor(current_frame, cv2.COLOR_BGR2GRAY)

        params = dict(pyr_scale=0.5, levels=3, winsize=15, iterations=3, poly_n=5, poly_sigma=1.2, flags=0)
        flow = cv2.calcOpticalFlowFarneback(prev_frame, current_frame, None, **params)

        # 모션 벡터의 크기 계산
        motion_magnitude = cv2.norm(flow, cv2.NORM_L2)    # 픽셀 단위

        return motion_magnitude
