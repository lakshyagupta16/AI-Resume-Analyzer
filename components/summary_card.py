import streamlit as st

def summary_card(summary):

    st.markdown(f"""
    <div class="dashboard-card">
        <div class="card-title">
            🧠 AI Resume Summary
        </div>

        <div class="card-body">
            {summary}
        </div>

    </div>
    """, unsafe_allow_html=True)