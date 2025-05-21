import streamlit as st
import sys
import os
os.environ["PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION"] = "python"

# Allow Streamlit to import from the backend folderpip show protobuf

sys.path.append(os.path.abspath(os.path.join(os.path.dirname("C:\\Users\\Devar\\Downloads\\Prompt Engineering\\generator.py"), '..')))

from generator import get_study_prompts

# Streamlit UI Setup
st.set_page_config(page_title="🧠 Local Exam Prompt Generator", page_icon="📚")
st.title("📚 Exam Prep Prompt Generator (Offline - GPT-2)")
st.markdown("Generate smart study questions using a locally running GPT-2 model!")

# --- User Inputs ---
topic = st.text_input("📘 Enter your topic or subject:", placeholder="e.g. Thermodynamics, Contract Law")
exam_type = st.selectbox("🧪 Select exam type:", ["Multiple Choice", "Essay", "Oral Exam", "Problem Solving", "Coding Interview"])
level = st.selectbox("🎓 Choose your level:", ["High School", "Undergraduate", "Graduate", "Professional"])

generate = st.button("🚀 Generate Study Prompts")

# --- Output ---
if generate and topic:
    with st.spinner("Thinking with GPT-2... (this may take a few seconds)"):
        try:
            result = get_study_prompts(topic, exam_type, level)
            st.markdown("### 📝 Suggested Study Questions:")
            st.markdown(result)
        except Exception as e:
            st.error(f"⚠️ Something went wrong:\n\n{e}")
elif generate:
    st.warning("🚨 Please enter a topic before generating.")
