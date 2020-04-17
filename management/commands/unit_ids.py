from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

from django.core.management.base import BaseCommand
from django.db.models import Q
from publishing_projects.models import PublishingProgram, Campus
from pprint import pprint as pp
import lxml.etree as ET
import os


class Command(BaseCommand):
    help = "Describe the Command Here"

    def handle(self, **options):
        # for collection in Collection.objects.filter(harvest_type='OAC'):
        #    process_collection(collection)
        print("hey!~!")
        main()


# If modifying these scopes, delete the file token.pickle.
SCOPES = ["https://www.googleapis.com/auth/spreadsheets.readonly"]

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = "1VR8oaSEBngcewZ7LElewyInsbDNo4dAgVkm1QD_EZm4"
SAMPLE_RANGE_NAME = "All publications!A:U"

# https://docs.google.com/spreadsheets/d/17Md7PxQ34ZGBE2geHV2lpnA0bPurIVejbE4IgldmuFI/edit#gid=139692784

SAMPLE_SPREADSHEET_ID = "17Md7PxQ34ZGBE2geHV2lpnA0bPurIVejbE4IgldmuFI"
SAMPLE_RANGE_NAME = "Unit_IDs!A:B"


def main():
    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    dir_path = os.path.dirname(os.path.realpath(__file__))
    tpfile = os.path.join(dir_path, "token.pickle")
    print(tpfile)
    if os.path.exists(tpfile):
        with open(tpfile, "rb") as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open(tpfile, "wb") as token:
            pickle.dump(creds, token)

    service = build("sheets", "v4", credentials=creds)

    # Call the Sheets API
    sheet = service.spreadsheets()
    result = (
        sheet.values()
        .get(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=SAMPLE_RANGE_NAME)
        .execute()
    )
    values = result.get("values", [])

    if not values:
        print("No data found.")
    else:
        for row in values:
            # Print columns A and E, which correspond to indices 0 and 4.
            one = row[0]
            two = row[1]
            name = one.rsplit("-", 1)[0]
            try:
                campus = one.rsplit("-", 1)[1]
                camp = Campus.objects.get_or_create(name=campus)
                program = PublishingProgram.objects.create(id=two, name=one)
                program.campus.add(camp[0])

            except IndexError:
                campus = ""
            print(f"{two}\t{campus}\t{name}")
            # print('%s, %s' % (row[0], row[4]))


if __name__ == "__main__":
    main()
