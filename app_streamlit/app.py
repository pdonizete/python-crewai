"""Simple Streamlit front-end for triggering analysis."""

import streamlit as st

from agentes_crewai import Orquestrador

st.title("Code Analysis")

path = st.text_input("Path to analyze", value=".")

if st.button("Run Analysis"):
    orq = Orquestrador(path)
    report = orq.run()
    st.text(report)
