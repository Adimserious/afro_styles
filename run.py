# import gspread library and credential class from google-auth library after download 
import gspread
from google.oauth2.service_account import Credentials

# Google Sheets API scope and credentials
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("afro_styles")

main_sales = SHEET.worksheet("main_sales")

def request_main_sales():
    """Main sales data request from user"""
    print("welcome to Afro_styles, please enter yesterday's main sales.")
    print("please enter four numbers, separated by commas.")
    print("for_instance: 20,1,44,5\n")

    last_sales = input("Enter last sales: ")
    print(f"you entered {last_sales}")



request_main_sales()