import pandas as pd
import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="keystroke_warehouse",
    user="postgres",
    password="root"
)

cursor = conn.cursor()

df = pd.read_csv("data/DSL-StrongPasswordData.csv")

df = df.drop(columns=["subject"])
df = df.iloc[:, :11]

print("Rows Loaded:", len(df))

for _, row in df.iterrows():

    cursor.execute("""
        INSERT INTO raw.keystroke_raw (
            feature_1,
            feature_2,
            feature_3,
            feature_4,
            feature_5,
            feature_6,
            feature_7,
            feature_8,
            feature_9,
            feature_10,
            label
        )
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
    """, tuple(row))

conn.commit()

print("Data Loaded Successfully")

cursor.close()
conn.close()