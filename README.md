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

 내용

</details>

<details>
<summary><b>제스처 분석</b></summary>

제스처 분석은 강사가 설명을 강조 할 때 손동작 제스처를 얼마나 활용하며 설명을 진행하는지 비교하는 분석이며 각 강의 데이터 속 강사의 제스처 모션 유동량을 추출해 계산을 진행 하였다. 모션 유동량은 OpenCV를 통해 프레임 별로 이미지를 로드한 뒤, 구글에서 개발한 핸드 트랙킹 모델인 Mediapipe를 이용하여 핸드 모션의 랜드마크를 추출하였고, 추출한 랜드마크를 데이터를 이용해 OpenCV에 내장된 calcOpticalFlowFarneback 함수를 사용하여 모션 유동량을 계산하였다. 계산한 값들을 데이터 프레임으로 변환한 뒤 Sklearn의 IsolationForest 함수를 사용하여 모션 유동량 데이터의 이상치 값들을 추출하였다. 이때 이상치로 분류된 값들을 강사의 강조 모션량이라 지정하였다.

</details>

---

### **🕵️ 음성 분석**

<details>
<summary><b>초 당 음절 수 분석</b></summary>

 내용

</details>

<details>
<summary><b>피치 분석</b></summary>

피치 분석은 강사가 강의를 진행할 때 목소리 톤의 차이를 비교하는 분석이며 강의 영상의 음성 데이터를 Librosa 패키지에 내장된 Yib 함수를 사용하여 주파수 단위로 데이터를 추출한 뒤 강사의 평균 음역대를 비교하였다. 음역대 기준을 성인 여성 기본 주파수인 150~250Hz로 범위를 설정하였고 남성 강사의 강의자료인 경우는 그에 맞는 가중치(x1.5배)를 적용하여 계산을 진행하였다.

</details>

---

### **🕵️ 텍스트 분석**

<details>
<summary><b>프롬프트 엔지니어링</b></summary>

 내용

</details>

<details>
<summary><b>어휘 난이도 분석</b></summary>
 내용

</details>

<details>
<summary><b>형태소 분석</b></summary>

 내용

</details>

<details>
<summary><b>구문 패턴 분석</b></summary>
 
 내용

</details>

---

### **☑️ 결론**

**강사 측면**

- 밀크티 베스트 강의는 연구 결과의 긍정적 기준과 일치하므로 현재 수준을 유지한다.

- 밀크티 워스트 강의는 연구 결과 대비 얼굴 표정과 말하기 속도, 목소리 통을 개선하여 품질 향상을 시켜야한다.


**기업 측면**

- 시각적 효과와 전자칠판 활용의 장점을 적극적으로 홍보한다.

- 프롬프트 엔지니어링 도입으로 강의 품질을 빠르게 파악하고 효율성을 극대화 할 수 있다.
