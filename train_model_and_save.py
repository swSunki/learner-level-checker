import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.cluster import KMeans
import pickle

# 1. 데이터 불러오기
df = pd.read_csv("student_learning3_raws.csv", encoding="latin1")

# 2. 필요한 지표만 추출
features = [
    "total_lessonExp",
    "avg_microTestScore",
    "total_submittedCount",
    "total_completed_lessons",
    "total_lessons_attempted"
]
df = df[features].fillna(0)

# 3. 정규화 및 클러스터링
scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(df)

kmeans = KMeans(n_clusters=4, random_state=42, n_init=10)
kmeans.fit(X_scaled)

# 4. 모델 저장
with open("scaler.pkl", "wb") as f:
    pickle.dump(scaler, f)

with open("kmeans.pkl", "wb") as f:
    pickle.dump(kmeans, f)

print("✅ scaler.pkl, kmeans.pkl 저장 완료!")
