#import pandas as pd
import requests
import xml.etree.ElementTree as ET

link_armenia = "http://tarea-4.2021-1.tallerdeintegracion.cl/gho_ARM.xml"
# link_tanzania = "http://tarea-4.2021-1.tallerdeintegracion.cl/gho_TZA.xml"
# link_azerbaiyan = "http://tarea-4.2021-1.tallerdeintegracion.cl/gho_AZE.xml"
# link_australia = "http://tarea-4.2021-1.tallerdeintegracion.cl/gho_AUS.xml"
# link_jamaica = "http://tarea-4.2021-1.tallerdeintegracion.cl/gho_JAM.xml"
# link_kenia = "http://tarea-4.2021-1.tallerdeintegracion.cl/gho_KEN.xml"

death_index = ["Number of deaths", "Number of infant deaths"]

resp_armenia = requests.get(link_armenia)
# print(resp_armenia.content)
tree = ET.fromstring(resp_armenia.content)
result = []
print("#############")
print("#############")
print("#############")
print("#############")
for row in tree.findall('Fact'):
    gho = row.find('GHO').text

    if gho in death_index:

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
            result = [gho, country, year, ghecauses,
                      agegroup, display, numeric, low, high]
            print(result)

        except:
            pass

    #gho = row.get('GHO')
    #numeric = row.get('Numeric')
    # if numeric != None:
    #     result = [gho, numeric]
    #     print(result)


#tree = ET.parse(r_armenia.text)
#root = tree.getroot()

# for country in root.findall('COUNTRY'):
#     rank = country.find('GBDCHILDCAUSES').text
#     print(rank)
#     # name = country.get('name')
#     # print(name, rank)

# for child in root:
#     print(child.tag, child.attrib)
