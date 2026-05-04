import os
import sys
import streamlit as st

# 현재 디렉토리를 path에 추가하여 app 모듈을 불러올 수 있도록 설정
# root 디렉토리에서 실행될 것을 가정함
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if ROOT_DIR not in sys.path:
    sys.path.append(ROOT_DIR)

from app.embedder import SimilartyBaseLogic

# 페이지 설정
st.set_page_config( # 여기 수정 2026-05-03
    page_title="TALKTALK한 선배",
    layout="centered"
)

@st.cache_resource
def load_chatbot_logic():
    logic = SimilartyBaseLogic()
    logic.getSentenceFromJson(fileDir="data/dummy.json")

    return logic

try:
    chatbot = load_chatbot_logic()
except Exception as e:
    st.error(f"모델 또는 데이터를 불러오는 중 오류가 발생했습니다: {e}")
    st.stop()

# 사이드바 설정
with st.sidebar:
    st.title("챗봇 설정") # 여기도 수정 2026-05-03
    st.info("주제를 벗어난 질문에는 답변이 제한될 수 있습니다.")
    if st.button("대화 기록 삭제"):
        st.session_state.messages = []
        st.rerun()

# 메인 UI
st.title("TALKTALK한 선배")
st.caption("궁금하신 내용을 질문해 주세요.")

# 세션 상태 초기화 (대화 기록 저장)
if "messages" not in st.session_state:
    st.session_state.messages = []

# 대화 기록 표시
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 사용자 입력 처리
# 여기도 수정 2026-05-03
if prompt := st.chat_input("질문을 입력해주세요."):
    # 1. 사용자 메시지 표시 및 저장
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # 2. 챗봇 응답 생성
    with st.chat_message("assistant"):
        with st.spinner("분석 중입니다..."):
            try:
                response = chatbot.getSimilarity(prompt)
                st.markdown(response)
            except Exception as e:
                response = f"응답 생성 중 오류가 발생했습니다: {e}"
                st.error(response)
    
    # 3. 챗봇 메시지 저장
    st.session_state.messages.append({"role": "assistant", "content": response})
