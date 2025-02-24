import pandas as pd
from sklearn.preprocessing import MinMaxScaler, StandardScaler, RobustScaler
from utils.config import NUMERIC_SCALING_METHOD

class DataUtils:
    """Helper functions for data processing such as scaling and encoding."""

    @staticmethod
    def handle_missing_values(data, method="impute"):
        """Handles missing values in a dataset using the specified method."""
        if method == "impute":
            data.fillna(data.median(), inplace=True)
        elif method == "drop":
            data.dropna(inplace=True)
        elif method == "flag":
            data["missing_flag"] = data.isnull().sum(axis=1)
        return data

    @staticmethod
    def scale_numeric_features(data, features):
        """Scales numerical features based on the specified method."""
        scaler = None
        if NUMERIC_SCALING_METHOD == "min-max":
            scaler = MinMaxScaler()
        elif NUMERIC_SCALING_METHOD == "standard":
            scaler = StandardScaler()
        elif NUMERIC_SCALING_METHOD == "robust":
            scaler = RobustScaler()
        
        if scaler:
            data[features] = scaler.fit_transform(data[features])
        return data

    @staticmethod
    def encode_categorical_features(data, categorical_columns, method="label"):
        """Encodes categorical features using label or one-hot encoding."""
        if method == "label":
            for col in categorical_columns:
                data[col] = data[col].astype("category").cat.codes
        elif method == "one-hot":
            data = pd.get_dummies(data, columns=categorical_columns)
        return data
