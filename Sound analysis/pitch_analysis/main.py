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

        
        man_list = []  ## 남자 강사 강의리스트

        if audios.replace('.mp3', '') in man_list:
            print(audios)
            df['sound pitches'] = df['sound pitches'].mul(1.5)
            
        df["sound pitches"] = df["sound pitches"][df["sound pitches"] != 2205.0]    ## 무음 또는 소리인식이 안됬을때 값 제거
        df["sound pitches"] = df["sound pitches"][df["sound pitches"] != 11025.0]    

        df = df.dropna()

        audios2 = audios.replace(".mp3", "")
        
        df.to_csv(f"{save_path}\\{sub}\\{audios2}.csv", index = None)


        