import matplotlib.pyplot as plt

def plot_cluster_distribution(data, cluster_labels):
    """Creates a bar chart of impairment levels per cluster."""
    data['Cluster'] = cluster_labels
    cluster_means = data.groupby('Cluster')['Impairment_Level'].mean()
    
    plt.figure(figsize=(8, 5))
    cluster_means.plot(kind='bar', color='blue')
    plt.xlabel("Cluster")
    plt.ylabel("Average Impairment Level")
    plt.title("Impairment Levels Across Clusters")
    plt.show()
