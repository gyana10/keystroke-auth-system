import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("../data/DSL-StrongPasswordData.csv")

print("=" * 50)
print("DATASET OVERVIEW")
print("=" * 50)

print("\nShape of Dataset:")
print(df.shape)

print("\nColumns:")
print(df.columns)

print("\nFirst 5 Rows:")
print(df.head())

print("\nMissing Values:")
print(df.isnull().sum())

print("\nUnique Users:")
print(df["subject"].nunique())

print("\nSamples Per User:")
print(df["subject"].value_counts())


df["subject"].value_counts().plot(
    kind='bar',
    figsize=(14,6)
)

plt.title("Samples Per User")
plt.xlabel("Users")
plt.ylabel("Number of Samples")

plt.tight_layout()

plt.show()