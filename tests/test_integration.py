"""End-to-end integration tests for the patient scheduling system."""
import pytest
from data_processing.data_loader import load_patient_data
from clustering.clustering_model import ClusteringModel
from reporting.report_generator import generate_cluster_report
from llm_interface.query_processor import QueryProcessor
from llm_interface.override_handler import OverrideHandler
from utils.logger import Logger

logger = Logger()

def test_data_loading():
    logger.info("Testing data loading...")
    data = load_patient_data()
    assert data is not None
    assert not data.empty

def test_clustering_pipeline():
    logger.info("Testing clustering pipeline...")
    data = load_patient_data()
    clustering_model = ClusteringModel()
    cluster_labels = clustering_model.fit(data)
    assert cluster_labels is not None
    assert len(cluster_labels) == len(data)

def test_reporting_pipeline():
    logger.info("Testing reporting pipeline...")
    data = load_patient_data()
    clustering_model = ClusteringModel()
    cluster_labels = clustering_model.fit(data)
    report = generate_cluster_report(data, cluster_labels, override_log=None)
    assert report is not None

def test_llm_query():
    logger.info("Testing LLM query...")
    data = load_patient_data()
    clustering_model = ClusteringModel()
    cluster_labels = clustering_model.fit(data)
    query_processor = QueryProcessor(data, cluster_labels)
    response = query_processor.explain_cluster_assignment(patient_id=1)
    assert response is not None

def test_override_system():
    logger.info("Testing override system...")
    data = load_patient_data()
    clustering_model = ClusteringModel()
    cluster_labels = clustering_model.fit(data)
    override_handler = OverrideHandler(data, cluster_labels)
    result = override_handler.override_patient_cluster(patient_id=1, new_cluster=2, reason="Clinical decision")
    assert "moved from" in result
