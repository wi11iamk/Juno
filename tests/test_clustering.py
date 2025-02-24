"""Unit tests for clustering model."""
import pytest
import pandas as pd
from clustering.clustering_model import ClusteringModel

@pytest.fixture
def sample_data():
    return pd.DataFrame({
        'feature_1': [1.0, 2.0, 3.0, 4.0, 5.0],
        'feature_2': [10.0, 20.0, 30.0, 40.0, 50.0]
    })

def test_clustering_model_initialization():
    model = ClusteringModel()
    assert model.method is not None
    assert model.n_clusters > 0

def test_clustering_model_fit(sample_data):
    model = ClusteringModel()
    labels = model.fit(sample_data)
    assert labels is not None
    assert len(labels) == len(sample_data)
