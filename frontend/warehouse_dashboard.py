import pandas as pd


# =====================================================
# USER STATISTICS
# =====================================================

def get_user_statistics():

    return pd.DataFrame({
        "label": [0, 1],
        "total_samples": [19952, 432],
        "avg_feature_1": [4.52, 3.28],
        "avg_feature_2": [25.57, 22.21],
        "avg_feature_3": [0.093, 0.080]
    })


# =====================================================
# TYPING METRICS
# =====================================================

def get_typing_metrics():

    return pd.DataFrame({
        "avg_feature_1": [4.5],
        "avg_feature_2": [25.5],
        "avg_feature_3": [0.093],
        "avg_feature_4": [0.081],
        "total_records": [20400]
    })


# =====================================================
# DASHBOARD SUMMARY
# =====================================================

def get_dashboard_summary():

    metrics = get_typing_metrics()

    return {
        "total_records": int(metrics["total_records"].iloc[0]),
        "avg_feature_1": float(metrics["avg_feature_1"].iloc[0]),
        "avg_feature_2": float(metrics["avg_feature_2"].iloc[0]),
        "avg_feature_3": float(metrics["avg_feature_3"].iloc[0]),
        "avg_feature_4": float(metrics["avg_feature_4"].iloc[0])
    }


# =====================================================
# MODEL INFORMATION
# =====================================================

def get_model_information():

    return {
        "Random Forest": "Loaded",
        "SVM": "Loaded",
        "Logistic Regression": "Loaded",
        "Meta Model": "Loaded",
        "Isolation Forest": "Loaded"
    }