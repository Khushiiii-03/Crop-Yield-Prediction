import streamlit as st
import numpy as np
import pickle

with open("model.pkl", "rb") as f:
    model = pickle.load(f)

crop_dict = {
    0: 'apple', 1: 'banana', 2: 'blackgram', 3: 'chickpea', 4: 'coconut',
    5: 'coffee', 6: 'cotton', 7: 'grapes', 8: 'jute', 9: 'kidneybeans',
    10: 'lentil', 11: 'maize', 12: 'mango', 13: 'mothbeans', 14: 'mungbean',
    15: 'muskmelon', 16: 'orange', 17: 'papaya', 18: 'pigeonpeas',
    19: 'pomegranate', 20: 'rice', 21: 'watermelon'
}

st.subheader("🌱 Crop Recommendation System")

N = st.number_input("Enter the value of Nitrogen content(N) (in %)", value=50.0)
P = st.number_input("Enter the value of Phosphorous content(P) (in %)", value=30.0)
K = st.number_input("Enter the value of Potassium content(K) (in %)", value=40.0)
temp = st.number_input("Enter the temperature in degree celsius", value=25.0)
humidity = st.number_input("Enter the humidity percent", value=60.0)
ph = st.number_input("Enter the pH value", value=6.0)
rainfall = st.number_input("Enter the rainfall amount in mm", value=100.0)

if st.button("Predict"):
    input_data = np.array([[N, P, K, temp, humidity, ph, rainfall]])
    prediction = model.predict(input_data)[0]

    crop = crop_dict.get(prediction, "Unknown Crop")

    st.subheader("🌾 Recommended Crop:")
    st.success(f"✅ {crop.capitalize()}")
    st.write(f"🔢 Model output: `{prediction}`")
