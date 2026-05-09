import streamlit as st
import requests
import pandas as pd
import plotly.express as px
import random

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="Keystroke Authentication System",
    layout="wide",
    page_icon="⌨️"
)

# =====================================================
# CUSTOM CSS
# =====================================================

st.markdown("""
<style>

.main {
    background-color: #0E1117;
}

.stButton>button {
    width: 100%;
    border-radius: 10px;
    height: 3em;
    font-size: 18px;
    font-weight: bold;
}

</style>
""", unsafe_allow_html=True)

# =====================================================
# TITLE
# =====================================================

st.title("⌨️ AI Keystroke Authentication System")

st.markdown("""
### Behavioral Biometrics + Ensemble AI + Anomaly Detection

This system authenticates users based on typing behavior patterns.
""")

# =====================================================
# SYSTEM STATUS
# =====================================================

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Accuracy",
        "98.87%"
    )

with col2:
    st.metric(
        "Models Used",
        "5"
    )

with col3:
    st.metric(
        "Threat Detection",
        "ACTIVE"
    )

with col4:
    st.metric(
        "System Status",
        "ONLINE"
    )

st.divider()

# =====================================================
# SIDEBAR
# =====================================================

st.sidebar.title("Navigation")

page = st.sidebar.radio(
    "Go To",
    [
        "Manual Authentication",
        "CSV Authentication",
        "Project Info"
    ]
)

# =====================================================
# PROJECT INFO PAGE
# =====================================================

if page == "Project Info":

    st.header("📌 Project Overview")

    st.markdown("""
    ## 🔐 About This Project

    This system uses keystroke dynamics and ensemble machine learning
    to authenticate users based on typing behavior.

    ## 🤖 Machine Learning Models

    - Random Forest
    - Support Vector Machine (SVM)
    - Logistic Regression
    - Meta Classifier
    - Isolation Forest

    ## 🧠 Core Technologies

    - FastAPI
    - Streamlit
    - Scikit-learn
    - Plotly
    - Behavioral Biometrics

    ## 🚨 Security Features

    - Impersonation Detection
    - Threat Analysis
    - Anomaly Scoring
    - Real-Time Authentication
    """)

# =====================================================
# MANUAL AUTHENTICATION
# =====================================================

