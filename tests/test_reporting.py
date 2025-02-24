"""Unit tests for reporting functions."""
import pytest
import pandas as pd
from reporting.report_generator import generate_cluster_report

@pytest.fixture
def sample_data():
    return pd.DataFrame({
        'patient_id': [1, 2, 3, 4, 5],
        'Cluster': [0, 1, 0, 1, 0],
        'Impairment_Level': [30, 40, 50, 60, 70]
    })

@pytest.fixture
def override_log():
    return pd.DataFrame({
        'patient_id': [2],
        'Old_Cluster': [0],
        'New_Cluster': [1],
        'Reason': ["Clinical decision"],
        'Timestamp': ["2025-02-21 12:00:00"]
    })

def test_generate_cluster_report(sample_data, override_log):
    report = generate_cluster_report(sample_data, sample_data['Cluster'], override_log)
    assert report is not None
    assert 'Patient_Count' in report.columns
    assert 'Overrides_Applied' in report.columns
