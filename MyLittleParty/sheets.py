from oauth2client.service_account import ServiceAccountCredentials

import gspread
import pandas as pd

def googleDocReadIn():
    ### Read-in google doc
    scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive'] # link of my google sheet

    # add credentials to the account
    creds = ServiceAccountCredentials.from_json_keyfile_name('j.json', scope) # json file contains my own key

    # authorize the clientsheet 
    client = gspread.authorize(creds)

    # get the instance of the Spreadsheet
    sheet = client.open('Az én kicsi pártom') # name of the spreadsheat file
    return sheet

t = googleDocReadIn()
t = t.get_worksheet(0)

t = t.get_values()
t = pd.DataFrame(t[1::], columns =t[0])
t = t[0:50] # 50 kártya 
#### filter
# ONLY B1 BATCH

#t = t[t["NO-PRINT"] != "x"]
# filter temp print
#t = t[t["TEMP_PRINT"] == "x"]


# sort - cards with pictures first
# t.sort_values(by=['KÉP'], ascending=0, inplace=True)
# t.sort_values(by=['D-Leiras Raw Conter'], ascending=0, inplace=True)

t.to_csv('nepKartyak.csv', index=False, encoding = 'iso-8859-2')

