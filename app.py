import streamlit as st
import pages
import pathlib

st.set_page_config(
    page_title="Hello Page"
)

def load_css(file_path):
    with open(file_path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

css_path = pathlib.Path("assets/styles.css")
load_css(css_path)


st.header("Welcome to Heart Disease Prediction App")
st.divider()
st.image("images/heart_disease.jpg")

st.page_link("pages/pred_page.py", label="Start Prediction Now")
