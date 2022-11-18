import streamlit as st
from PIL import Image

def local_css():
    with open("ui/style.css") as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
        

def max_width():
    max_width_str = f"max-width: 2000px;"
    st.markdown(
        f"""
    <style>
    .reportview-container .main .block-container{{
        {max_width_str}
    }}
    </style>    
    """,
        unsafe_allow_html=True,
    )