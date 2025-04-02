"""Module for scheduling appointments using Google Calendar API with OAuth 2.0."""

# pylint: disable=line-too-long, no-member, broad-except, unspecified-encoding

import os
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Constants
SCOPES = ['https://www.googleapis.com/auth/calendar']
CLIENT_SECRET_FILE = os.getenv(
    'GOOGLE_CLIENT_SECRET_FILE', 'client_secret.json')
TOKEN_FILE = os.getenv('GOOGLE_TOKEN_FILE', 'token.json')


def schedule_google_appointment(summary: str, start_time: str, end_time: str,
                                description: str = None, attendees: list = None) -> dict:
    """
    Schedules an appointment in Google Calendar using OAuth 2.0.

    Args:
        summary (str): The title of the appointment/event.
        start_time (str): Start time in ISO format (e.g., '2025-04-03T10:00:00-07:00').
        end_time (str): End time in ISO format (e.g., '2025-04-03T11:00:00-07:00').
        description (str, optional): Description of the appointment. Defaults to None.
        attendees (list, optional): List of email addresses for attendees. Defaults to None.

    Returns:
        dict: Response containing the created event details from Google Calendar API.

    Raises:
        ValueError: If required parameters are missing or invalid.
        FileNotFoundError: If client secret file is not found.
        Exception: For other API-related errors.

    Example:
        >>> result = schedule_google_appointment(
        ...     summary="Team Meeting",
        ...     start_time="2025-04-03T10:00:00-07:00",
        ...     end_time="2025-04-03T11:00:00-07:00",
        ...     description="Weekly sync-up",
        ...     attendees=["user1@example.com"]
        ... )
        >>> print(result['id'])  # Prints the event ID
    """
    if not all([summary, start_time, end_time]):
        raise ValueError("Summary, start_time, and end_time are required")

    # Load or generate credentials
    creds = Credentials.from_authorized_user_file(
        TOKEN_FILE, SCOPES) if os.path.exists(TOKEN_FILE) else None
    if not creds or not creds.valid:
        if not os.path.exists(CLIENT_SECRET_FILE):
            raise FileNotFoundError(
                f"Client secret file not found at {CLIENT_SECRET_FILE}")
        flow = InstalledAppFlow.from_client_secrets_file(
            CLIENT_SECRET_FILE, SCOPES)
        creds = flow.run_local_server(port=0)
        with open(TOKEN_FILE, 'w') as token:
            token.write(creds.to_json())

    # Build the service and create the event
    service = build('calendar', 'v3', credentials=creds)
    event = {
        'summary': summary,
        'start': {'dateTime': start_time, 'timeZone': 'UTC'},
        'end': {'dateTime': end_time, 'timeZone': 'UTC'},
        **({'description': description} if description else {}),
        **({'attendees': [{'email': email} for email in attendees]} if attendees else {})
    }

    try:
        return service.events().insert(calendarId='primary', body=event).execute()
    except Exception as error:
        return {'error': f"Failed to schedule appointment: {str(error)}"}
