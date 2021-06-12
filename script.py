#import pandas as pd
import requests
import xml.etree.ElementTree as ET
from google.oauth2 import service_account
from googleapiclient.discovery import build


def sort_alpha(data):
    sorted_list = sorted(data)
    for gho in sorted_list:
        print(gho)


link_armenia = "http://tarea-4.2021-1.tallerdeintegracion.cl/gho_ARM.xml"
link_tanzania = "http://tarea-4.2021-1.tallerdeintegracion.cl/gho_TZA.xml"
link_azerbaiyan = "http://tarea-4.2021-1.tallerdeintegracion.cl/gho_AZE.xml"
link_australia = "http://tarea-4.2021-1.tallerdeintegracion.cl/gho_AUS.xml"
link_jamaica = "http://tarea-4.2021-1.tallerdeintegracion.cl/gho_JAM.xml"
link_kenia = "http://tarea-4.2021-1.tallerdeintegracion.cl/gho_KEN.xml"

headers = [["GHO", "COUNTRY", "SEX", "YEAR", "GHECAUSES",
           "AGEGROUP", "Display", "Numeric", "Low", "High"]]

gho_index = ["Number of deaths", "Number of infant deaths",
             "Number of under-five deaths", "Mortality rate for 5-14 year-olds (probability of dying per 1000 children aged 5-14 years)",
             "Adult mortality rate (probability of dying between 15 and 60 years per 1000 population)",
             "Estimates of number of homicides", "Crude suicide rates (per 100 000 population)",
             "Mortality rate attributed to unintentional poisoning (per 100 000 population)",
             "Number of deaths attributed to non-communicable diseases, by type of disease and sex",
             "Estimated road traffic death rate (per 100 000 population)", "Estimated number of road traffic deaths",
             "Mean BMI (kg/m&#xb2;) (crude estimate)", "Mean BMI (kg/m&#xb2;) (age-standardized estimate)",
             "Prevalence of obesity among adults, BMI &GreaterEqual; 30 (age-standardized estimate) (%)",
             "Prevalence of obesity among children and adolescents, BMI > +2 standard deviations above the median (crude estimate) (%)",
             "Prevalence of overweight among adults, BMI &GreaterEqual; 25 (crude estimate) (%)",
             "Prevalence of overweight among children and adolescents, BMI > +1 standard deviations above the median (crude estimate) (%)",
             "Prevalence of underweight among adults, BMI < 18.5 (age-standardized estimate) (%)",
             "Prevalence of thinness among children and adolescents, BMI < -2 standard deviations below the median (crude estimate) (%)",
             "Alcohol, recorded per capita (15+) consumption (in litres of pure alcohol)",
             "Estimate of daily cigarette smoking prevalence (%)", "Estimate of daily tobacco smoking prevalence (%)",
             "Estimate of current cigarette smoking prevalence (%)", "Estimate of current tobacco smoking prevalence (%)",
             "Mean systolic blood pressure (crude estimate)", "Mean fasting blood glucose (mmol/l) (crude estimate)",
             "Mean Total Cholesterol (crude estimate)"]

# Get data from URL
resp_armenia = requests.get(link_armenia)
resp_tanzania = requests.get(link_tanzania)
resp_azerbaiyan = requests.get(link_azerbaiyan)
resp_australia = requests.get(link_australia)
resp_jamaica = requests.get(link_jamaica)
resp_kenia = requests.get(link_kenia)

# Create Trees
armenia_tree = ET.fromstring(resp_armenia.content)
tanzania_tree = ET.fromstring(resp_tanzania.content)
azerbaiyan_tree = ET.fromstring(resp_azerbaiyan.content)
australia_tree = ET.fromstring(resp_australia.content)
jamaica_tree = ET.fromstring(resp_jamaica.content)
kenia_tree = ET.fromstring(resp_kenia.content)

# Saving data in array of arrays
data_armenia = []
data_tanzania = []
data_azerbaiyan = []
data_australia = []
data_jamaica = []
data_kenia = []

for row in armenia_tree.findall('Fact'):
    gho = row.find('GHO').text
    if gho in gho_index:

        try:
            country = row.find('COUNTRY').text
            sex = row.find('SEX').text
            year = row.find('YEAR').text
            ghecauses = row.find('GHECAUSES').text
            agegroup = row.find('AGEGROUP').text
            display = row.find('Display').text
            numeric = row.find('Numeric').text
            low = row.find('Low').text
            high = row.find('High').text
            result = [gho, country, sex, year, ghecauses,
                      agegroup, display, numeric, low, high]
            data_armenia.append(result)

        except:
            pass


# Carga de datos a spreadsheet
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
SERVICE_ACCOUNT_FILE = 't4_keys.json'

creds = None
creds = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)

SAMPLE_SPREADSHEET_ID = '1thuNzDZjTp4vuKn6oe-pYTtgIH_hl2Km2rRHIzBLYvs'
service = build('sheets', 'v4', credentials=creds)

# Call the Sheets API
sheet = service.spreadsheets()
# Loading headers in sheets
wrt_headers = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                    range="Armenia [ARM]!A1", valueInputOption="USER_ENTERED", body={"values": headers}).execute()
# Loading Armenia to sheet
wrt_armenia = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                    range="Armenia [ARM]!A2", valueInputOption="USER_ENTERED", body={"values": data_armenia}).execute()
# wrt_tanzania = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID,
#                                      range="Tanzania [TZA]!A2", valueInputOption="USER_ENTERED", body={"values": data_armenia}).execute()

print("done")
