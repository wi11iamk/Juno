import pandas as pd

def create_interaction_features(data):
    """Generates new interaction features based on existing numerical and categorical data."""
    data['Cognitive_Motivation'] = data['Cognitive_Score'] * data['Motivation_Level'].astype('category').cat.codes
    data['Impairment_Support'] = data['Impairment_Level'] * data['Support_System'].astype('category').cat.codes
    return data

def encode_categorical_features(data):
    """Encodes categorical variables for clustering."""
    categorical_features = ['Support_System', 'Communication_Ability', 'Motivation_Level']
    for feature in categorical_features:
        data[feature] = data[feature].astype('category').cat.codes
    return data
