import streamlit as st

def local_css():
    with open("ui/style.css") as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
