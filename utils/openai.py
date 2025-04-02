"""Module for interacting with the OpenAI API."""

import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Constants
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
MODEL = "gpt-4o"

if not OPENAI_API_KEY:
    raise ValueError(
        "Missing OpenAI API key. Please set OPENAI_API_KEY in .env file.")


class OpenAIClient:
    """Handles interaction with OpenAI API."""

    def __init__(self):
        """Initializes the OpenAIClient with the given API key."""
        self.client = OpenAI(api_key=OPENAI_API_KEY)

    def chat(self, prompt: str) -> str:
        """Generates a response from the OpenAI API based on the provided prompt.

        Args:
            prompt (str): The user's input prompt.

        Returns:
            str: The response from the AI model.
        """
        try:
            response = self.client.chat.completions.create(
                model=MODEL,
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": prompt},
                ],
                temperature=0.5,
            )
            return response.choices[0].message.content
        except Exception as error:  # pylint: disable=broad-except
            return f"Error occurred: {error}"
