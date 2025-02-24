import pandas as pd

def generate_rehab_schedule(data, cluster_labels):
    """Generates an automated rehab schedule based on clusters."""
    data['Cluster'] = cluster_labels
    schedule = []
    
    time_slots = ["09:00 - 10:00", "10:00 - 11:00", "11:00 - 12:00"]
    locations = ["Gym 1", "Gym 2", "Fine Motor Room"]
    therapists = ["Dr. Smith", "Dr. Lee", "Dr. Patel"]
    
    for i, cluster in enumerate(data['Cluster'].unique()):
        cluster_data = data[data['Cluster'] == cluster]
        rehab_focus = determine_rehab_focus(cluster_data['Impairment_Level'].mean())
        
        schedule.append({
            "Time Slot": time_slots[i % len(time_slots)],
            "Group": cluster,
            "Location": locations[i % len(locations)],
            "Focus": rehab_focus,
            "Lead Therapist": therapists[i % len(therapists)]
        })
    
    return pd.DataFrame(schedule)
