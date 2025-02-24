import pandas as pd
import numpy as np

def preprocess_data(data):
    """Cleans missing values, encodes categorical variables, normalizes numerical features, and detects outliers."""
    numerical_features = ['Impairment_Level', 'Cognitive_Score']
    categorical_features = ['Support_System', 'Communication_Ability', 'Motivation_Level']
    
    # Handle missing values
    data[numerical_features] = data[numerical_features].fillna(data[numerical_features].mean())
    data[categorical_features] = data[categorical_features].fillna(data[categorical_features].mode().iloc[0])
    
    # Detect and handle outliers using z-score
    z_scores = np.abs((data[numerical_features] - data[numerical_features].mean()) / data[numerical_features].std())
    data = data[(z_scores < 3).all(axis=1)]  # Remove rows where any numerical feature has a z-score > 3
    
    # Normalize numerical features
    data[numerical_features] = (data[numerical_features] - data[numerical_features].min()) / (data[numerical_features].max() - data[numerical_features].min())
    
    return data
