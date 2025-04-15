import streamlit as st
import pandas as pd
import pickle
from sklearn.preprocessing import MinMaxScaler
from sklearn.cluster import KMeans

st.title("🧠 AI 기반 학습자 레벨 자동 평가기")
st.markdown("""
CSV 파일을 업로드하면, KMeans 모델 기반으로 자동 레벨(`auto_level`)을 부여하고,
업로드된 `manual_level`과 비교하여 오차율을 계산합니다.

필수 컬럼:
- total_lessonExp
- avg_microTestScore
- total_submittedCount
- total_completed_lessons
- total_lessons_attempted
- manual_level
""")

# 1. 모델 불러오기
try:
    with open("scaler.pkl", "rb") as f:
        scaler = pickle.load(f)

    with open("kmeans.pkl", "rb") as f:
        kmeans = pickle.load(f)
except Exception as e:
    st.error("❌ scaler.pkl 또는 kmeans.pkl 파일을 찾을 수 없습니다. 모델을 먼저 학습하세요.")
    st.stop()

# 2. CSV 업로드 받기
uploaded_file = st.file_uploader("CSV 파일 업로드", type="csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    required_cols = [
        "total_lessonExp", "avg_microTestScore", "total_submittedCount",
        "total_completed_lessons", "total_lessons_attempted", "manual_level"
    ]

    if all(col in df.columns for col in required_cols):
        df = df.fillna(0)
        X_input = df[required_cols[:-1]]

        # 3. 정규화 및 클러스터 예측
        X_scaled = scaler.transform(X_input)
        cluster_preds = kmeans.predict(X_scaled)

        # 4. 클러스터 번호 → 레벨 매핑
        cluster_to_level = {
            0: 0,  # Passive
            1: 1,  # High Score
            2: 2,  # Advanced
            3: 3   # Diligent
        }
        df["auto_level"] = [cluster_to_level[c] for c in cluster_preds]
        df["is_mismatch"] = df["manual_level"] != df["auto_level"]

        # 5. 오차율 계산 및 출력
        error_rate = df["is_mismatch"].mean()
        st.subheader("📊 평가 결과")
        st.metric("불일치 오차율", f"{error_rate * 100:.2f}%")

        st.subheader("❗ 불일치 사례 (상위 10건)")
        st.dataframe(df[df["is_mismatch"]].head(10))

        # 결과 다운로드
        to_download = df.to_csv(index=False).encode("utf-8-sig")
        st.download_button("⬇️ 결과 CSV 다운로드", data=to_download,
                           file_name="level_comparison_result.csv",
                           mime="text/csv")
    else:
        st.error("❌ 필수 컬럼이 누락되어 있습니다. CSV 구조를 확인해주세요.")