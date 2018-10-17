import gspread
import os.path
import sys
from oauth2client.service_account import ServiceAccountCredentials
import pprint

client_secret = 'client-secret.json'

def get_client():
    scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name(client_secret, scope)
    client = gspread.authorize(creds)

    return client

def get_all(sheet):
    results = sheet.get_all_records()
    return results

def main():
    if not os.path.isfile(client_secret):
        print('Client secret not found. Create one here: https://console.developers.google.com/apis')
        sys.exit(1)

    client = get_client()
    sheet = client.open('grocery_list').sheet1

    results = get_all(sheet)
    pp = pprint.PrettyPrinter()
    pp.pprint(results)

    #last_id = results[-1].get('id')
    last_id = 0
    sheet.insert_row([(int(last_id) + 1), 1, 'food', 'Mango'], len(results) + 2)

if __name__ == '__main__':
    main()