
import streamlit as st
import pandas as pd

st.set_page_config(page_title="📝 수동 레벨 할당기", layout="wide")
st.title("📝 수동 레벨 할당기")

uploaded = st.file_uploader("CSV 파일을 업로드해주세요 (total_lessonExp 포함)", type=["csv"])

def assign_manual_level(exp):
    if exp >= 40000:
        return 3
    elif exp >= 16000:
        return 2
    elif exp >= 6000:
        return 1
    else:
        return 0

if uploaded:
    df = pd.read_csv(uploaded, encoding="utf-8").fillna(0)

    if "total_lessonExp" not in df.columns:
        st.error("❌ 'total_lessonExp' 컬럼이 누락되었습니다.")
    else:
        df["manual_level_4feat"] = df["total_lessonExp"].apply(assign_manual_level)
        st.success("✅ 수동 레벨이 할당되었습니다.")
        st.dataframe(df.head())

        st.download_button(
            label="📥 수동 레벨 CSV 다운로드",
            data=df.to_csv(index=False).encode("utf-8-sig"),
            file_name="manual_labeled.csv",
            mime="text/csv"
        )
else:
    st.info("CSV 파일을 업로드해주세요.")
