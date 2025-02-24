from utils.logger import Logger

logger = Logger()

def update_clusters(patient_data, clustering_model):
    """Dynamically updates patient clusters as new data arrives."""
    try:
        logger.info("Updating patient clusters with new data.")
        new_labels = clustering_model.fit(patient_data)
        logger.info("Cluster update completed successfully.")
        return new_labels
    except Exception as e:
        logger.error(f"Error during dynamic cluster update: {str(e)}")
        return None
