from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

from django.core.management.base import BaseCommand
from django.db.models import Q
from publishing_projects.models import PublishingProgram, Project, Subject, PublicationType
from pprint import pprint as pp
import lxml.etree as ET
import os

class Command(BaseCommand):
    help = "Describe the Command Here"

    def handle(self, **options):
        #for collection in Collection.objects.filter(harvest_type='OAC'):
        #    process_collection(collection)
        print("hey!~!")
        main()

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

# The ID and range of a sample spreadsheet.
# https://docs.google.com/spreadsheets/d/17Md7PxQ34ZGBE2geHV2lpnA0bPurIVejbE4IgldmuFI/edit#gid=139692784
SAMPLE_SPREADSHEET_ID = '17Md7PxQ34ZGBE2geHV2lpnA0bPurIVejbE4IgldmuFI'
SAMPLE_RANGE_NAME = 'All publications!A:Y'

def main():
    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time. 
    dir_path = os.path.dirname(os.path.realpath(__file__))
    tpfile = os.path.join(dir_path, 'token.pickle')
    if os.path.exists(tpfile):
        with open(tpfile, 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open(tpfile, 'wb') as token:
            pickle.dump(creds, token)

    service = build('sheets', 'v4', credentials=creds)

    # Call the Sheets API
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                range=SAMPLE_RANGE_NAME,
                                valueRenderOption='FORMATTED_VALUE',).execute()
    values = result.get('values', [])

    if not values:
        print('No data found.')
    else:
        for row in values[1:]:
            # eat the two off the back
            row.pop()
            row.pop()
            # ['Unit_ID'0 'Project_ID'1 'Unit + Campus'2 'Unit'3 'Campus'4 'Publication'5 'Type'6 'Other?'7 'Publisher/Platform'8 'Owned ', 'ISSN', 'ISBN', 'Open Access Y/N', 'Cost, if not', 'Website', 'Department 1', 'Department 2']
            # Print columns A and E, which correspond to indices 0 and 4.
            unit_id = row.pop(0)
            
            project_id = row.pop(0)
            # skip 2, 3
            row.pop(0)
            row.pop(0)
            campus = row.pop(0)
            publication = row.pop(0) # 5
            type_v = row.pop(0) #6
            other_v = row.pop(0) #7
            type_s = type_v if type_v != 'Other' else other_v
            publisher_platform = row.pop(0).replace('\n', ' ¶ ') #8
            subjects = row.pop(-2)
            notes = '\n\r'.join(row)
            url = row[5].partition('\n')[0]
            print(row)
            parent_program = PublishingProgram.objects.get(id=unit_id)
            project_type = PublicationType.objects.get_or_create(name=type_s)[0]
            add_this_row(project_id, parent_program, project_type, publication, url, notes, publisher_platform, subjects)


def add_this_row(project_id, program, publication_type, publication_name, url, notes, publishing_partner, subjects):
        this_row = Project.objects.get_or_create(id=project_id,
                                          program=program,
                                          publication_type=publication_type,
                                          publication_name=publication_name,
                                          publishing_partner=publishing_partner,
                                          url=url,
                                          notes=notes)[0]
        for s in subjects.split(','):
            clean_name = s.strip()
            if clean_name:
                ss = Subject.objects.get_or_create(name=s.strip())[0]
                this_row.subject.add(ss)


if __name__ == '__main__':
    main()
