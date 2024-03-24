# 오디오 데이터처리
import librosa
import IPython.display as ipd
    
def sound_anal(audio_path):

    y, sr = librosa.load(audio_path, sr=16000)

    # 오디오 확인
    ipd.Audio(audio_path)

    def get_pitch(y, train=True):
        
        pitch = librosa.yin(y, fmin=librosa.note_to_hz('C2'), fmax=8000)
        
        return pitch

    pitch = get_pitch(y, train=True)

    return pitch

