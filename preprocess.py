import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import joblib

df = pd.read_csv("../data/DSL-StrongPasswordData.csv")

genuine_user = "s002"

genuine_data = df[df["subject"] == genuine_user]

imposter_data = df[df["subject"] != genuine_user]

print("Genuine Shape:", genuine_data.shape)
print("Imposter Shape:", imposter_data.shape)

X_genuine = genuine_data.drop(columns=["subject"])
X_imposter = imposter_data.drop(columns=["subject"])

X_train, X_test_genuine = train_test_split(
    X_genuine,
    test_size=0.2,
    random_state=42
)

X_test = pd.concat([X_test_genuine, X_imposter])

y_test = [1] * len(X_test_genuine) + [-1] * len(X_imposter)

scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

joblib.dump(scaler, "models/scaler.pkl")

print("\nPreprocessing Completed!")
print("Training Shape:", X_train_scaled.shape)
print("Testing Shape:", X_test_scaled.shape)