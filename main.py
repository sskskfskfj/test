import os
import sys
import streamlit.web.cli as stcli
from streamlit.runtime import exists

# 1. 경로 설정 (app 패키지를 올바르게 찾기 위함)
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

def main():
    # 2. 현재 실행 중인 환경이 Streamlit 내부인지 확인
    if not exists():
        # [상황 A] 로컬에서 "python main.py"라고 직접 쳤을 때
        # -> 스스로를 streamlit 환경으로 재실행시켜서 브라우저를 띄워줍니다.
        sys.argv = [
            "streamlit",
            "run",
            os.path.join(ROOT_DIR, "main.py"),
        ]
        sys.exit(stcli.main())
    else:
        # [상황 B] 배포 서버(Cloud)나 로컬에서 "streamlit run main.py"로 켰을 때
        # -> 실제 우리 서비스 화면(front.py)을 불러와서 보여줍니다.
        try:
            import app.front
        except Exception as e:
            import streamlit as st
            st.error(f"애플리케이션을 불러오는 중 오류가 발생했습니다: {e}")

if __name__ == "__main__":
    main()
