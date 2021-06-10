#import pandas as pd
import requests
import xml.etree.ElementTree as ET
from google.oauth2 import service_account
from googleapiclient.discovery import build


link_armenia = "http://tarea-4.2021-1.tallerdeintegracion.cl/gho_ARM.xml"
# link_tanzania = "http://tarea-4.2021-1.tallerdeintegracion.cl/gho_TZA.xml"
# link_azerbaiyan = "http://tarea-4.2021-1.tallerdeintegracion.cl/gho_AZE.xml"
# link_australia = "http://tarea-4.2021-1.tallerdeintegracion.cl/gho_AUS.xml"
# link_jamaica = "http://tarea-4.2021-1.tallerdeintegracion.cl/gho_JAM.xml"
# link_kenia = "http://tarea-4.2021-1.tallerdeintegracion.cl/gho_KEN.xml"

# death_index = ["Number of deaths", "Number of infant deaths"]

# resp_armenia = requests.get(link_armenia)
# # print(resp_armenia.content)
# tree = ET.fromstring(resp_armenia.content)
# result = []

# for row in tree.findall('Fact'):
#     gho = row.find('GHO').text

#     if gho in death_index:

#         try:
#             country = row.find('COUNTRY').text
#             sex = row.find('SEX').text
#             year = row.find('YEAR').text
#             ghecauses = row.find('GHECAUSES').text
#             agegroup = row.find('AGEGROUP').text
#             display = row.find('Display').text
#             numeric = row.find('Numeric').text
#             low = row.find('Low').text
#             high = row.find('High').text
#             result = [gho, country, year, ghecauses,
#                       agegroup, display, numeric, low, high]
#             print(result)

#         except:
#             pass


SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
SERVICE_ACCOUNT_FILE = 't4_keys.json'

creds = None
creds = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)

SAMPLE_SPREADSHEET_ID = '1thuNzDZjTp4vuKn6oe-pYTtgIH_hl2Km2rRHIzBLYvs'
service = build('sheets', 'v4', credentials=creds)

# Call the Sheets API
sheet = service.spreadsheets()
result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                            range="datos!A1:G16").execute()

list_ex = [["a", "b"],[1, 2]]
values = result.get('values', [])

writing = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID, range="datos!A2", valueInputOption="USER_ENTERED", body={"values":list_ex}).execute()
print(writing)

