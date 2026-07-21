from components.score_card import display_score
import streamlit as st
from utils.pdf_reader import extract_text
from utils.analyzer import analyze_resume

# Page Configuration
st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide"
)
def load_css():
    with open("assets/styles.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()

# Title
st.markdown("""
<div class="header-box">
    <div class="header-title">
        📄 AI Resume Analyzer
    </div>
    <div class="header-subtitle">
        AI-Powered Resume Evaluation • ATS Score • Resume Insights • Interview Preparation
    </div>
</div>
""", unsafe_allow_html=True)
# Upload PDF
uploaded_file = st.file_uploader(
    "Choose your Resume (PDF)",
    type=["pdf"]
)

if uploaded_file is not None:

    # Read resume text
    resume_text = extract_text(uploaded_file)

    st.success("✅ Resume uploaded successfully!")

    # Optional: Show extracted text
    with st.expander("View Extracted Resume Text"):
        st.write(resume_text)

    # Analyze button
    if st.button("🚀 Analyze Resume"):

        with st.spinner("Analyzing your resume..."):

            analysis = analyze_resume(resume_text)

        # ATS Score
        col1, col2 = st.columns([1, 2])

        with col1:
            display_score(analysis["ats_score"])

        with col2:
            st.info(analysis["summary"])

        

        # Strengths
        st.subheader("💪 Strengths")
        for item in analysis["strengths"]:
            st.success(item)

        # Weaknesses
        st.subheader("⚠️ Weaknesses")
        for item in analysis["weaknesses"]:
            st.warning(item)

        # Missing Skills
        st.subheader("📌 Missing Skills")
        for item in analysis["missing_skills"]:
            st.error(item)

        # Suggestions
        st.subheader("💡 Suggestions")
        for item in analysis["suggestions"]:
            st.info(item)

        # Interview Questions
        st.subheader("🎤 Interview Questions")
        for i, question in enumerate(analysis["interview_questions"], start=1):
            st.markdown(f"**{i}.** {question}")