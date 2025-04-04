"""Module for making a simple phone call using Vapi to pitch a service and get demo time."""

# pylint: disable=line-too-long, missing-timeout, broad-except

import os
from datetime import datetime, timedelta

import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Vapi API configuration
VAPI_API_KEY = os.getenv('VAPI_API_KEY')
VAPI_BASE_URL = 'https://api.vapi.ai'
PHONE_NUMBER_ID = os.getenv('VAPI_PHONE_NUMBER_ID')


def phone_caller(job_seeker_name: str, target_phone_number: str, target_email: str) -> dict:
    """
    Makes a phone call to inform about a quotation and get a demo appointment time.

    Args:
        job_seeker_name (str): The name of the job seeker (used in the pitch).
        target_phone_number (str): The phone number to call (e.g., '+12345678901').
        target_email (str): The email where the quotation was sent.

    Returns:
        dict: Contains 'datetime' (datetime object) if successful, or 'error' (str) if failed.

    Raises:
        ValueError: If required parameters or Vapi credentials are missing.

    Example:
        >>> result = phone_caller(
        ...     job_seeker_name="Tomilola Oluwafemi",
        ...     target_phone_number="+2347-13002667",
        ...     target_email="client@example.com"
        ... )
        >>> if 'datetime' in result:
        ...     print(result['datetime'])  # e.g., 2025-04-03 10:00:00
        ... else:
        ...     print(result['error'])
    """
    # Validate inputs
    if not all([job_seeker_name, target_phone_number, target_email]):
        raise ValueError(
            "job_seeker_name, target_phone_number, and target_email are required")
    if not VAPI_API_KEY or not PHONE_NUMBER_ID:
        raise ValueError(
            "VAPI_API_KEY and VAPI_PHONE_NUMBER_ID must be set in .env")

    # Simple prompt for the call
    prompt = (
        f"Hello! I’m calling on behalf of {job_seeker_name} from Job Pitch AI. "
        f"We’ve prepared a quotation showing how our service can boost your hiring success by connecting you with top talent like {job_seeker_name}. "
        f"It’s been sent to {target_email}—please check it out! "
        "To explore this further, we’d love to schedule a quick demo. When are you free in the next few days? "
        "Please respond with a specific date and time"
    )

    # Vapi API payload
    payload = {
        "assistant": {
            "model": {
                "provider": "openai",
                "model": "gpt-4",
                "messages": [{"role": "system", "content": prompt}]
            },
            "voice": {
                "provider": "11labs",
                "voiceId": "default"
            },
            "firstMessage": prompt
        },
        "phoneNumberId": PHONE_NUMBER_ID,
        "customer": {
            "number": target_phone_number
        }
    }

    # API headers
    headers = {
        "Authorization": f"Bearer {VAPI_API_KEY}",
        "Content-Type": "application/json"
    }

    try:
        # Initiate the call
        response = requests.post(
            f"{VAPI_BASE_URL}/call", json=payload, headers=headers)
        response.raise_for_status()
        call_data = response.json()

        print(call_data)

        # For MVP simplicity, assume the recipient responds with a time during the call
        # In a real scenario, you'd need to fetch the call transcript later via Vapi's API
        # Here, we’ll simulate a response (replace with actual logic later if needed)
        # For now, return a placeholder datetime 2 days from now at 10 AM
        demo_time = datetime.now() + timedelta(days=2)
        demo_time = demo_time.replace(
            hour=10, minute=0, second=0, microsecond=0)

        return {"datetime": demo_time}
    except requests.RequestException as error:
        return {"error": f"Failed to initiate call: {str(error)}"}
    except Exception as error:
        return {"error": f"Unexpected error: {str(error)}"}
