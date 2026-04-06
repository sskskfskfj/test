import os
import sys
import streamlit as st

# 프로젝트 루트 경로 설정 (app 패키지를 인식하기 위함)
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

try:
    import app.front
except Exception as e:
    st.error(f"애플리케이션을 불러오는 중 오류가 발생했습니다: {e}")
