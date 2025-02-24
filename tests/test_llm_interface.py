"""Unit tests for LLM interface functions."""
import pytest
from unittest.mock import patch
from llm_interface.llm_connector import generate_llm_response

@patch("llm_interface.llm_connector.openai.ChatCompletion.create")
def test_generate_llm_response(mock_openai):
    mock_openai.return_value = {"choices": [{"message": {"content": "Test response"}}]}
    response = generate_llm_response("Explain clustering.")
    assert response == "Test response"

def test_llm_fallback():
    with patch("llm_interface.llm_connector.openai.ChatCompletion.create", side_effect=Exception("API failure")):
        response = generate_llm_response("Explain clustering.")
        assert response == "[LLM Expansion Unavailable]"
