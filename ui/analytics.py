import streamlit as st

def analytics_dashboard(results):
    scores = [r["score"] for r in results]
    st.bar_chart(scores)
