import streamlit as st

from dotenv import load_dotenv


# from llm import get_ai_response

# Streamlit 페이지 기본 설정 (브라우저 탭에 표시되는 제목과 아이콘)
st.set_page_config(page_title="소득세 챗봇", page_icon="🤖")

# 웹 페이지 제목
st.title("🤖 소득세 챗봇")
# 제목 아래 작은 설명 텍스트
st.caption("소득세에 관련된 모든것을 답해드립니다!")

load_dotenv()

# Streamlit 세션 상태 초기화
# 세션 상태: 사용자가 페이지를 새로고침해도 데이터가 유지되는 저장소
# message_list가 없으면 빈 리스트로 생성
if 'message_list' not in st.session_state:
    st.session_state.message_list = []

# 이전에 저장된 모든 메시지를 화면에 출력 (대화 히스토리 표시)
for message in st.session_state.message_list:
    # 메시지의 역할에 따라 (user 또는 ai) 다른 스타일로 표시
    with st.chat_message(message["role"]):
        # 메시지 내용 출력
        st.write(message["content"])


# 사용자가 입력한 메시지를 받음 (입력란이 비어있지 않으면 실행)
# := 는 "walrus operator" - 변수 할당과 동시에 값 확인
if user_question := st.chat_input(placeholder="소득세에 관련된 궁금한 내용들을 말씀해주세요!"):
    # 사용자 메시지를 화면에 표시 (user 스타일로)
    with st.chat_message("user"):
        st.write(user_question)
    # 사용자 메시지를 세션 상태의 message_list에 저장 (나중에 다시 표시될 수 있도록)
    st.session_state.message_list.append({"role": "user", "content": user_question})

# ===== 아래는 나중에 구현할 부분 =====
    # 로딩 표시 (처리 중임을 사용자에게 알림)
    # with st.spinner("답변을 생성하는 중입니다"):
    #     # llm.py의 get_ai_response() 함수 호출해서 AI 응답 생성
    #     ai_response = get_ai_response(user_question)
    #     # AI 응답을 ai 스타일로 표시
    #     with st.chat_message("ai"):
    #         # st.write_stream(): 텍스트를 스트리밍 방식으로 표시 (타이핑 효과)
    #         ai_message = st.write_stream(ai_response)
    #         # AI 메시지를 세션 상태의 message_list에 저장
    #         st.session_state.message_list.append({"role": "ai", "content": ai_message})