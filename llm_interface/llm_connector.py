import openai
from utils.logger import Logger
from utils.config import LLM_API_KEY, LLM_MODEL, LLM_MAX_TOKENS, LLM_TEMPERATURE, LLM_FALLBACK_ON_FAILURE

logger = Logger()

def generate_llm_response(prompt):
    """Uses an external LLM (GPT-4) to generate additional contextual explanations."""
    logger.info("Sending query to LLM API.")
    try:
        response = openai.ChatCompletion.create(
            model=LLM_MODEL,
            messages=[{"role": "system", "content": "Expand on this response in a clinically relevant way."},
                      {"role": "user", "content": prompt}],
            max_tokens=LLM_MAX_TOKENS,
            temperature=LLM_TEMPERATURE,
            api_key=LLM_API_KEY
        )
        logger.info("LLM API response received successfully.")
        return response['choices'][0]['message']['content']
    except Exception as e:
        logger.error(f"LLM API request failed: {str(e)}")
        if LLM_FALLBACK_ON_FAILURE:
            logger.warning("Using structured response fallback.")
            return "[LLM Expansion Unavailable]"
        else:
            return None
