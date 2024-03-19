import openai
import os

# GPT API Key 입력
os.environ["OPENAI_API_KEY"] = 'Key'
openai.api_key = os.getenv("OPENAI_API_KEY")

# 국어 평가 함수
def korean_evaluate_lecture(file_path):

    with open(file_path, 'r', encoding='utf-8') as file:
        lecture_content = file.read()
    
    # 프롬프트 엔지니어링 (GPT-4 사용)
    response = openai.ChatCompletion.create(
        model="gpt-4-turbo-preview",
        messages=[
            {"role": "system", 
             "content": """Task: Conduct a Rigorous Evaluation of Subtitles for an Online Korean Language Lecture Aimed at Middle School Students.
                Your objective is to critically assess the subtitles of the lecture across three essential dimensions: Clarity, Difficulty, and Sentence Mastery. Assign a score between 1 and 10 for each category, with 1 indicating very poor performance and 10 indicating excellence. Your evaluation must be critical and based on specific, concrete examples from the subtitles. Ensure strictness in scoring to maintain objectivity.
                Evaluation Criteria:
                Clarity
                Score: /10
                Evaluation: Seek out instances where the lecture fails to clearly convey its primary themes and essential messages. Critically evaluate the effectiveness of explanations, such as 'a is b', in making concept x understandable. Highlight any ambiguities or instances of poor explanation.
                Difficulty
                Score: /10
                Evaluation: Identify examples from the subtitles that suggest the material may not be adequately tailored to the comprehension level of middle school students. Critique the language used for its complexity or simplicity, and the examples for their lack of relatability or appropriateness, such as "The example 'e' fails to clearly illustrate the principle of f."
                Sentence Mastery
                Score: /10
                Evaluation: Point out examples where the subtitles demonstrate poorly constructed sentences that hinder smooth and coherent information delivery. An example could be, "The sentence 'h is i' is constructed in a way that confuses rather than aids understanding."
                Overall Score: /30
                Conclude with an aggregated total score from each category and provide a succinct summary of the lecture's content, emphasizing areas of weakness or concern.
                Your analysis should focus on identifying significant shortcomings to provide a clear and honest evaluation. Avoid leniency to ensure the assessment accurately reflects the quality of the subtitles in delivering an effective and understandable lecture to middle school students.
                You MUST answer in korean.
            """},
            {"role": "user", "content": f"Evaluate the following lecture content:\n\n{lecture_content}"}
        ]
    )
    
    # 결과 출력
    return response.choices[0].message['content']


# 국어 과목 불러와서 평가하면 결과가 나온다.
korean_best_1 = 'milkt text/korean_best_1.txt'
print(korean_evaluate_lecture(korean_best_1))

# 결과 예시
# 명확성
# 점수: 8/10

# 강의의 콘텐츠는 비교적 명확하게 주제와 개념을 전달하고 있습니다. 예를 들어, "시 속의 말하드니 목소리의 주인공"이라는 부분은 학생들이 시 속 화자의 개념을 이해하는 데 도움을 줍니다. 
# 하지만 "나라는 표현이 등장하지 않으면 직접 드러나지 않는다라고 보시면 됩니다."와 같은 부분에서는 조금 더 구체적인 설명이나 예시가 필요할 것 같습니다. 이론적 설명과 예시 사이에 균형을 맞추어 학생들의 이해를 도울 수 있었으면 합니다.

# 난이도
# 점수: 7/10

# 전반적인 강의 내용은 중학생들이 이해할 수 있는 난이도로 구성되어 있습니다. 
# 그러나 일부 용어와 개념, 예를 들어 "시적 화자", "서정적 자아"등은 중학생들에게 다소 어려울 수 있습니다. 
# 이 개념들은 핵심적이며 중요하지만, 좀 더 학생들의 수준에 맞게 설명하거나 일상적인 예시를 더 추가하여 설명한다면 더 좋을 것 같습니다.

# 문장 완성도
# 점수: 9/10

# 대체적으로 문장 구조가 잘 정리되어 있어 정보의 전달이 명확하고 이해하기 쉽습니다. 예를 들어, "시에 말하는 이의 특징을 선생님과 함께 정리해볼게요." 같은 문장은 명령형을 사용하여 강의의 흐름을 명확하게 안내합니다. 그러나 간혹 학생들의 경험이나 사전 지식을 가정하는 문장 사용은 정보의 전달을 어렵게 만들 수 있습니다. 전반적으로 문장 구성이 이해하기 쉽게 잘 되어 있으나, 일부 개념을 소개할 때 사용하는 문장은 좀 더 섬세한 설명이 필요할 수 있습니다.

# 전체 점수: 24/30

# 이 강의는 명확성, 난이도, 문장 완성도 측면에서 좋은 점수를 받았습니다. 
# 강의의 주제와 개념 전달이 비교적 명확하며, 문장 구조가 잘 정리되어 정보 전달에 효과적입니다. 
# 하지만, 일부 개념은 중학생들에게 다소 어렵게 느껴질 수 있으며, 이를 해소하기 위해 좀 더 구체적인 예시나 좀 더 쉬운 설명이 필요할 것 같습니다. 
# 강의 내용이 중학생들의 수준에 더 잘 맞도록 조정한다면 더욱 효과적인 학습이 가능할 것으로 보입니다.


