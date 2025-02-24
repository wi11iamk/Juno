from utils.logger import Logger
from clustering.clustering_model import ClusteringModel
from reporting.report_generator import generate_cluster_report
from llm_interface.llm_connector import generate_llm_response

logger = Logger()

def main():
    logger.info("Patient Scheduler System Starting.")
    try:
        # Placeholder: Load patient data
        logger.info("Loading patient data.")
        patient_data = None  # Placeholder for actual data loading
        cluster_labels = None  # Placeholder for actual clustering results
        
        # Clustering
        clustering_model = ClusteringModel()
        logger.info("Fitting clustering model.")
        cluster_labels = clustering_model.fit(patient_data)
        logger.info("Clustering complete.")

        # Generate reports
        logger.info("Generating reports.")
        report = generate_cluster_report(patient_data, cluster_labels, override_log=None)
        logger.info("Reports generated successfully.")

        # Test LLM response
        logger.info("Querying LLM for a test response.")
        llm_test_response = generate_llm_response("Explain why clustering helps in rehabilitation.")
        logger.info(f"LLM Test Response: {llm_test_response}")
    
    except Exception as e:
        logger.error(f"System encountered an error: {str(e)}")
    finally:
        logger.info("Patient Scheduler System Shutdown.")

if __name__ == "__main__":
    main()
