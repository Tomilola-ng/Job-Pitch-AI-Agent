"""Tests for AI-agent."""

from utils.openai import OpenAIClient


def test_main():
    """Test function for AI-agent."""
    # TODO: Add tests for AI-agent
    print("Testing AI-agent...")
    client = OpenAIClient()
    response = client.chat("Hello!")
    if response:
        print(response)
    print("---\n Done testing AI-agent. \n---")


if __name__ == "__main__":
    test_main()
