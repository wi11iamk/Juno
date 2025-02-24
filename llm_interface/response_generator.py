from llm_interface.llm_connector import generate_llm_response

class ResponseGenerator:
    """Formats and structures LLM responses for clarity and usability."""

    @staticmethod
    def format_patient_cluster_response(response):
        structured_response = f"📌 {response}"
        return structured_response + "\n\n" + generate_llm_response(structured_response)

    @staticmethod
    def format_cluster_summary(summary):
        structured_response = f"\n🔍 **Cluster Summary:**\n{summary}\n"
        return structured_response + "\n" + generate_llm_response(structured_response)

    @staticmethod
    def format_schedule(schedule_df):
        structured_response = f"\n📅 **Rehab Schedule:**\n{schedule_df.to_string(index=False)}\n"
        return structured_response + "\n" + generate_llm_response(structured_response)

    @staticmethod
    def format_explanation(response):
        structured_response = f"\n🧐 **Cluster Assignment Explanation:**\n{response}\n"
        return structured_response + "\n" + generate_llm_response(structured_response)

    @staticmethod
    def format_statistical_summary(summary_df):
        structured_response = f"\n📊 **Cluster Statistics:**\n{summary_df.to_string(index=False)}\n"
        return structured_response + "\n" + generate_llm_response(structured_response)
