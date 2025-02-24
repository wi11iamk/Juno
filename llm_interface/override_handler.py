import pandas as pd
from datetime import datetime

class OverrideHandler:
    """Handles structured physician overrides for patient assignments with validation."""

    def __init__(self, patient_data, cluster_labels):
        self.patient_data = patient_data.copy()
        self.cluster_labels = cluster_labels
        self.patient_data['Cluster'] = cluster_labels
        self.override_log = pd.DataFrame(columns=['patient_id', 'Old_Cluster', 'New_Cluster', 'Reason', 'Timestamp'])

    def override_patient_cluster(self, patient_id, new_cluster, reason):
        """Reassigns a patient to a new cluster, ensuring validation is followed, and logs the reason."""
        if patient_id not in self.patient_data['patient_id'].values:
            return f"Patient {patient_id} not found. Override not applied."
        
        old_cluster = self.patient_data.loc[self.patient_data['patient_id'] == patient_id, 'Cluster'].values[0]
        validation_result = self.validate_override(patient_id, new_cluster)
        
        if validation_result != "Override validated and applied.":
            return validation_result
        
        self.patient_data.loc[self.patient_data['patient_id'] == patient_id, 'Cluster'] = new_cluster
        self.override_log = pd.concat([
            self.override_log,
            pd.DataFrame.from_records([{
                'patient_id': patient_id,
                'Old_Cluster': old_cluster,
                'New_Cluster': new_cluster,
                'Reason': reason,
                'Timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }])
        ], ignore_index=True)
        return f"Patient {patient_id} moved from Cluster {old_cluster} to Cluster {new_cluster}. Reason: {reason}"

    def validate_override(self, patient_id, new_cluster):
        """Validates if an override request is clinically appropriate."""
        if new_cluster not in self.patient_data['Cluster'].unique():
            return f"Cluster {new_cluster} does not exist. Override rejected."

        patient_impairment = self.patient_data.loc[self.patient_data['patient_id'] == patient_id, 'Impairment_Level'].values[0]
        new_cluster_impairment_range = self.patient_data[self.patient_data['Cluster'] == new_cluster]['Impairment_Level']
        
        if new_cluster_impairment_range.empty:
            return "New cluster has no patients yet. Override allowed."

        avg_impairment = new_cluster_impairment_range.mean()
        max_deviation = new_cluster_impairment_range.std() * 1.5

        if abs(patient_impairment - avg_impairment) > max_deviation:
            return f"Override rejected: Patient {patient_id} has an impairment score of {patient_impairment}, which is too different from Cluster {new_cluster}'s average ({avg_impairment:.2f})."

        return "Override validated and applied."

    def get_override_log(self):
        """Returns a structured log of all overrides applied."""
        return self.override_log
