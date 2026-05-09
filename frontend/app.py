import streamlit as st
import requests
import pandas as pd

# ============================================
# PAGE CONFIG
# ============================================

st.set_page_config(
    page_title="Keystroke Authentication System",
    layout="wide"
)

# ============================================
# TITLE
# ============================================

st.title("⌨️ Keystroke Dynamics Authentication")

st.markdown("""
AI-powered behavioral biometric authentication system
using stacked ensemble machine learning.
""")

# ============================================
# FEATURE INPUT
# ============================================

st.header("Enter 33 Keystroke Features")

features = []

for i in range(33):
    value = st.number_input(
        f"Feature {i+1}",
        value=0.1,
        format="%.4f"
    )

    features.append(value)

# ============================================
# PREDICT BUTTON
# ============================================

if st.button("Authenticate User"):

    url = "http://127.0.0.1:8000/predict"

    payload = {
        "features": features
    }

    response = requests.post(
        url,
        json=payload
    )

    result = response.json()

    st.subheader("Prediction Result")

    if result["prediction"] == "Genuine User":
        st.success(result["prediction"])
    else:
        st.error(result["prediction"])

    # ============================================
    # DISPLAY SCORES
    # ============================================

    st.write("### Confidence Score")
    st.write(result["confidence"])

    st.write("### Anomaly Score")
    st.write(result["anomaly_score"])

    st.write("### Base Model Scores")

    scores = pd.DataFrame({
        "Model": [
            "Random Forest",
            "SVM",
            "Logistic Regression"
        ],
        "Probability": [
            result["rf_probability"],
            result["svm_probability"],
            result["lr_probability"]
        ]
    })

    st.dataframe(scores)