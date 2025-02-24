"""Unit tests for override handling functions."""
import pytest
import pandas as pd
from llm_interface.override_handler import OverrideHandler

@pytest.fixture
def sample_data():
    return pd.DataFrame({
        'patient_id': [1, 2, 3, 4, 5],
        'Cluster': [0, 1, 0, 1, 0]
    })

def test_override_patient_cluster(sample_data):
    override_handler = OverrideHandler(sample_data, sample_data['Cluster'])
    result = override_handler.override_patient_cluster(patient_id=1, new_cluster=2, reason="Clinical decision")
    assert "moved from" in result

def test_invalid_override(sample_data):
    override_handler = OverrideHandler(sample_data, sample_data['Cluster'])
    result = override_handler.override_patient_cluster(patient_id=10, new_cluster=2, reason="Invalid patient")
    assert result == "Patient not found"