elif page == "Manual Authentication":

    st.header("🔐 Manual Authentication")

    st.write("Enter 33 keystroke timing features.")

    # Generate sample values
    if st.button("Generate Sample Features"):

        st.session_state["sample_data"] = [
            round(random.uniform(0.05, 0.4), 4)
            for _ in range(33)
        ]

    features = []

    for i in range(33):

        default_value = 0.1

        if "sample_data" in st.session_state:
            default_value = st.session_state["sample_data"][i]

        value = st.number_input(
            f"Feature {i+1}",
            value=float(default_value),
            format="%.4f"
        )

        features.append(value)

    # =====================================================
    # AUTHENTICATION BUTTON
    # =====================================================

    if st.button("Authenticate User"):

        with st.spinner("Authenticating..."):

            url = "http://127.0.0.1:8000/predict"

            payload = {
                "features": features
            }

            response = requests.post(
                url,
                json=payload
            )

            result = response.json()

            prediction = result["prediction"]
            confidence = result["confidence"]
            anomaly_score = result["anomaly_score"]

            st.success("Authentication Completed!")

            col1, col2, col3 = st.columns(3)

            with col1:

                if prediction == "Genuine User":
                    st.success(prediction)
                else:
                    st.error(prediction)

            with col2:

                st.metric(
                    "Confidence Score",
                    f"{confidence:.2f}"
                )

            with col3:

                threat = "LOW"

                if anomaly_score < 0:
                    threat = "HIGH"

                st.metric(
                    "Threat Level",
                    threat
                )

            # =====================================================
            # MODEL SCORES
            # =====================================================

            st.subheader("📊 Base Model Confidence Scores")

            scores_df = pd.DataFrame({
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

            fig = px.bar(
                scores_df,
                x="Model",
                y="Probability",
                title="Model Confidence Scores"
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

# =====================================================
# CSV AUTHENTICATION
# =====================================================

elif page == "CSV Authentication":

    st.header("📂 CSV Authentication")

    st.write("""
    Upload CSV file containing exactly 33 keystroke timing features.
    """)

    # =====================================================
    # FEATURE EXPLANATION
    # =====================================================

    with st.expander("📘 Detailed Feature Explanation"):

        st.markdown("""
        # ⌨️ Understanding Keystroke Features

        Each row in the CSV represents one typing attempt.

        The system analyzes timing behavior while typing a password.

        ---

        # 🟢 Hold Time Features (H)

        Measures how long a key is pressed.

        Example:
        - H.t → Time key 't' is held

        Features:
        - H.period
        - H.t
        - H.i
        - H.e
        - H.five
        - H.Shift.r
        - H.o
        - H.a
        - H.n
        - H.l
        - H.Return

        ---

        # 🔵 Down-Down Features (DD)

        Time between pressing two keys.

        Example:
        - DD.t.i → Time between pressing 't' and 'i'

        Features:
        - DD.period.t
        - DD.t.i
        - DD.i.e
        - DD.e.five
        - DD.five.Shift.r
        - DD.Shift.r.o
        - DD.o.a
        - DD.a.n
        - DD.n.l
        - DD.l.Return

        ---

        # 🟡 Up-Down Features (UD)

        Time between releasing one key and pressing another.

        Example:
        - UD.t.i → Time between releasing 't' and pressing 'i'

        Features:
        - UD.period.t
        - UD.t.i
        - UD.i.e
        - UD.e.five
        - UD.five.Shift.r
        - UD.Shift.r.o
        - UD.o.a
        - UD.a.n
        - UD.n.l
        - UD.l.Return

        ---

        # 📄 CSV Requirements

        ✅ Exactly 33 numerical columns  
        ✅ One row = one typing attempt  
        ✅ No text values  
        ✅ No subject labels  

        ---

        # 📌 Expected Column Order

        1. sessionIndex
        2. rep
        3. H.period
        4. DD.period.t
        5. UD.period.t
        6. H.t
        7. DD.t.i
        8. UD.t.i
        9. H.i
        10. DD.i.e
        11. UD.i.e
        12. H.e
        13. DD.e.five
        14. UD.e.five
        15. H.five
        16. DD.five.Shift.r
        17. UD.five.Shift.r
        18. H.Shift.r
        19. DD.Shift.r.o
        20. UD.Shift.r.o
        21. H.o
        22. DD.o.a
        23. UD.o.a
        24. H.a
        25. DD.a.n
        26. UD.a.n
        27. H.n
        28. DD.n.l
        29. UD.n.l
        30. H.l
        31. DD.l.Return
        32. UD.l.Return
        33. H.Return
        """)

    # =====================================================
    # FILE UPLOAD
    # =====================================================

    uploaded_file = st.file_uploader(
        "Upload CSV File",
        type=["csv"]
    )

    if uploaded_file is not None:

        try:

            df = pd.read_csv(uploaded_file)

            st.subheader("📄 Uploaded Data")

            st.dataframe(df.head())

            # =====================================================
            # VALIDATION
            # =====================================================

            if df.shape[1] != 33:

                st.error(
                    f"Invalid CSV! Expected 33 columns but found {df.shape[1]}"
                )

            else:

                st.success("CSV Validated Successfully!")

                if st.button("Authenticate CSV Data"):

                    predictions = []

                    url = "http://127.0.0.1:8000/predict"

                    progress_bar = st.progress(0)

                    for index, row in df.iterrows():

                        payload = {
                            "features": row.tolist()
                        }

                        response = requests.post(
                            url,
                            json=payload
                        )

                        result = response.json()

                        predictions.append({
                            "Prediction": result["prediction"],
                            "Confidence": round(
                                result["confidence"], 4
                            ),
                            "Anomaly Score": round(
                                result["anomaly_score"], 4
                            )
                        })

                        progress_bar.progress(
                            (index + 1) / len(df)
                        )

                    result_df = pd.DataFrame(predictions)

                    # =====================================================
                    # RESULTS
                    # =====================================================

                    st.subheader("🔐 Authentication Results")

                    st.dataframe(result_df)

                    # =====================================================
                    # METRICS
                    # =====================================================

                    genuine_count = (
                        result_df["Prediction"]
                        == "Genuine User"
                    ).sum()

                    suspicious_count = (
                        result_df["Prediction"]
                        == "Suspicious User"
                    ).sum()

                    col1, col2 = st.columns(2)

                    with col1:
                        st.metric(
                            "Genuine Users",
                            genuine_count
                        )

                    with col2:
                        st.metric(
                            "Suspicious Users",
                            suspicious_count
                        )

                    # =====================================================
                    # PIE CHART
                    # =====================================================

                    pie_fig = px.pie(
                        result_df,
                        names="Prediction",
                        title="Authentication Distribution"
                    )

                    st.plotly_chart(
                        pie_fig,
                        use_container_width=True
                    )

                    # =====================================================
                    # HISTOGRAM
                    # =====================================================

                    hist_fig = px.histogram(
                        result_df,
                        x="Confidence",
                        title="Confidence Distribution"
                    )

                    st.plotly_chart(
                        hist_fig,
                        use_container_width=True
                    )

                    # =====================================================
                    # DOWNLOAD REPORT
                    # =====================================================

                    csv = result_df.to_csv(index=False)

                    st.download_button(
                        label="📥 Download Authentication Report",
                        data=csv,
                        file_name="authentication_results.csv",
                        mime="text/csv"
                    )

        except Exception as e:

            st.error(f"Error Processing File: {e}")

# =====================================================
# FOOTER
# =====================================================

st.divider()

st.markdown("""
<center>
Developed by <b>Gyana Ranjan Mohanty</b><br>
AI-Based Behavioral Biometric Authentication System
</center>
""", unsafe_allow_html=True)