from googleapiclient import discovery
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
import os
import requests
from datetime import datetime

SCOPES = 'https://www.googleapis.com/auth/calendar'
APPLICATION_NAME = 'Google Kalendář Automatizace'

def main():
    creds = None
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(requests.Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                "credentials.json", SCOPES
            )
            creds = flow.run_local_server(port=0)
        with open("token.json", "w") as token:
            token.write(creds.to_json())
    return creds

creds = main()
service = discovery.build('calendar', 'v3', credentials=creds)
event_summary = input("Napiště název události: ")
event_description = input("Napište popisek události:  ")
event_start_date = input("Napište datum začátku události: ")
event_start_time = input("Napište čas začátku události v podobě (HH:MM): ")
event_end_date = input("Napište datum konce události: ")
event_end_time = input("Napište čas konce události v podobě (HH:MM):  ")
event_recurrence = input("Napište jak často se bude událost opakovat (denně, týdně, měsíčně, ročně): ")
event_interval = input("Napiště kolikrát se má událost opakovat: ")

event_start_time = event_start_time + ":00"
event_end_time = event_end_time + ":00"

event_start_date = datetime.strptime(event_start_date, '%d.%m.%Y').strftime('%Y-%m-%d').isoformat()
event_end_date = datetime.strptime(event_end_date, '%d.%m.%Y').strftime('%Y-%m-%d').isoformat()

if event_recurrence == "denně": event_recurrence = "DAILY"
if event_recurrence == "týdně": event_recurrence = "WEEKLY"
if event_recurrence == "měsíčně": event_recurrence = "MONTHLY"
if event_recurrence == "ročně": event_recurrence = "YEARLY"

event = {
        'summary': event_summary,
        'description': event_description,
        'start': {
            'dateTime': event_start_date + "T" + event_start_time,
            'timeZone': 'Europe/Prague'
        },
        'end': {
            'dateTime': event_end_date + "T" + event_end_time,
            'timeZone': 'Europe/Prague'
        },
        'recurrence': [
            'RRULE:FREQ=' + event_recurrence + ';' + 'COUNT=' + event_interval
        ]
    }
event = service.events().insert(calendarId='primary', body=event).execute()
print(f'Událost vytvořena: {event.get("id")}')

if __name__ == "__main__":
=======
from googleapiclient import discovery
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
import os
import requests
from datetime import datetime

SCOPES = 'https://www.googleapis.com/auth/calendar'
APPLICATION_NAME = 'Google Kalendář Automatizace'

def main():
    creds = None
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(requests.Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                "credentials.json", SCOPES
            )
            creds = flow.run_local_server(port=0)
        with open("token.json", "w") as token:
            token.write(creds.to_json())
    return creds

creds = main()
service = discovery.build('calendar', 'v3', credentials=creds)
event_summary = input("Napiště název události: ")
event_description = input("Napište popisek události:  ")
event_start_date = input("Napište datum začátku události: ")
event_start_time = input("Napište čas začátku události v podobě (HH:MM): ")
event_end_date = input("Napište datum konce události: ")
event_end_time = input("Napište čas konce události v podobě (HH:MM):  ")
event_recurrence = input("Napište jak často se bude událost opakovat (denně, týdně, měsíčně, ročně): ")
event_interval = input("Napiště kolikrát se má událost opakovat: ")

event_start_time = event_start_time + ":00"
event_end_time = event_end_time + ":00"

event_start_date = datetime.strptime(event_start_date, '%d.%m.%Y').strftime('%Y-%m-%d').isoformat()
event_end_date = datetime.strptime(event_end_date, '%d.%m.%Y').strftime('%Y-%m-%d').isoformat()

if event_recurrence == "denně": event_recurrence = "DAILY"
if event_recurrence == "týdně": event_recurrence = "WEEKLY"
if event_recurrence == "měsíčně": event_recurrence = "MONTHLY"
if event_recurrence == "ročně": event_recurrence = "YEARLY"

event = {
        'summary': event_summary,
        'description': event_description,
        'start': {
            'dateTime': event_start_date + "T" + event_start_time,
            'timeZone': 'Europe/Prague'
        },
        'end': {
            'dateTime': event_end_date + "T" + event_end_time,
            'timeZone': 'Europe/Prague'
        },
        'recurrence': [
            'RRULE:FREQ=' + event_recurrence + ';' + 'COUNT=' + event_interval
        ]
    }
event = service.events().insert(calendarId='primary', body=event).execute()
print(f'Událost vytvořena: {event.get("id")}')

if __name__ == "__main__":
  main()
