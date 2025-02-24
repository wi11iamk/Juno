import pandas as pd
from sklearn.cluster import AgglomerativeClustering
from utils.logger import Logger
from utils.config import DEFAULT_CLUSTERING_METHOD, MAX_CLUSTERS

logger = Logger()

class ClusteringModel:
    """Handles patient clustering using hierarchical methods."""
    def __init__(self, method=DEFAULT_CLUSTERING_METHOD, n_clusters=MAX_CLUSTERS):
        self.method = method
        self.n_clusters = n_clusters
        self.model = None
        logger.info(f"Initialized clustering model with method: {self.method}, max clusters: {self.n_clusters}")

    def fit(self, data):
        """Fits the clustering model to the patient data."""
        if self.method == "hierarchical":
            self.model = AgglomerativeClustering(n_clusters=self.n_clusters)
        else:
            logger.error(f"Clustering method {self.method} not supported.")
            raise ValueError(f"Unsupported clustering method: {self.method}")
        
        logger.info("Starting clustering fit.")
        self.model.fit(data)
        logger.info("Clustering fit completed successfully.")
        return self.model.labels_

    def predict(self, data):
        """Hierarchical clustering does not support prediction, so return existing labels."""
        if self.model is None:
            logger.error("Model has not been fitted yet.")
            raise ValueError("Model must be fitted before predicting.")
        return self.model.labels_
