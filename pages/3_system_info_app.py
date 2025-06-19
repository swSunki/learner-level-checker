import streamlit as st
import psutil
import platform
import os

st.set_page_config(page_title="System Info", layout="centered")

st.title("📊 Streamlit 실행 환경 정보")

# CPU 정보
cpu_count = psutil.cpu_count(logical=True)
cpu_freq = psutil.cpu_freq()
st.subheader("🧠 CPU")
st.write(f"코어 수 (Logical): {cpu_count}")
if cpu_freq:
    st.write(f"현재 주파수: {cpu_freq.current:.2f} MHz")

# RAM 정보
mem = psutil.virtual_memory()
st.subheader("💾 메모리 (RAM)")
st.write(f"총 용량: {mem.total / (1024 ** 3):.2f} GB")
st.write(f"사용 가능: {mem.available / (1024 ** 3):.2f} GB")

# Storage 정보
st.subheader("🗂️ 저장소 (Storage)")
disk = psutil.disk_usage('/')
st.write(f"총 용량: {disk.total / (1024 ** 3):.2f} GB")
st.write(f"사용 중: {disk.used / (1024 ** 3):.2f} GB")
st.write(f"남은 용량: {disk.free / (1024 ** 3):.2f} GB")

# OS 정보
st.subheader("🖥️ OS 정보")
st.write(f"운영체제: {platform.system()} {platform.release()}")
st.write(f"Python 버전: {platform.python_version()}")
