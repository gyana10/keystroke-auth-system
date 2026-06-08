```
                ┌─────────────────────┐
                │     CSV Dataset     │
                └──────────┬──────────┘
                           │
                           ▼
                ┌─────────────────────┐
                │     ETL Pipeline    │
                │ Extract • Transform │
                │       • Load        │
                └──────────┬──────────┘
                           │
                           ▼
```

┌───────────────────────────────────────────────────────────┐
│                   PostgreSQL Warehouse                    │
└───────────────────────────────────────────────────────────┘

raw.keystroke_raw
│
├── feature_1
├── feature_2
├── feature_3
├── ...
├── feature_10
└── label

```
    │
    ▼
```

staging.stg_keystrokes
│
├── cleaned_features
├── normalized_features
└── transformed_labels

```
    │
    ▼
```

analytics.user_statistics
│
├── label
├── total_samples
├── avg_feature_1
├── avg_feature_2
└── avg_feature_3

analytics.user_typing_metrics
│
├── avg_feature_1
├── avg_feature_2
├── avg_feature_3
├── avg_feature_4
└── total_records

```
    │
    ▼
```

Analytics Dashboard
│
├── User Statistics
├── Typing Metrics
├── Authentication Trends
└── Data Insights

===========================================================
AUTHENTICATION PIPELINE
=======================

User
│
▼
Streamlit Dashboard
│
▼
FastAPI Backend
│
▼
Feature Processing & Scaling
│
▼

Stacking Ensemble Model
│
├── Random Forest
├── SVM
├── Logistic Regression
│
└── Meta Model

│
▼

Isolation Forest
(Anomaly Detection)

│
▼

Ensemble XAI
│
├── Random Forest Contribution
├── SVM Contribution
└── Logistic Regression Contribution

│
▼

Prediction Result
│
├── Genuine User
├── Suspicious User
├── Confidence Score
└── Anomaly Score
