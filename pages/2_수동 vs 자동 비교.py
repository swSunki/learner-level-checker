
import streamlit as st
import pandas as pd
import pickle
from sklearn.preprocessing import MinMaxScaler
from sklearn.cluster import KMeans

st.set_page_config(page_title="📊 레벨 비교", layout="wide")
st.title("📊 수동 vs 자동 레벨 비교")

uploaded = st.file_uploader("수동 레벨이 포함된 CSV 업로드 (manual_level_4feat 포함)", type=["csv"])

features = [
    "total_lessonExp",
    "total_submittedCount",
    "total_completed_lessons",
    "total_lessons_attempted"
]

if uploaded:
    df = pd.read_csv(uploaded, encoding="utf-8").fillna(0)

    if "manual_level_4feat" not in df.columns:
        st.error("❌ 'manual_level_4feat' 컬럼이 없습니다.")
    else:
        with open("scaler.pkl", "rb") as f:
            scaler = pickle.load(f)
        with open("kmeans.pkl", "rb") as f:
            kmeans = pickle.load(f)

        X_scaled = scaler.transform(df[features])
        clusters = kmeans.predict(X_scaled)

        cluster_means = df.assign(cluster=clusters).groupby("cluster")["total_lessonExp"].mean()
        cluster_order = cluster_means.sort_values().index.tolist()
        cluster_to_level = {cid: i for i, cid in enumerate(cluster_order)}
        df["auto_level_4feat"] = [cluster_to_level[c] for c in clusters]

        df["mismatch"] = df["manual_level_4feat"] != df["auto_level_4feat"]
        error_rate = df["mismatch"].mean()

        st.metric("❗ 오차율", f"{error_rate * 100:.2f}%")

        st.dataframe(df[["uid", "manual_level_4feat", "auto_level_4feat", "total_lessonExp", "mismatch"]].head())

        st.download_button(
            label="📥 비교 결과 CSV 다운로드",
            data=df.to_csv(index=False).encode("utf-8-sig"),
            file_name="level_comparison.csv",
            mime="text/csv"
        )
