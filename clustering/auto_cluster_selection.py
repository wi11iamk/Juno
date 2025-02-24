import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import linkage
from sklearn.metrics import silhouette_score
from scipy.cluster.hierarchy import fcluster

def optimal_num_clusters(gower_dist, max_clusters=10):
    """Determines the optimal number of clusters using the Silhouette Score."""
    best_score = -1
    best_k = 2  # Minimum possible number of clusters
    
    for k in range(2, max_clusters + 1):
        Z = linkage(gower_dist, method='ward')
        cluster_labels = fcluster(Z, k, criterion='maxclust')
        silhouette_avg = silhouette_score(gower_dist, cluster_labels, metric='precomputed')
        
        if silhouette_avg > best_score:
            best_score = silhouette_avg
            best_k = k
    
    return best_k
