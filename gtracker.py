from oauth2client.service_account import ServiceAccountCredentials
import gspread
from datetime import date


def initWorksheet(keyfile, sheetname):
  """Takes a Google Drive API JSON keyfile and the name of the file to connect to and returns a Google Worksheet object.
  keyfile: full path and name of your GDrive API json file
  sheetname: name of sheet in your Google Drive"""
  SCOPES = ["https://spreadsheets.google.com/feeds"]
  credentials = ServiceAccountCredentials.from_json_keyfile_name(keyfile, SCOPES)
  connection = gspread.authorize(credentials)
  worksheet = connection.open(sheetname).sheet1
  return worksheet

def dailyUpdate(worksheet, data):
  """ Takes a worksheet object and appends the data in the next column, adding the current date to the header row.
  If a key from the data dict is found in column A, then its value is added to the same row.
  If a key from the data dict is not found, then it is added to the next empty row in column A, and value on the same row.
  worksheet: Takes a Google API Worksheet object
  data: takes a Dict object"""
  date_today = str(date.today())
  current_col = worksheet.row_values(1).index('')+1
  current_row = worksheet.col_values(1).index('')+1
  worksheet.update_cell(1,current_col, date_today)
  for key in data.keys():
    # if plate already in sheet, add price on same row, current day col
    try:
      row_number = worksheet.col_values(1).index(key)+1
      worksheet.update_cell(row_number,current_col, data[key])
  # if plate not in sheet, add plate to first empty row in column 1, then add price on current day col
    except:
      current_row = worksheet.col_values(1).index('')+1
      worksheet.update_cell(current_row,current_col, data[key])
      worksheet.update_cell(current_row,1, key)
  return "Daily Update done."
