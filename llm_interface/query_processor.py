import pandas as pd
from reporting.report_generator import generate_cluster_report
from reporting.summary_generator import generate_cluster_summary
from reporting.schedule_generator import generate_rehab_schedule

class QueryProcessor:
    """Handles structured LLM queries for retrieving patient, cluster, and schedule data."""

    def __init__(self, patient_data, cluster_labels):
        self.patient_data = patient_data.copy()
        self.cluster_labels = cluster_labels
        self.patient_data['Cluster'] = cluster_labels
        self.cluster_report, self.override_summary = generate_cluster_report(self.patient_data, cluster_labels)
        self.cluster_summary = generate_cluster_summary(self.patient_data, cluster_labels)
        self.schedule = generate_rehab_schedule(self.patient_data, cluster_labels)

    def get_patient_cluster(self, patient_id):
        """Returns the cluster assignment for a specific patient."""
        patient = self.patient_data[self.patient_data['patient_id'] == patient_id]
        if not patient.empty:
            return f"Patient {patient_id} is assigned to Cluster {patient.iloc[0]['Cluster']}."
        return f"Patient {patient_id} not found."

    def get_cluster_summary(self, cluster_id):
        """Returns a structured summary for a specific cluster."""
        return self.cluster_summary.get(cluster_id, "Cluster not found.")

    def get_rehab_schedule(self):
        """Returns the automatically generated rehab schedule."""
        return self.schedule

    def explain_cluster_assignment(self, patient_id):
        """Explains why a patient was grouped into a specific cluster."""
        patient = self.patient_data[self.patient_data['patient_id'] == patient_id]
        if not patient.empty:
            cluster_id = patient.iloc[0]['Cluster']
            summary = self.cluster_summary.get(cluster_id, "No summary available.")
            return f"Patient {patient_id} was assigned to Cluster {cluster_id} because:\n{summary}"
        return f"Patient {patient_id} not found."

    def get_statistical_summary(self):
        """Provides high-level stats about cluster composition."""
        return self.cluster_report, self.override_summary
