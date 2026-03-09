import streamlit as st
import pickle
import numpy as np

# Load trained model
model = pickle.load(open("gold_model.pkl", "rb"))

st.title("Gold Price Prediction App")

st.write("Enter the economic indicators to predict gold price")

# User inputs
spx = st.number_input("SPX (Stock Market Index)")
uso = st.number_input("USO (Oil Price)")
slv = st.number_input("SLV (Silver Price)")
eur_usd = st.number_input("EUR/USD Exchange Rate")

# Prediction button
if st.button("Predict Gold Price"):
    
    input_data = np.array([[spx, uso, slv, eur_usd]])
    
    prediction = model.predict(input_data)
    
    st.success(f"Predicted Gold Price (GLD): {prediction[0]:.2f}")