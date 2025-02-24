def generate_cluster_summary(data, cluster_labels):
    """Creates a text-based summary of each cluster for physicians."""
    data['Cluster'] = cluster_labels
    summaries = {}
    
    for cluster in data['Cluster'].unique():
        cluster_data = data[data['Cluster'] == cluster]
        avg_impairment = cluster_data['Impairment_Level'].mean()
        rehab_focus = determine_rehab_focus(avg_impairment)
        
        summaries[cluster] = f"""
        📌 **Group {cluster}**
        - Patients: {', '.join(map(str, cluster_data['patient_id'].tolist()))}
        - Impairment Level: {cluster_data['Impairment_Level'].min()}-{cluster_data['Impairment_Level'].max()}
        - Key Rehab Focus: {rehab_focus}
        """
    
    return summaries
