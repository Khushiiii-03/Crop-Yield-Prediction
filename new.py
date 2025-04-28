import streamlit as st
import numpy as np
import pickle

# Load the model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

# Crop Dictionary
crop_dict = {
    0: 'apple', 1: 'banana', 2: 'blackgram', 3: 'chickpea', 4: 'coconut',
    5: 'coffee', 6: 'cotton', 7: 'grapes', 8: 'jute', 9: 'kidneybeans',
    10: 'lentil', 11: 'maize', 12: 'mango', 13: 'mothbeans', 14: 'mungbean',
    15: 'muskmelon', 16: 'orange', 17: 'papaya', 18: 'pigeonpeas',
    19: 'pomegranate', 20: 'rice', 21: 'watermelon'
}

# Page Config
st.set_page_config(page_title="Crop Recommendation System 🌱", page_icon="🌾", layout="wide")

# Background CSS
page_bg = """
<style>
[data-testid="stAppViewContainer"] {
    background-image: url('https://images.unsplash.com/photo-1582281298056-2ebdfa2b1e89?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=MnwzNjUyOXwwfDF8c2VhcmNofDJ8fGNyb3B8ZW58MHx8fHwxNjc4MTY1Nzky&ixlib=rb-4.0.3&q=80&w=1080');
    background-size: cover;
    background-position: center;
}
[data-testid="stAppViewContainer"]::before {
    content: "";
    position: absolute;
    inset: 0;
    background: rgba(255, 255, 255, 0.5); /* White layer with 50% transparency */
    z-index: 0;
}
.block-container {
    position: relative;
    z-index: 1;
}
[data-testid="stHeader"] {
    background: rgba(0,0,0,0);
}
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)

# Title
st.title("🌾 Smart Crop Recommendation System")
st.markdown("#### Predict the best crop to cultivate based on soil and weather conditions. 🌎")

# Inputs organized nicely
with st.form(key="crop_form"):
    col1, col2, col3 = st.columns(3)
    with col1:
        N = st.number_input("Nitrogen Content (N) [%]", value=50.0)
        K = st.number_input("Potassium Content (K) [%]", value=40.0)
        ph = st.number_input("pH Value", value=6.0)
    with col2:
        P = st.number_input("Phosphorus Content (P) [%]", value=30.0)
        temp = st.number_input("Temperature [°C]", value=25.0)
    with col3:
        humidity = st.number_input("Humidity [%]", value=60.0)
        rainfall = st.number_input("Rainfall [mm]", value=100.0)

    predict_button = st.form_submit_button("🚀 Predict Crop")

# Prediction
if predict_button:
    input_data = np.array([[N, P, K, temp, humidity, ph, rainfall]])
    prediction = model.predict(input_data)[0]
    crop = crop_dict.get(prediction, "Unknown Crop")

    st.success(f"✅ Recommended Crop: **{crop.capitalize()}**")
    st.info(f"🔢 Model output code: `{prediction}`")
