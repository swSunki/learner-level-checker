# Learner Level Checker

📊 Compare manual and AI-predicted learner levels using KMeans clustering.

## 🔧 Features

- Upload a CSV file containing learner stats and manual levels
- Automatically predicts levels using pretrained KMeans model
- Shows error rate between manual and auto levels
- Download detailed comparison results

## 📁 Expected CSV Columns

- total_lessonExp
- avg_microTestScore
- total_submittedCount
- total_completed_lessons
- total_lessons_attempted
- manual_level

## 🚀 How to Use

1. Go to the app:
   [https://swfact-learner-level-checker.streamlit.app/](https://swfact-learner-level-checker.streamlit.app/)

2. Upload your CSV file.

3. Review the error rate and download comparison results.

## 🛠️ Developer Notes

To retrain the model:

```bash
python train_model_and_save.py
```
