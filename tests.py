"""Tests for AI-agent."""

from datetime import datetime, timedelta

from utils.openai import OpenAIClient
from tools.appointment_scheduler import schedule_google_appointment
from tools.pitch_writer import generate_pitch
from tools.phone_caller import phone_caller
from tools.whatsapp_chat import whatsapp_chat


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


def test_pitch_writer():
    """Test function for pitch writer."""
    print("Testing pitch writer...")

    pitch = generate_pitch(
        job_seeker_name="Tomilola Oluwafemi",
        job_description="AI Agent Developer: Develop scalable AI-agent using Python...",
        company_name="FinTech Solutions"
    )
    print(pitch)


def test_phone_caller():
    """Test function for phone caller."""
    print("Testing phone caller...")
    # Note: Replace the phone number with a valid test number
    result = phone_caller(
        job_seeker_name="Tomilola Oluwafemi",
        target_phone_number="+2347055708314",
        target_email="mulumbadeborah02@gmail.com"
    )
    if 'datetime' in result:
        print(f"Demo scheduled for: {result['datetime']}")
    else:
        print(result['error'])


def test_whatsapp_chat():
    """Test function for WhatsApp chat."""
    print("Testing WhatsApp chat...")
    result = whatsapp_chat(
        job_seeker_name="Tomilola Oluwafemi",
        target_phone_number="+2347013002604",
        target_email="tee.o2809@gmail.com"
    )
    print(result.get('datetime', result.get('error')))


if __name__ == "__main__":
    # test_main()
    # test_appointment_scheduling()
    # test_pitch_writer()
    # test_phone_caller()
    test_whatsapp_chat()
