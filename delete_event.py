import os
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build

SCOPES = 'https://www.googleapis.com/auth/calendar'

def delete_event():
    creds = None
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
            creds = flow.run_local_server(port=0)
        with open("token.json", "w") as token:
            token.write(creds.to_json())
    return creds
creds = delete_event()
service = build("calendar", "v3", credentials=creds)      
event_id = input("Napište ID události, kterou chcete smazat: ")

service.events().delete(calendarId='primary', eventId=event_id).execute()
print("Událost byla úspěšně smazána.")