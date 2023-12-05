import httplib2
import os
from apiclient import discovery
from oauth2client import client, tools, file

SCOPES = 'https://www.googleapis.com/auth/calendar'
APPLICATION_NAME = 'Google Kalendář Automatizace'

credentials = None
store = file.Storage('token.json')
credentials = store.get()
if not credentials or credentials.invalid:
    flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
    credentials = tools.run_flow(flow, store)
    print('Storing credentials to "token.json"')

http = credentials.authorize(httplib2.Http())
service = discovery.build('calendar', 'v3', http=http)

event_summary = input("Napiště název události: ")
event_description = input("Napište popisek události:  ")
event_start_date = input("Napište datum začátku události v podobě (RRRR-MM-DD): ")
event_start_time = input("Napište čas začátku události v podobě (HH:MM): ")
event_end_date = input("Napište datum konce události v podobě (RRRR-MM-DD): ")
event_end_time = input("Napište čas konce události v podobě (HH:MM):  ")
event_recurrence = input("Napište jak často se bude událost opakovat v angličtině (například DAILY,WEEKLY, MONTHLY): ")
event_interval = input("Napiště kolikrát se má událost opakovat: ")

event_start_time = event_start_time + ":00Z"
event_end_time = event_end_time + ":00Z"

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
print('Událost vytvořena: %s' % event.get('id'))