# 수학 평가 함수
def math_evaluate_lecture(file_path):

    with open(file_path, 'r', encoding='utf-8') as file:
        lecture_content = file.read()
    
    # 프롬프트 엔지니어링 (GPT-4 사용)
    response = openai.ChatCompletion.create(
        model="gpt-4-turbo-preview",
        messages=[
            {"role": "system", 
             "content": """Task: Conduct a Rigorous Evaluation of Subtitles for an Online Math Lecture Aimed at Middle School Students.
                Your objective is to critically assess the subtitles of the lecture across three essential dimensions: Clarity, Difficulty, and Sentence Mastery. Assign a score between 1 and 10 for each category, with 1 indicating very poor performance and 10 indicating excellence. Your evaluation must be critical and based on specific, concrete examples from the subtitles. Ensure strictness in scoring to maintain objectivity.
                Evaluation Criteria:
                Clarity
                Score: /10
                Evaluation: Seek out instances where the lecture fails to clearly convey its primary themes and essential messages. Critically evaluate the effectiveness of explanations, such as 'a is b', in making concept x understandable. Highlight any ambiguities or instances of poor explanation.
                Difficulty
                Score: /10
                Evaluation: Identify examples from the subtitles that suggest the material may not be adequately tailored to the comprehension level of middle school students. Critique the language used for its complexity or simplicity, and the examples for their lack of relatability or appropriateness, such as "The example 'e' fails to clearly illustrate the principle of f."
                Sentence Mastery
                Score: /10
                Evaluation: Point out examples where the subtitles demonstrate poorly constructed sentences that hinder smooth and coherent information delivery. An example could be, "The sentence 'h is i' is constructed in a way that confuses rather than aids understanding."
                Overall Score: /30
                Conclude with an aggregated total score from each category and provide a succinct summary of the lecture's content, emphasizing areas of weakness or concern.
                Your analysis should focus on identifying significant shortcomings to provide a clear and honest evaluation. Avoid leniency to ensure the assessment accurately reflects the quality of the subtitles in delivering an effective and understandable lecture to middle school students.
                You MUST answer in korean.
            """},
            {"role": "user", "content": f"Evaluate the following lecture content:\n\n{lecture_content}"}
        ]
    )
    
    # 결과 출력
    return response.choices[0].message['content']

# 수학 과목 불러와서 평가하면 결과가 나온다.
math_worst_1 = 'milkt text/math_worst_1.txt'
print(math_evaluate_lecture(math_worst_1))



# 영어 평가 함수
def english_evaluate_lecture(file_path):

    with open(file_path, 'r', encoding='utf-8') as file:
        lecture_content = file.read()
    
    # 프롬프트 엔지니어링 (GPT-4 사용)
    response = openai.ChatCompletion.create(
        model="gpt-4-turbo-preview",
        messages=[
            {"role": "system", 
             "content": """Task: Conduct a Rigorous Evaluation of Subtitles for an Online English Language Lecture Aimed at Middle School Students.
                Your objective is to critically assess the subtitles of the lecture across three essential dimensions: Clarity, Difficulty, and Sentence Mastery. Assign a score between 1 and 10 for each category, with 1 indicating very poor performance and 10 indicating excellence. Your evaluation must be critical and based on specific, concrete examples from the subtitles. Ensure strictness in scoring to maintain objectivity.
                Evaluation Criteria:
                Clarity
                Score: /10
                Evaluation: Seek out instances where the lecture fails to clearly convey its primary themes and essential messages. Critically evaluate the effectiveness of explanations, such as 'a is b', in making concept x understandable. Highlight any ambiguities or instances of poor explanation.
                Difficulty
                Score: /10
                Evaluation: Identify examples from the subtitles that suggest the material may not be adequately tailored to the comprehension level of middle school students. Critique the language used for its complexity or simplicity, and the examples for their lack of relatability or appropriateness, such as "The example 'e' fails to clearly illustrate the principle of f."
                Sentence Mastery
                Score: /10
                Evaluation: Point out examples where the subtitles demonstrate poorly constructed sentences that hinder smooth and coherent information delivery. An example could be, "The sentence 'h is i' is constructed in a way that confuses rather than aids understanding."
                Overall Score: /30
                Conclude with an aggregated total score from each category and provide a succinct summary of the lecture's content, emphasizing areas of weakness or concern.
                Your analysis should focus on identifying significant shortcomings to provide a clear and honest evaluation. Avoid leniency to ensure the assessment accurately reflects the quality of the subtitles in delivering an effective and understandable lecture to middle school students.
                You MUST answer in korean.
            """},
            {"role": "user", "content": f"Evaluate the following lecture content:\n\n{lecture_content}"}
        ]
    )
    
    # 결과 출력
    return response.choices[0].message['content']

# 영어 과목 불러와서 평가하면 결과가 나온다.
english_best_1 = 'milkt text/english_best_1.txt'
print(math_evaluate_lecture(english_best_1))
