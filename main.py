import sys
from streamlit.web import cli as stcli

def main():
    # streamlit run app/front.py 명령어를 실행하는 것과 동일한 효과
    sys.argv = ["streamlit", "run", "app/front.py"]
    sys.exit(stcli.main())

if __name__ == "__main__":
    main()
