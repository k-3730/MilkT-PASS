import pandas as pd
import os
from konlpy.tag import Okt
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from collections import Counter

# 폰트 지정
font_path = 'JALNANGOTHICTTF.TTF'
font_prop = fm.FontProperties(fname=font_path, size=12)
plt.rc('font', family=font_prop.get_name())

okt = Okt()

# 형태소 갯 수 -> 엑셀 파일 저장
directory = r'milkt text/'
txt_files = [os.path.join(directory, f) for f in os.listdir(directory) if f.endswith('.txt')]

for file_path in txt_files:
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
        
    pos_tags = okt.pos(text)
    pos_counts = Counter(tag for word, tag in pos_tags)

    # 데이터 프레임 변환
    df = pd.DataFrame(pos_counts.items(), columns=['품사', '빈도'])
    
    # 원본 파일 이름 + 엑셀 이름 추가 저장
    base_name = os.path.basename(file_path)  # 원본 파일 이름 가져오기
    name_without_ext = os.path.splitext(base_name)[0]  # 확장자 제거
    excel_filename = f"{name_without_ext}_pos_counts.xlsx"  # 파일 이름 생성
    excel_path = os.path.join(directory, excel_filename)  # 저장 경로

    # Excel 파일로 저장
    df.to_excel(excel_path, index=False)


# Okt 형태소 한글 변환
pos_korean = {
    'Adjective': '형용사',
    'Adverb': '부사',
    'Alpha': '알파벳',
    'Conjunction': '접속사',
    'Determiner': '관형사',
    'Eomi': '어미',
    'Exclamation': '감탄사',
    'Foreign': '외국어, 한자 및 기타기호',
    'Hashtag': '트위터 해쉬태그',
    'Josa': '조사',
    'KoreanParticle': '한국어 의존 명사',
    'Noun': '명사',
    'Number': '숫자',
    'PreEomi': '선어말어미',
    'Punctuation': '구두점',
    'ScreenName': '트위터 아이디',
    'Suffix': '접미사',
    'Unknown': '미등록어',
    'Verb': '동사',
    'Modifier':'수식어',
    'VerbPrefix' : '동사 접두사'
}

# 엑셀 파일 불러오기
milkt_korean_best = ["milkt text/korean_best_1_pos_counts.xlsx",
                     "milkt text/korean_best_2_pos_counts.xlsx",
                     "milkt text/korean_best_3_pos_counts.xlsx",
                     "milkt text/korean_best_4_pos_counts.xlsx",
                     "milkt text/korean_best_5_pos_counts.xlsx",
        ]

# 엑셀 파일 통합
milkt_korean_best_excel = []
for file in milkt_korean_best:
    df = pd.read_excel(file)
    milkt_korean_best_excel.append(df)
    
# 정규화 값 -> 비율 컬럼 추가
korean_normalized_all = []
for df in milkt_korean_best_excel:
    total_word = df['빈도'].sum()
    normalized_df = df.copy()
    normalized_df['비율'] = df['빈도'] / total_word
    korean_normalized_all.append(normalized_df)
    
# 정규화 데이터 합치기 및 빈도 컬럼 삭제
korean_final = pd.concat(korean_normalized_all, ignore_index=True)
korean_final= korean_final.drop(columns=['빈도'])


# 품사 별 비율 평균 계산, 데이터 프레임 변환
milkt_korean_best_df = korean_final.groupby('품사')['비율'].mean()
milkt_korean_best_df = pd.DataFrame(list(milkt_korean_best_df.items()), columns=['품사', '비율'])

# 품사 한글화
milkt_korean_best_df['품사'] = milkt_korean_best_df['품사'].map(pos_korean)

# 데이터 시각화
plt.figure(figsize=(10, 8))
barplot = sns.barplot(x='비율', y='품사', data=milkt_korean_best_df.sort_values('비율', ascending=False), palette='viridis')
plt.title('품사 비율', fontproperties = font_prop)
plt.xticks(fontproperties = font_prop)
plt.yticks(fontproperties = font_prop)
plt.xlabel('비율',fontproperties = font_prop)
plt.ylabel('품사', fontproperties = font_prop)

# 숫자 추가
for p in barplot.patches:
    width = p.get_width()
    plt.text(p.get_width(), p.get_y() + p.get_height() / 2., f'{width:.2%}', va='center')


plt.tight_layout()
plt.show()

# 나머지도 파일만 바꾼 후 동일한 코드로 진행한다.


# 형용사, 부사 분석

# 경로 설정
file_path = r'english_best_1.txt'

# 파일 읽기
with open(file_path, 'r', encoding='utf-8') as file:
    text = file.read()

# 형태소 분석 및 품사 태깅
pos_tags = okt.pos(text)

# 형용사 부사 필터링
adjectives_adverbs = [word for word, tag in pos_tags if tag in ('Adjective', 'Adverb')]

# 빈도 수 계산
word_counts = Counter(adjectives_adverbs)

# 가장 많이 사용된 형용사와 부사를 출력한다
most_common_words = word_counts.most_common()  # 상위 N개 단어를 보고 싶다면, most_common(N)으로 호출한다
for word, count in most_common_words:
    print(f"{word}: {count}")
