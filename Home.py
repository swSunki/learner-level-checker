
import streamlit as st

st.set_page_config(page_title="📊 학습자 레벨 평가", layout="wide")
st.title("📊 학습자 레벨 평가")

st.markdown("""
이 앱은 총 2단계로 구성됩니다:

1. **수동 레벨 할당**: 경험치(total_lessonExp)를 기준으로 학습자에게 수동 레벨을 부여합니다.
2. **수동 vs 자동 비교**: 클러스터링 기반 자동 레벨과 수동 기준의 일치율을 비교하고 오차율을 확인합니다.

좌측 사이드바에서 원하는 기능을 선택하세요.
""")
