import os
import pandas as pd
from settings import subject, load_path, save_path, PATH
from image_preprocess import image_anal


mean_list = []
motion_vector_list = []

os.chdir(PATH)
os.makedirs(f"{save_path}")

for sub in subject:
    os.makedirs(f"{save_path}\\{sub}")

    video_path = f"{load_path}\\image\\{sub}"
    video_list = os.listdir(video_path)

    if video_list == []:
        continue

    for video in video_list:
        print(video)
        mag_list = image_anal(video_path, video)
        
        video = video.replace(".mp4","")
        df_l = pd.DataFrame(mag_list, columns=["time", "motion magnitude"])
        df_l.to_csv(f"{save_path}\\{sub}\\{video}.csv")
        
   

