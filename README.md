# gtracker
Simple Python module for logging data daily to a Google Sheet. 

Requirements: oauth2client, gspread



Sample usage: 

temperaturesWorksheet = gtracker.initWorksheet(GOOGLE_SHEETS_JSON_KEYFILE, SHEET_FILENAME)

temperatures_today = {'London': 15, 'Paris': 17}

gtracker.dailyUpdate(temperaturesWorksheet, temperatures_today)


