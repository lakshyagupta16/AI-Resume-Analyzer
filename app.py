import streamlit as st
from utils.pdf_reader import extract_text
from utils.analyzer import analyze_resume

# Configure page
st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide"
)

st.title("📄 AI Resume Analyzer")
st.write("Upload your resume and get an AI-powered ATS analysis!")

uploaded_file = st.file_uploader(
    "Choose your Resume (PDF)",
    type=["pdf"]
)

if uploaded_file is not None:

    st.success("Resume uploaded successfully!")

    resume_text = extract_text(uploaded_file)

    with st.expander("📄 Extracted Resume"):
        st.write(resume_text)

    if st.button("🚀 Analyze Resume"):

        with st.spinner("Analyzing your resume using Gemini AI..."):

            analysis = analyze_resume(resume_text)

        st.success("Analysis Completed!")

        st.markdown("## 📊 AI Analysis")

        st.write(analysis)