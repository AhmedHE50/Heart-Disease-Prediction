import streamlit as st
import pickle
import numpy as np
import pathlib

st.set_page_config(
    page_title="Prediction Page"
)

#st.sidebar("Hello Page", "Prediction")

def load_css(file_path):
    with open(file_path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

css_path = pathlib.Path("assets/styles.css")
load_css(css_path)


def load_pickle(filename):
    with open(filename, "rb") as f:
        return pickle.load(f)

# Load scaler
scaler = load_pickle("scaler.pkl")

# Load models
models = {
    'SVM': load_pickle('SVM_model.pkl'),
    'Decision Tree': load_pickle('DecisionTree_model.pkl'),
    'Random Forest': load_pickle('RandomForest_model.pkl'),
    'Logistic Regression': load_pickle('LogisticRegression_model.pkl'),
    'KNN': load_pickle('KNN_model.pkl')
}

st.title("Heart Disease Prediction App🫀")
st.divider()

model_name = st.selectbox("Choose a Model", list(models.keys()))

st.subheader("Enter Patient Data")

age = st.number_input("Age", 0, 120, 30)
sex = st.selectbox("Sex", [0, 1], format_func=lambda x: "Male" if x == 1 else "Female")
cp = st.number_input("Chest Pain Type (0-3)", 0, 3, 0)
trestbps = st.number_input("Resting Blood Pressure", 80, 200, 120)
chol = st.number_input("Cholesterol Level", 100, 600, 200)
fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl?", [0, 1], format_func=lambda x: "Yes" if x else "No")
restecg = st.number_input("Resting ECG (0-2)", 0, 2, 0)
thalach = st.number_input("Max Heart Rate Achieved", 60, 250, 150)
exang = st.selectbox("Exercise Induced Angina", [0, 1], format_func=lambda x: "Yes" if x else "No")
oldpeak = st.number_input("ST Depression", 0.0, 10.0, 1.0)
slope = st.selectbox("Slope of ST", [0, 1, 2])
ca = st.selectbox("Number of Major Vessels (0-4)", [0, 1, 2, 3, 4])
thal = st.selectbox("Thalassemia (2 = Normal, 1 = Fixed Defect, 3 = Reversible Defect)", [1, 2, 3])

if st.button("Predict", key='pulse'):
    input_data = np.array([[age, sex, cp, trestbps, chol, fbs, restecg,
                            thalach, exang, oldpeak, slope, ca, thal]])
    input_scaled = scaler.transform(input_data)
    model = models[model_name]
    prediction = model.predict(input_scaled)
    st.success(f"Prediction: {'Heart Disease Detected' if prediction[0] == 1 else 'No Heart Disease'}")
