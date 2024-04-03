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

    while True:
        print("please enter yesterday's main sales.")
        print("please enter four numbers, separated by commas.")
        print("for_instance: 20,1,44,5\n")

        last_sales = input("Enter last sales: ")
    
        # split method to break commas from string data in a list
        main_sales_rate = last_sales.split(",")
    
        # call rates date from authentic_data and if statement to true rates
        if authentic_data(main_sales_rate):
            print("Data is valid")
            break
    return main_sales_rate

def authentic_data(rates):
    """
    try statement to coverts string rates to integer, raise valueError if not interger or 4 rates exactly, run while loop until rates are authentic
    """
    try:
        [int(rate) for rate in rates]
        if len(rates) != 4:
            raise ValueError(
                f"4 rates are required, you provided {len(rates)}"
            )
    except ValueError as e:
        print(f"Invalid rates: {e}, please try again.\n")
        return False
    return True


def modify_main_sales(new_rate):
    """modify main_sales worksheet, add new row with new provided rates"""
    print("modifying main_sales rates......\n")
    main_sales_worksheet = SHEET.worksheet("main_sales")
    main_sales_worksheet.append_row(new_rate)
    print("main_sales_worksheet successfully modified\n")

new_rate = request_main_sales()
main_sales_rate = [int(sale) for sale in new_rate]
modify_main_sales(main_sales_rate)