import pandas as pd
import numpy as np
import joblib

from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import IsolationForest

from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)

# =====================================================
# LOAD DATASET
# =====================================================

print("=" * 50)
print("LOADING DATASET")
print("=" * 50)

df = pd.read_csv("../data/DSL-StrongPasswordData.csv")

print("Dataset Shape:", df.shape)

# =====================================================
# GENUINE VS IMPOSTER SETUP
# =====================================================

genuine_user = "s002"

# Genuine user data
genuine_data = df[df["subject"] == genuine_user].copy()

# Imposter data
imposter_data = df[df["subject"] != genuine_user].copy()

print("\nGenuine Samples:", genuine_data.shape[0])
print("Imposter Samples:", imposter_data.shape[0])

# =====================================================
# CREATE LABELS
# =====================================================

# Genuine = 1
# Imposter = 0

genuine_data["label"] = 1
imposter_data["label"] = 0

# Combine both
combined_data = pd.concat(
    [genuine_data, imposter_data],
    ignore_index=True
)

# =====================================================
# FEATURES & LABELS
# =====================================================

X = combined_data.drop(columns=["subject", "label"])
y = combined_data["label"]

print("\nFeature Shape:", X.shape)
print("Label Shape:", y.shape)

# =====================================================
# TRAIN TEST SPLIT
# =====================================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

print("\nTraining Samples:", X_train.shape[0])
print("Testing Samples:", X_test.shape[0])

# =====================================================
# FEATURE SCALING
# =====================================================

print("\nScaling Features...")

scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

print("Scaling Completed!")

# Save scaler
joblib.dump(scaler, "models/scaler.pkl")

# =====================================================
# BASE MODEL 1 - RANDOM FOREST
# =====================================================

print("\n" + "=" * 50)
print("TRAINING RANDOM FOREST")
print("=" * 50)

rf_model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

rf_model.fit(X_train_scaled, y_train)

print("Random Forest Trained!")

# =====================================================
# BASE MODEL 2 - SVM
# =====================================================

print("\n" + "=" * 50)
print("TRAINING SVM")
print("=" * 50)

svm_model = SVC(
    probability=True,
    kernel='rbf',
    random_state=42
)

svm_model.fit(X_train_scaled, y_train)

print("SVM Trained!")

# =====================================================
# BASE MODEL 3 - LOGISTIC REGRESSION
# =====================================================

print("\n" + "=" * 50)
print("TRAINING LOGISTIC REGRESSION")
print("=" * 50)

lr_model = LogisticRegression(
    max_iter=1000,
    random_state=42
)

lr_model.fit(X_train_scaled, y_train)

print("Logistic Regression Trained!")

# =====================================================
# CREATE META FEATURES (TRAIN)
# =====================================================

print("\nCreating Train Meta Features...")

rf_train_probs = rf_model.predict_proba(X_train_scaled)[:, 1]
svm_train_probs = svm_model.predict_proba(X_train_scaled)[:, 1]
lr_train_probs = lr_model.predict_proba(X_train_scaled)[:, 1]

train_meta_features = np.column_stack((
    rf_train_probs,
    svm_train_probs,
    lr_train_probs
))

print("Train Meta Features Shape:", train_meta_features.shape)

# =====================================================
# CREATE META FEATURES (TEST)
# =====================================================

print("\nCreating Test Meta Features...")

rf_test_probs = rf_model.predict_proba(X_test_scaled)[:, 1]
svm_test_probs = svm_model.predict_proba(X_test_scaled)[:, 1]
lr_test_probs = lr_model.predict_proba(X_test_scaled)[:, 1]

test_meta_features = np.column_stack((
    rf_test_probs,
    svm_test_probs,
    lr_test_probs
))

print("Test Meta Features Shape:", test_meta_features.shape)

# =====================================================
# META MODEL (STACKING CLASSIFIER)
# =====================================================

print("\n" + "=" * 50)
print("TRAINING META MODEL")
print("=" * 50)

meta_model = LogisticRegression()

meta_model.fit(train_meta_features, y_train)

print("Meta Model Trained!")

# =====================================================
# FINAL PREDICTIONS
# =====================================================

print("\nGenerating Final Predictions...")

y_pred = meta_model.predict(test_meta_features)

# =====================================================
# ISOLATION FOREST (ANOMALY SCORING)
# =====================================================

print("\n" + "=" * 50)
print("TRAINING ISOLATION FOREST")
print("=" * 50)

iso_model = IsolationForest(
    contamination=0.1,
    random_state=42
)

iso_model.fit(train_meta_features)

print("Isolation Forest Trained!")

# Generate anomaly scores
anomaly_scores = iso_model.decision_function(test_meta_features)

print("Anomaly Scores Generated!")

# =====================================================
# MODEL EVALUATION
# =====================================================

print("\n" + "=" * 50)
print("MODEL EVALUATION")
print("=" * 50)

accuracy = accuracy_score(y_test, y_pred)

print("\nAccuracy Score:")
print(accuracy)

print("\nClassification Report:")
print(classification_report(y_test, y_pred))

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

# =====================================================
# SAVE ALL MODELS
# =====================================================

print("\nSaving Models...")

joblib.dump(rf_model, "models/random_forest.pkl")
joblib.dump(svm_model, "models/svm.pkl")
joblib.dump(lr_model, "models/logistic_regression.pkl")
joblib.dump(meta_model, "models/meta_model.pkl")
joblib.dump(iso_model, "models/isolation_forest.pkl")

print("\nAll Models Saved Successfully!")

# =====================================================
# PROJECT COMPLETED
# =====================================================

print("\n" + "=" * 50)
print("STACKED ENSEMBLE TRAINING COMPLETED")
print("=" * 50)