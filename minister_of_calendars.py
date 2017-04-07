import datetime

from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client.service_account import ServiceAccountCredentials

CALENDAR_ID = 'slean2j66d8bulngt6sfr7j874@group.calendar.google.com'

def main():
    scopes = ['https://www.googleapis.com/auth/calendar']
    credentials = ServiceAccountCredentials.from_json_keyfile_name(
        './SatStalkerPredictor.json',
        scopes
    )

    http_auth = credentials.authorize(Http())

    service = build('calendar', 'v3', http=http_auth)

    event = {
        'summary': 'NOAA-XX',
        'location': 'Des Moines, IA',
        'description': 'Satellite Frequency Goes Here',
        'start': {
            'dateTime': '2017-04-07T09:00:00',
            'timeZone': 'America/Chicago'
        },
        'end': {
            'dateTime': '2017-04-07T09:07:43',
            'timeZone': 'America/Chicago'
        }
    }

    new_event = service.events().insert(
        calendarId=CALENDAR_ID,
        body=event
    ).execute()

    print new_event['status']

if __name__ == '__main__':
    main()
