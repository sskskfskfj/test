import sys
import os
from streamlit.web import cli as stcli

def main():
    # Streamlit Cloud 등 이미 실행 중인 환경에서는 중복 실행하지 않음
    # 환경 변수나 sys.argv를 통해 이미 streamlit run 중인지 확인
    if "streamlit" in sys.argv[0] or any("streamlit" in arg for arg in sys.argv):
        return

    sys.argv = ["streamlit", "run", "app/front.py", "--server.port", "8501", "--server.address", "0.0.0.0"]
    sys.exit(stcli.main())

if __name__ == "__main__":
    main()
