"""Unit tests for data processing functions."""
import pytest
import pandas as pd
from utils.data_utils import DataUtils

@pytest.fixture
def sample_data():
    return pd.DataFrame({
        'numeric_feature': [10, 20, None, 40, 50],
        'categorical_feature': ['A', 'B', 'A', None, 'C']
    })

def test_handle_missing_values(sample_data):
    processed_data = DataUtils.handle_missing_values(sample_data, method="impute")
    assert processed_data.isnull().sum().sum() == 0

def test_scale_numeric_features(sample_data):
    processed_data = DataUtils.scale_numeric_features(sample_data, ['numeric_feature'])
    assert processed_data['numeric_feature'].max() <= 1

def test_encode_categorical_features(sample_data):
    encoded_data = DataUtils.encode_categorical_features(sample_data, ['categorical_feature'], method="label")
    assert encoded_data['categorical_feature'].dtype == 'int8'
