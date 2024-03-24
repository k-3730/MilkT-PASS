from langchain.document_loaders import PyPDFLoader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores.elastic_vector_search import ElasticVectorSearch
from langchain.vectorstores import Chroma
from langchain.chat_models import ChatOpenAI
import openai
import pandas as pd
from langchain.chains import RetrievalQAWithSourcesChain
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)

# OpenAI API 키를 변수에 저장
openai_api_key = 'openai_api_key'

# 텍스트 분할
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
texts = text_splitter.split_documents(documents)

# 텍스트 임베딩 및 Chroma(DB) 저장
embeddings = OpenAIEmbeddings(openai_api_key=openai.api_key)

# 여기에서 embeddings_model 대신 embedding을 사용합니다.
vector_store = Chroma.from_documents(documents=texts, embedding=embeddings)
retriever = vector_store.as_retriever(search_kwargs={"k": 2})

# 여러 CSV 파일이 저장된 폴더의 경로
csv_folder_path = 'csv_folder_path'

# 결과를 저장할 폴더의 경로
output_folder_path = 'output_folder_path'

# CSV 파일 순회
for csv_file in os.listdir(csv_folder_path):
    if csv_file.endswith('.csv'):
        print(f"Processing file: {csv_file}")
        # 질문 로드
        df = pd.read_csv(os.path.join(csv_folder_path, csv_file))

        # PDF 문서 로드 및 텍스트로 변환
        pdf_loader = PyPDFLoader(file_path="등급_요약_merged(1).pdf")
        document_text = pdf_loader.load()

        # 텍스트 분할
        text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
        texts = text_splitter.split_documents(documents)

        # 텍스트 임베딩 및 Chroma(DB) 저장
        embeddings = OpenAIEmbeddings(openai_api_key=openai.api_key)
        vector_store = Chroma.from_documents(documents=texts, embedding=embeddings)
        retriever = vector_store.as_retriever(search_kwargs={"k": 2})


        # llm 객체 및 프롬프트 설정, 질문 처리 및 답변 생성 로직
        llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0, openai_api_key=openai_api_key)
        
       
        summaries = """This is an article that defines the difficulty level of words on a 
        scale of 1 to 6. Use it as a guide to judge the level of words for yourself."""
        
        system_template = """
        You are an expert in assessing the difficulty of Korean words.
        You need to predict the difficulty level of every word based on the content of the document.
        You can only mark a word as 'unrated' if it cannot be rated because it is a name or proper noun.
        {summaries}
        
        Example:
        - '짠'은 몇 등급이 될 수 있을 것 같나요? -> "1급"
        - '발광'은 몇 등급이 될 수 있을 것 같나요? -> "4급"
        - '는지'은 몇 등급이 될 수 있을 것 같나요? -> "4급"
        - '김미미누'은 몇 등급이 될 수 있을 것 같나요? -> "등급없음"
        
        Please indicate the grade only.
        You MUST answer in Korean:
        """
        
        messages = [
            SystemMessagePromptTemplate.from_template(system_template),
            HumanMessagePromptTemplate.from_template("{question}")
        ]

        prompt = ChatPromptTemplate.from_messages(messages)

        chain_type_kwargs = {"prompt": prompt}

        chain = RetrievalQAWithSourcesChain.from_chain_type(
            llm=llm,
            chain_type="stuff",
            retriever = retriever,
            return_source_documents=True,
            chain_type_kwargs=chain_type_kwargs
        )

        # 질문 처리 및 답변 생성
        answers = []
        for question in df['Question'].tolist():
            result = chain({"question": question})
            answers.append(result['answer'])

        # 답변을 DataFrame에 추가
        df['Answer'] = answers

        # 결과를 CSV 파일로 저장
        output_path = os.path.join(output_folder_path, f'GPT_{csv_file}')
        df.to_csv(output_path, index=False)

        print(f"답변이 포함된 파일이 저장되었습니다: {output_path}")
