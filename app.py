import streamlit as st
from utils.pdf_reader import extract_text

# Configure page
st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide"
)

# Title
st.title("📄 AI Resume Analyzer")

st.write("Welcome to your first AI project!")

st.header("Upload Your Resume")

uploaded_file = st.file_uploader(
    "Choose a PDF Resume",
    type=["pdf"]
)

if uploaded_file is not None:

    st.success("Resume uploaded successfully! 🎉")

    st.write("Filename:", uploaded_file.name)

    # Extract text from PDF
    resume_text = extract_text(uploaded_file)

    st.subheader("📄 Extracted Resume Text")

    st.text_area(
        "Resume Content",
        resume_text,
        height=400
    )