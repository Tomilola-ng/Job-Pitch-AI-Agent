"""Tests for AI-agent."""

from datetime import datetime, timedelta

from utils.openai import OpenAIClient
from tools.appointment_scheduler import schedule_google_appointment


def test_main():
    """Test function for AI-agent."""
    print("Testing AI-agent...")
    client = OpenAIClient()
    messages = [
        {"role": "system", "content": "This is a test message."},
        {"role": "user", "content": "Return random informal greeting."}
    ]
    response = client.chat(messages)
    if response:
        print(response)
    print("---\n Done testing AI-agent. \n---")


def test_appointment_scheduling():
    """Test function for appointment scheduling."""

    # Get current time and round up to the next hour
    now = datetime.now()
    next_hour = now.replace(
        minute=0, second=0, microsecond=0) + timedelta(hours=1)
    end_time = next_hour + timedelta(hours=1)

    # Format times in ISO format with timezone
    start_time = next_hour.strftime("%Y-%m-%dT%H:%M:%S-07:00")
    end_time = end_time.strftime("%Y-%m-%dT%H:%M:%S-07:00")

    result = schedule_google_appointment(
        summary="Test Meeting",
        start_time=start_time,
        end_time=end_time,
        description="Cleaned-up test",
        attendees=["test@example.com"]
    )
    print(result.get('id', result))


if __name__ == "__main__":
    test_main()
    test_appointment_scheduling()
