import streamlit as st
import plotly.graph_objects as go

def display_score(score):

    fig = go.Figure(go.Indicator(

        mode="gauge+number",

        value=score,

        number={'suffix': "%"},

        title={'text': "ATS Score"},

        gauge={

            'axis': {'range': [0, 100]},

            'bar': {'color': "#3B82F6"},

            'steps': [

                {'range': [0, 60], 'color': "#EF4444"},

                {'range': [60, 80], 'color': "#F59E0B"},

                {'range': [80, 100], 'color': "#22C55E"}

            ],

        }

    ))

    fig.update_layout(

        height=300,

        margin=dict(l=20, r=20, t=60, b=20),

        paper_bgcolor="#0F172A",

        font=dict(color="white")

    )

    st.plotly_chart(fig, use_container_width=True)