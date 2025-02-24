import pandas as pd
from utils.logger import Logger

logger = Logger()

def generate_cluster_report(data, cluster_labels, override_log):
    """Generates a tabular report summarizing patient clusters, including override tracking."""
    logger.info("Generating cluster report.")
    data['Cluster'] = cluster_labels
    data = data.merge(override_log, on='patient_id', how='left')
    data['Override_Applied'] = data['Old_Cluster'].notna()
    report = data.groupby('Cluster').agg(
        Patient_Count=('patient_id', 'count'),
        Impairment_Range=('Impairment_Level', lambda x: f"{x.min()}-{x.max()}"),
        Primary_Rehab_Focus=('Impairment_Level', lambda x: determine_rehab_focus(x.mean())),
        Overrides_Applied=('Override_Applied', 'sum')
    ).reset_index()
    logger.info("Cluster report generation complete.")
    return report
