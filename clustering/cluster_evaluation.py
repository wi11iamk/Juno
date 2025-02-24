from sklearn.metrics import silhouette_score, davies_bouldin_score
import numpy as np
from scipy.spatial.distance import pdist, squareform

def evaluate_clusters(gower_dist, cluster_labels):
    """Evaluates clustering quality using silhouette, Davies-Bouldin, and Dunn Index."""
    silhouette_avg = silhouette_score(gower_dist, cluster_labels, metric='precomputed')
    db_index = davies_bouldin_score(gower_dist, cluster_labels)
    dunn_index = compute_dunn_index(gower_dist, cluster_labels)
    
    return {
        "silhouette_score": silhouette_avg,
        "davies_bouldin_index": db_index,
        "dunn_index": dunn_index
    }

def compute_dunn_index(gower_dist, cluster_labels):
    """Computes the Dunn Index for clustering quality assessment."""
    cluster_list = np.unique(cluster_labels)
    inter_cluster_distances = []
    intra_cluster_distances = []
    
    for cluster in cluster_list:
        cluster_points = np.where(cluster_labels == cluster)[0]
        if len(cluster_points) > 1:
            intra_dists = pdist(gower_dist[np.ix_(cluster_points, cluster_points)], metric='euclidean')
            intra_cluster_distances.append(np.max(intra_dists))
    
    for i, cluster_a in enumerate(cluster_list):
        for cluster_b in cluster_list[i + 1:]:
            points_a = np.where(cluster_labels == cluster_a)[0]
            points_b = np.where(cluster_labels == cluster_b)[0]
            inter_dists = pdist(gower_dist[np.ix_(points_a, points_b)], metric='euclidean')
            inter_cluster_distances.append(np.min(inter_dists))
    
    if len(inter_cluster_distances) == 0 or len(intra_cluster_distances) == 0:
        return float('inf')  # Avoid division by zero
    
    return np.min(inter_cluster_distances) / np.max(intra_cluster_distances)
