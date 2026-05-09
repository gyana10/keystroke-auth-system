# ⌨️ AI Keystroke Authentication System

An AI-powered Behavioral Biometrics Authentication System that verifies users based on their unique typing patterns using Machine Learning, Ensemble Learning, and Anomaly Detection.

---

# 🚀 Live Demo

🔗 https://keystroke-app-system-in9vfxa49ttrgjhzpngnaf.streamlit.app/

---

# 📌 Project Overview

Traditional authentication systems rely only on passwords, which can be stolen, guessed, or shared. This project introduces an advanced AI-based authentication system that analyzes keystroke dynamics (typing behavior) to identify whether a user is genuine or suspicious.

The system captures behavioral biometric patterns from typing data and applies multiple machine learning models to perform real-time authentication.

This project demonstrates:
- Behavioral Biometrics
- Machine Learning Authentication
- Ensemble Learning
- Anomaly Detection
- Real-Time AI Prediction
- Streamlit Cloud Deployment

---

# 🧠 Key Features

✅ Behavioral Biometrics Authentication  
✅ Ensemble Machine Learning Model  
✅ Isolation Forest Anomaly Detection  
✅ Manual Feature Authentication  
✅ CSV File Authentication  
✅ Real-Time Prediction System  
✅ Confidence Score Calculation  
✅ Interactive Streamlit Dashboard  
✅ AI-Based Suspicious User Detection  
✅ Cloud Deployment using Streamlit  

---

# 🛠️ Technologies Used

## Frontend
- Streamlit
- Plotly

## Backend / AI
- Python
- FastAPI
- Scikit-learn
- NumPy
- Pandas
- Joblib

## Machine Learning Models
- Random Forest
- Support Vector Machine (SVM)
- Logistic Regression
- Meta Ensemble Model
- Isolation Forest

## Deployment
- Streamlit Cloud
- GitHub

---

# 🤖 Machine Learning Architecture

The system uses an Ensemble Learning Architecture:

### Base Models
- Random Forest
- SVM
- Logistic Regression

### Meta Model
The probabilities generated from the base models are combined using a Meta Model for final prediction.

### Anomaly Detection
Isolation Forest is used to calculate anomaly scores and detect suspicious behavior.

---

# 📊 Input Features

The model uses 33 keystroke timing features extracted from user typing behavior.

Examples include:
- Hold Time (H)
- Down-Down Time (DD)
- Up-Down Time (UD)
- Key Press Duration
- Key Transition Latency

These behavioral patterns uniquely identify users.

---

# 📂 Project Structure

```bash
keystroke-auth-system/
│
├── backend/
│   ├── models/
│   │   ├── scaler.pkl
│   │   ├── random_forest.pkl
│   │   ├── svm.pkl
│   │   ├── logistic_regression.pkl
│   │   ├── meta_model.pkl
│   │   └── isolation_forest.pkl
│   │
│   ├── main.py
│   ├── train_model.py
│   ├── preprocess.py
│   └── requirements.txt
│
├── frontend/
│   └── app.py
│
├── data/
│   └── dataset.csv
│
├── notebooks/
│
├── requirements.txt
├── README.md
└── .gitignore