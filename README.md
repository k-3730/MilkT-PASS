# 📈 MilkT PASS

![K-001](https://github.com/k-3730/MilkT-PASS/assets/45035923/9cec0587-9afb-43b4-953f-d44aa68787d2)

### **🗞️ 프로젝트 소개**
🕛 개발 기간 : 2024.02.05 ~ 2024.03.25
<br>

이 프로젝트는 천재교육이 서비스하는 밀크티 중등의 강의 품질 향상을 위해서 강의 평가 시스템을 설계하여 
강의 품질을 객관적으로 평가하고 밀크티 중등의 경쟁력 강화 방안을 모색한다.


<br>

## **🧑‍🤝‍🧑 천재교육 빅데이터 5기 '데이터 스쿼드' 팀 구성 및 역할**

<div align="center">
 
| **권홍준** | **김하리** | **신다인** | **최태영** |
| :------: |  :------: | :------: | :------: |
| [<img src="https://github.com/k-3730.png" height=150 width=150> <br/> @k-3730](https://github.com/k-3730) | [<img src="https://github.com/hariqueen.png" height=150 width=150> <br/> @hariqueen](https://github.com/hariqueen) | [<img src="https://github.com/daini0i.png" height=150 width=150> <br/> @daini0i](https://github.com/daini0i) | [<img src="https://github.com/surplus96.png" height=150 width=150> <br/> @surplus96](https://github.com/surplus96) |

</div>

### 🐻‍❄️ 권홍준
- **얼굴 감정분석 / 프롬프트 엔지니어링 / 형태소 분석**

### 🐶 김하리
 - **초 당 음절 수 분석 / 어휘 난이도 분석 / 구문 패턴 분석**

### 🐱 신다인
- **객체 인식 분석**

### 🐭 최태영
- **제스처 분석 / 피치 분석**

---

### **🛠 개발 환경**
**✔️ 언어 및 라이브러리**

<img alt="Python" src ="https://img.shields.io/badge/Python-3776AB.svg?&style=for-the-badge&logo=Python&logoColor=white"/> 

<img src="https://img.shields.io/badge/numpy-013243?style=for-the-badge&logo=numpy&logoColor=white"> <img src="https://img.shields.io/badge/pandas-15048?style=for-the-badge&logo=pandas&logoColor=white"> <img src="https://img.shields.io/badge/pytorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white"> <img alt="OpenCV" src ="https://img.shields.io/badge/OpenCV-5C3EE8.svg?&style=for-the-badge&logo=OpenCV&logoColor=white"/> <img alt="OpenAI" src ="https://img.shields.io/badge/OpenAI-412991.svg?&style=for-the-badge&logo=OpenAI&logoColor=white"/> <img src="https://img.shields.io/badge/ffmpeg-007808?style=for-the-badge&logo=ffmpeg&logoColor=white"> <img src="https://img.shields.io/badge/scikitlearn-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white">

<br>

**✔️ 통합 개발환경 (IDE)**

<img src="https://img.shields.io/badge/visualstudiocode-007ACC?style=for-the-badge&logo=visualstudiocode&logoColor=white"> <img alt="Jupyter" src ="https://img.shields.io/badge/Jupyter-F37626.svg?&style=for-the-badge&logo=Jupyter&logoColor=white"/> <img src="https://img.shields.io/badge/googlecolab-F9AB00?style=for-the-badge&logo=googlecolab&logoColor=white"> 

<br>

**✔️ 버전 관리 및 협업**

<img src="https://img.shields.io/badge/github-181717?style=for-the-badge&logo=github&logoColor=white"> <img src="https://img.shields.io/badge/notion-000000?style=for-the-badge&logo=notion&logoColor=white"> <img src="https://img.shields.io/badge/slack-4A154B?style=for-the-badge&logo=slack&logoColor=white">


---
### **🕵️ 이미지 분석**

<details>
<summary><b>얼굴 감정분석</b></summary>

[모델](https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&aihubDataSe=data&dataSetSn=82)

Ai-hub에서 한국인 감정 인식을 위한 모델로 상기 링크에서 이용할 수 있다.
해당 모델은 7가지의 감정 기쁨, 당황, 분노, 불안, 상처, 슬픔, 중립으로 구성되어 있으며 각 감정 당 약 7만건의 한국인 데이터로만 학습되었다.
강의 영상(MP4)에 대해서 실시간으로 감정을 인식하게 하여 분석하였으며 모델이 해당 감정이 95% 이상일 때만 감정을 인식하게 하였다.
또 한 단순 감정 빈도수가 아닌 감정의 변화 횟수를 측정하고 영상의 길이를 고려하여 정규화하여 진행하였다.

</details>

<details>
<summary><b>객체 인식 분석</b></summary>

객체 감지 및 분석은 인터넷 강의에서 사용되는 시각 자료를 식별하고 그 출현 빈도를 비교하는 데 활용되었습니다. 이를 위해 YOLOv9 모델을 기본으로 사용했으며, 한국형 인터넷 강의에 대한 이미지 데이터셋을 학습시키기 위해 이미지 라벨링 작업이 수행되었습니다. 전체 라벨은 총 10가지로 구성되어 있으며, 학습된 모델의 성능은 각 라벨별로 다음과 같이 평가되었습니다.
학습된 모델을 통해 추론하고자 하는 영상을 열어 1초당 프레임을 캡처하여 이미지 내 객체를 감지하는 작업을 진행했습니다. 동시에 이미지에서 감지된 객체를 클래스명과 개수로 기록하여 이를 JSON 파일로 저장했습니다. 이를 통해 감지된 객체의 분포를 시각화할 수 있었습니다.

![image](https://github.com/k-3730/MilkT-PASS/assets/45035923/f3c88df6-8764-49f5-8d33-5358a3c19170) ![image (1)](https://github.com/k-3730/MilkT-PASS/assets/45035923/0e7907ed-ef7e-426d-83a6-1d50dc88e383)

</details>

<details>
<summary><b>제스처 분석</b></summary>

제스처 분석은 강사가 설명을 강조 할 때 손동작 제스처를 얼마나 활용하며 설명을 진행하는지 비교하는 분석이며 각 강의 데이터 속 강사의 제스처 모션 유동량을 추출해 계산을 진행 하였다. 모션 유동량은 OpenCV를 통해 프레임 별로 이미지를 로드한 뒤, 구글에서 개발한 핸드 트랙킹 모델인 Mediapipe를 이용하여 핸드 모션의 랜드마크를 추출하였고, 추출한 랜드마크를 데이터를 이용해 OpenCV에 내장된 calcOpticalFlowFarneback 함수를 사용하여 모션 유동량을 계산하였다. 계산한 값들을 데이터 프레임으로 변환한 뒤 Sklearn의 IsolationForest 함수를 사용하여 모션 유동량 데이터의 이상치 값들을 추출하였다. 이때 이상치로 분류된 값들을 강사의 강조 모션량이라 지정하였다

</details>

---

### **🕵️ 음성 분석**

<details>
<summary><b>초 당 음절 수 분석</b></summary>

 내용

</details>

<details>
<summary><b>피치 분석</b></summary>

피치 분석은 강사가 강의를 진행할 때 목소리 톤의 차이를 비교하는 분석이며 강의 영상의 음성 데이터를 Librosa 패키지에 내장된 Yin 함수를 사용하여 주파수 단위로 데이터를 추출한 뒤 강사의 평균 음역대를 비교하였다. 음역대 기준을 성인 여성 기본 주파수인 150~250Hz로 범위를 설정하였고 남성 강사의 강의자료인 경우는 그에 맞는 가중치(x1.5배)를 적용하여 계산을 진행하였다.

</details>

---

### **🕵️ 텍스트 분석**

<details>
<summary><b>프롬프트 엔지니어링</b></summary>

GPT-4 API를 활용하여 강의 자막을 주고 각 항목에 맞게 평가를 해서 점수를 메겨달라고 요청하였다.
프롬프트 전문은 One-shot prompt engineering.py에서 확인 가능하며 프롬프트를 간략하게 요약하자면 아래와 같다.
객관적인 평가를 위해 엄격하게 평가를 요청했으며, 각 항목마다 1점부터 10점까지 점수를 부여하게 하였다.

- 명확성 : 중학생 대상의 강의로서 설명이 자세하고 명확하게 표현되는지를 평가해달라고 하였다.
- 난이도 : 중학생 대상의 강의로서 내용을 어렵게 설명하거나 어려운 예시를 들지 않는지 평가해달라고 하였다.
- 문장 완성도 : 강사들의 문장 구성이 혼란을 주지 않는지 평가해달라고 하였다.

상기 항목들을 바탕으로 총 점 30점 만점에 최종 점수를 요청하였으며 GPT-4가 정확히 강의 내용을 이해하고 있는지 파악하기 위해 무슨 강의를 말하고 있는지도 설명해달라고
요청하였다.

</details>

<details>
<summary><b>어휘 난이도 분석</b></summary>
 내용

</details>

<details>
<summary><b>형태소 분석</b></summary>

 각 강의에 대해 형태소 비율의 차이를 비교하기 위해서 형태소 분석기 Okt를 사용하여 품사를 태깅하고 비율을 시각화 하였다.
 Okt는 트위터 형태소 분석기로 구어체와 신조어에 강점을 띄어 강의 자막을 잘 분류할 것이라고 판단하여 사용하였다.
 
 Okt 품사의 종류로는 [해당 링크](https://datascienceschool.net/03%20machine%20learning/03.01.02%20KoNLPy%20%ED%95%9C%EA%B5%AD%EC%96%B4%20%EC%B2%98%EB%A6%AC%20%ED%8C%A8%ED%82%A4%EC%A7%80.html)를 통하여 확인 가능하다.

</details>

<details>
<summary><b>구문 패턴 분석</b></summary>
 
 내용

</details>

---

### **☑️ 결론**

**강사 측면**

- 밀크티 베스트 강의는 연구 결과의 긍정적 기준과 일치하므로 현재 수준을 유지한다.

- 밀크티 워스트 강의는 연구 결과 대비 얼굴 표정과 말하기 속도, 목소리 톤을 개선하여 품질 향상을 시켜야한다.


**기업 측면**

- 시각적 효과와 전자칠판 활용의 장점을 적극적으로 홍보한다.

- 프롬프트 엔지니어링 도입으로 강의 품질을 빠르게 파악하고 효율성을 극대화 할 수 있다.
