from settings import subject, load_path, save_path, PATH
import os
import pandas as pd
from sound_preprocess import sound_anal
import librosa
import IPython.display as ipd
import numpy as np


os.chdir(PATH)
os.makedirs(f"{save_path}")


for sub in subject:
    os.makedirs(f"{save_path}\\{sub}")
    audio_path  = f"{load_path}\\sound\\{sub}"
    audio_list = os.listdir(audio_path)
    for audios in audio_list:
        sr = 16000
        fmax = sr / 2
        # 음성을 프레임으로 나누기
        frame_size = 1024
        hop_length = 160
        print(audios)
        audio = os.path.join(audio_path, audios)
        pitches = sound_anal(audio)
        frame_time = librosa.frames_to_time(range(len(pitches)), sr=sr)
        # 음성 데이터 불러오기
        pitches_list = []
        
        for i, (frame_pitches, time_stamp) in enumerate(zip(pitches, frame_time)):
            pitches_list.append([time_stamp, frame_pitches])
        df = pd.DataFrame(pitches_list, columns=["time", "sound pitches"])

        
        man_list = ["EBS L1. 가장 쉽게 배우는 단어 ＆ 숙어","EBS L1. 심쿵 단어",'EBS 영어 마을의 8 친구들： 8품사','EBSbe동사 보는 용어로 Start!','EBS품사','EBS문법_음성_음운(자음과_모음)','ebs-중등국어-시의목소리','ebs-중학국어-비유표현','[EBS] 소수의 분류',
    '[EBS] 소인수분해를 이용하여 약수와 약수의 개수 구하기']  ## 남자 강사 강의리스트

        if audios.replace('.mp3', '') in man_list:
            print(audios)
            df['sound pitches'] = df['sound pitches'].mul(1.1)
            
        df["sound pitches"] = df["sound pitches"][df["sound pitches"] != 2205.0]    ## 무음 또는 소리인식이 안됬을때 값 제거
        df["sound pitches"] = df["sound pitches"][df["sound pitches"] != 11025.0]    

        df = df.dropna()

        # 델타값(변화량) 계산
        df['delta_pitch'] = abs(df['sound pitches'].diff())
        y = df["delta_pitch"][df['delta_pitch'] > 300]
        audios2 = audios.replace(".mp3", "")
        
        df.to_csv(f"{save_path}\\{sub}\\{audios2}.csv", index = None)


        