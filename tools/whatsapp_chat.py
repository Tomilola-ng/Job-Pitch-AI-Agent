"""Module for sending WhatsApp messages using Meta's Cloud API."""

# pylint: disable=line-too-long, missing-timeout, broad-except

import os
from datetime import datetime, timedelta

import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

WHATSAPP_ACCESS_TOKEN = os.getenv('WHATSAPP_ACCESS_TOKEN')
PHONE_NUMBER_ID = os.getenv('WHATSAPP_PHONE_NUMBER_ID')
API_VERSION = 'v22.0'
API_URL = f"https://graph.facebook.com/{API_VERSION}/{PHONE_NUMBER_ID}/messages"


def whatsapp_chat(job_seeker_name: str, target_phone_number: str, target_email: str) -> dict:
    """
    Sends a WhatsApp message to inform about a quotation and get a demo time.

    Args:
        job_seeker_name (str): The name of the job seeker.
        target_phone_number (str): The recipient's phone number (e.g., '+2347013002604').
        target_email (str): The email where the quotation was sent.

    Returns:
        dict: Contains 'datetime' (datetime object) if successful, or 'error' (str) if failed.

    Example:
        >>> result = whatsapp_chat("Tomilola Oluwafemi", "+2347013002604", "tee.o2809@gmail.com")
        >>> print(result.get('datetime', result['error']))
    """
    if not all([job_seeker_name, target_phone_number, target_email]):
        return {"error": "All parameters are required"}
    if not WHATSAPP_ACCESS_TOKEN:
        return {"error": "WHATSAPP_ACCESS_TOKEN must be set in .env"}

    payload = {
        "messaging_product": "whatsapp",
        "to": target_phone_number,
        "type": "template",
        "template": {
            "name": "job_pitch_quotation",
            "language": {"code": "en"},
            "components": [
                {
                    "type": "body",
                    "parameters": [
                        {"type": "text", "text": job_seeker_name},
                        {"type": "text", "text": target_email}
                    ]
                }
            ]
        }
    }

    headers = {
        "Authorization": f"Bearer {WHATSAPP_ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }

    # Debug output
    print(f"Sending to: {API_URL}")
    print(f"Headers: {headers}")
    print(f"Payload: {payload}")

    try:
        response = requests.post(API_URL, json=payload, headers=headers)
        print(f"Response Status: {response.status_code}")
        print(f"Response Text: {response.text}")
        response.raise_for_status()
        # Mock datetime for now (webhook pending)
        demo_time = datetime.now() + timedelta(days=1, hours=10)  # Tomorrow at 10 AM
        return {"datetime": demo_time}
    except requests.RequestException as error:
        return {"error": f"Failed to send message: {str(error)}"}
