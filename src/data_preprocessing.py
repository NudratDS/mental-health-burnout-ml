"""
Data preprocessing functions
Mental Health in Tech Survey
"""

import pandas as pd

def load_data(path):
    return pd.read_csv(path)

def clean_data(df):
    df["Age"] = df["Age"].fillna(df["Age"].median())
    return df
  """
XGBoost training pipeline
"""

from xgboost import XGBClassifier

def build_model():
    model = XGBClassifier(
        n_estimators=400,
        learning_rate=0.05,
        max_depth=6,
        random_state=42
    )
    return model 
