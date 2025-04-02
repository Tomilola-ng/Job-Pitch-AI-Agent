"""Main module for AI-agent."""

from utils.openai import OpenAIClient


def main():
    """Main function for AI-agent."""
    openai_client = OpenAIClient()
    response = openai_client.chat("Hello, how are you?")
    print(response)


if __name__ == "__main__":
    main()
