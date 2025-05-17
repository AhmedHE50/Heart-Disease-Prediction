import streamlit as st
from streamlit_extras.switch_page_button import switch_page
import pathlib

st.set_page_config(
    page_title="Home Page"
)

def load_css(file_path):
    with open(file_path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

css_path = pathlib.Path("assets/styles.css")
load_css(css_path)


st.header("Welcome to Heart Disease Prediction App🫀")
st.divider()
st.write("Predict the propability of heart disease using Ai model")
st.image("images/heart_disease.jpg")

if st.button("Start Predicton Now", key='pulse'):
    st.switch_page("pages\Prediction_page.py")


