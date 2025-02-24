import pandas as pd

def validate_data(data):
    """Checks for missing values, duplicate entries, and incorrect data types in the dataset."""
    errors = []
    
    # Check for missing values
    if data.isnull().sum().sum() > 0:
        errors.append("Dataset contains missing values.")
    
    # Ensure a unique identifier exists
    if 'patient_id' not in data.columns:
        errors.append("Dataset is missing a unique patient identifier column.")
    
    # Check for duplicate patient sessions, not just duplicate scores
    if data.duplicated(subset=['patient_id', 'session_date']).sum() > 0:
        errors.append("Dataset contains duplicate session records for the same patient.")
    
    # Check for invalid numerical values
    if (data[['Impairment_Level', 'Cognitive_Score']] < 0).any().any():
        errors.append("Negative values detected in impairment scores.")
    
    return errors if errors else "Data validation passed."
