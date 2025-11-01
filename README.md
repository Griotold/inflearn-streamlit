# 💰 소득세 챗봇 (Tax Chatbot with RAG)

> LangChain과 RAG를 활용한 소득세 질의응답 시스템

[스크린샷 1: 메인 화면]

## 📌 프로젝트 소개

소득세 관련 문서를 벡터 DB에 임베딩하여, 사용자의 질문에 대해 관련 문서를 검색하고 LLM이 답변을 생성하는 RAG 기반 챗봇입니다.

**개발 기간**: 2025.10 (위니브 AI Chatbot & RAG 기반 서비스 개발자 양성 과정)

## ✨ 주요 기능

- 📚 **문서 임베딩**: 소득세 관련 문서를 벡터화하여 Pinecone에 저장
- 🔍 **시맨틱 검색**: 사용자 질문과 유사한 문서 자동 검색
- 🤖 **RAG 기반 응답**: 검색된 문서를 컨텍스트로 활용하여 정확한 답변 생성
- 💬 **대화형 UI**: Streamlit으로 구현한 직관적인 웹 인터페이스

[스크린샷 2: 질의응답 예시]

## 🛠 기술 스택

### AI/ML
- **LangChain**: RAG 파이프라인 구축
- **OpenAI API**: 임베딩 및 LLM 응답 생성
- **Pinecone**: 벡터 데이터베이스

### Backend & UI
- **Python 3.x**
- **Streamlit**: 웹 인터페이스

## 🏗 시스템 아키텍처

```
[사용자 질문]
    ↓
[임베딩 변환]
    ↓
[Pinecone 유사도 검색]
    ↓
[관련 문서 추출]
    ↓
[LLM에 컨텍스트 전달]
    ↓
[답변 생성 및 출력]
```

[다이어그램 이미지 자리]

## 🚀 설치 및 실행

### 1. 환경 설정

```bash
# 저장소 클론
git clone https://github.com/Griotold/inflearn-streamlit.git
cd inflearn-streamlit

# 가상환경 생성 및 활성화
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 패키지 설치
pip install -r requirements.txt
```

### 2. 환경 변수 설정

`.env` 파일 생성:
```
OPENAI_API_KEY=your_openai_api_key
PINECONE_API_KEY=your_pinecone_api_key
PINECONE_ENVIRONMENT=your_pinecone_environment
```

### 3. 실행

```bash
streamlit run app.py
```

## 📖 사용 방법

1. 애플리케이션 실행 후 브라우저에서 `localhost:8501` 접속
2. 채팅 입력창에 소득세 관련 질문 입력
3. AI가 관련 문서를 검색하여 답변 생성

[사용 예시 GIF 자리]

## 💡 핵심 학습 내용

### RAG (Retrieval-Augmented Generation)
- 외부 문서를 임베딩하여 벡터 DB에 저장
- 사용자 질문과 유사한 문서를 검색
- 검색된 문서를 LLM의 컨텍스트로 활용하여 답변 생성

### LangChain 활용
- `VectorStoreRetriever`를 통한 문서 검색
- `ConversationalRetrievalChain`으로 대화형 RAG 구현
- 프롬프트 템플릿 커스터마이징

### 벡터 데이터베이스
- Pinecone을 사용한 고속 유사도 검색
- 임베딩 차원 최적화 및 인덱스 관리

## 🔧 주요 코드

### 문서 임베딩 및 저장
```python
# [코드 예시 자리]
```

### RAG 체인 구성
```python
# [코드 예시 자리]
```

## 📊 성능 및 결과

- **검색 정확도**: [데이터 있으면 추가]
- **응답 속도**: [데이터 있으면 추가]
- **사용자 만족도**: [데이터 있으면 추가]

## 🔮 향후 개선 사항

- [ ] 더 많은 세금 관련 문서 추가 (근로소득세, 종합소득세, 양도소득세 등)
- [ ] 대화 히스토리 저장 기능
- [ ] 출처 문서 하이라이팅 기능
- [ ] 다국어 지원
- [ ] 질문 추천 기능

## 📝 프로젝트 구조

```
inflearn-streamlit/
├── app.py                 # Streamlit 메인 앱
├── embedding.py           # 문서 임베딩 로직
├── rag_chain.py          # RAG 체인 구성
├── data/                 # 소득세 관련 문서
├── requirements.txt      # 패키지 의존성
└── .env.example         # 환경 변수 예시
```

## 👤 개발자

**조해성**
- GitHub: [@Griotold](https://github.com/Griotold)
- Blog: [griotold.tistory.com](https://griotold.tistory.com)

## 📄 라이센스

MIT License

---

**위니브 AI Chatbot & RAG 기반 서비스 개발자 양성 과정** 프로젝트
