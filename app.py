import streamlit as st
from utils.pdf_reader import extract_text
from utils.analyzer import analyze_resume

# Page Configuration
st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide"
)

# Title
st.title("📄 AI Resume Analyzer")
st.write("Upload your resume (PDF) and get an AI-powered ATS analysis.")

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
            st.metric("🎯 ATS Score", f"{analysis['ats_score']}%")

        with col2:
            st.info(analysis["summary"])

        # Summary
        st.subheader("📄 Summary")
        st.write(analysis["summary"])

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