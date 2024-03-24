from transformers import WhisperProcessor, WhisperForConditionalGeneration, RobertaTokenizerFast, RobertaForSequenceClassification, TextClassificationPipeline
import torch
import json
import os
from pydub import AudioSegment
from pydub.silence import detect_nonsilent
import whisper
from transformers import RobertaTokenizerFast, RobertaForSequenceClassification, TextClassificationPipeline


# whisper 모델 설정
model_whisper = whisper.load_model("large")

# 의도 분류 모델 및 파이프라인 설정
tokenizer = RobertaTokenizerFast.from_pretrained("gg4ever/intent-classification-korean")
model_intent_classification = RobertaForSequenceClassification.from_pretrained("gg4ever/intent-classification-korean")
text_classifier = TextClassificationPipeline(tokenizer=tokenizer, model=model_intent_classification, return_all_scores=True)


def analyze_audio(file_path):
    print(f"Analyzing {os.path.basename(file_path)}...")

    # Whisper로 음성을 텍스트로 변환
    result = model_whisper.transcribe(file_path, verbose=True)
    segments = result["segments"]

    # PyDub으로 비침묵 시간 계산
    audio = AudioSegment.from_mp3(file_path)
    non_silence_chunks = detect_nonsilent(audio, min_silence_len=1000, silence_thresh=-40)

    json_data = []
    prev_end = 0  # 이전 세그먼트의 끝 시간 초기화
    for i, segment in enumerate(segments):
        start, end = segment['start'], segment['end']
        text = segment['text']
        duration = end - start
        syllables = sum(1 for char in text if char.isalnum())
        syllables_per_second = syllables / duration if duration > 0 else 0

        silence_duration_before = (start - prev_end) if i > 0 else 0
        prev_end = end

        # 의도 분류
        intent_result = text_classifier(text)[0]
        top_intent = max(intent_result, key=lambda x: x['score'])
        intention = top_intent['label']
        intention_score = top_intent['score']

        json_data.append({
            "word": text,
            "start": start,
            "end": end,
            "duration": duration,
            "syllables_per_second": syllables_per_second,
            "silence_duration_before": silence_duration_before,
            "intention": intention,
            "intention_score": intention_score
        })

    return json_data


def save_json(data, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

# 폴더 경로 설정
source_folder = "source_folder"
destination_folder = "destination_folder"

# 폴더 내의 모든 오디오 파일에 대해 분석 실행
for file in os.listdir(source_folder):
    if file.endswith(".mp3"):
        file_path = os.path.join(source_folder, file)
        analysis_result = analyze_audio(file_path)  # 오디오 파일 분석
        json_filename = os.path.join(destination_folder, file.replace(".mp3", ".json"))
        save_json(analysis_result, json_filename)  # 분석 결과를 JSON 파일로 저장
        print(f"V2_Saved analysis for {file}")
