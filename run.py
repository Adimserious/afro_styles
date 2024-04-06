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

    # Loop until authentic rates are inputed
    while True:
        print("please enter yesterday's main sales.")
        print("please enter four numbers, separated by commas.")
        print("for_instance: 20,1,44,5\n")

        last_sales = input("Enter last sales:\n")
        print(f"you entered {last_sales}")
    
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
    print("main_sales worksheet successfully modified\n")


def modify_remain(new_rate):
    """modify remain worksheet by adding new row"""
    print("modifying remain rates......\n")
    remain_worksheet = SHEET.worksheet("remain")
    remain_worksheet.append_row(new_rate)
    print("remain worksheet successfully modified\n")

def modify_before_sales(new_rate):
    """Modify before sales rate with recommended values to the new row"""
    print("modifying before_sales rates.....\n")
    before_sales_worksheet = SHEET.worksheet("before_sales")
    before_sales_worksheet.append_row(new_rate)
    print("Almost done.....\n")
    print("before_sales worksheet successfully modified")
    

def sales_prediction(new_rate):
    """Display modify before sales to user as dictionary"""
    print("There you have it, the following predictions are recommended for future sales\n")

    headings = SHEET.worksheet("before_sales").row_values(1)
    print(headings)
    last_row = SHEET.worksheet("before_sales").row_values()
    print(last_row)

    dictionary = dict(zip(headings, last_row))
    print(dictionary)

    print(f"Thank you for using our service, click run program to start again\n")


def evaluate_remain_rate(main_sales_row):
    """compare main sales to before sales"""
    print("evaluating remain rates...\n")

    # fetching data from worksheet using gspread method
    before_sales = SHEET.worksheet("before_sales").get_all_values()
    
    # fetching the last row from before sales rate to evaluate remain
    before_sales_row = before_sales[-1]
    
    # convert before sales to integer, loop through before sales and main sales with zip and append it to remain rate
    remain_rate = []
    for before_sales, main_sales in zip(before_sales_row, main_sales_row):
        remain = int(before_sales) - main_sales
        remain_rate.append(remain)
   
    return remain_rate


def last_four_main_sales():
    """Calculate last four collumns of the main_sales for every afro_style and return as a list"""
    main_sales = SHEET.worksheet("main_sales")
    
    # access all las 4 columns using gspread col_value method
    all_collums = []
    for one in range(1,5):
        one_collumn = main_sales.col_values(one)
        all_collums.append(one_collumn[-4: ])

    return all_collums 


def evaluate_before_sales(return_rates):
    """Evaluate mean rate for each list item and convert to integer"""
    print("evaluating before sales rate...\n")

    new_before_sales = []
    # loop through each column
    for col in return_rates:
        column = [int(num) for num in col]
        mean = sum(column) / 4
        # Add ten percent to mean as recommendation for future sales
        before_sales_add = mean * 1.1
        new_before_sales.append(round(before_sales_add))

    return new_before_sales    



def main_functions():
    """All program functions wrapped here and run"""
    new_rate = request_main_sales()
    main_sales_rate = [int(sale) for sale in new_rate]
    modify_main_sales(main_sales_rate)
    update_remain_rate = evaluate_remain_rate(main_sales_rate)
    modify_remain(update_remain_rate)
    main_sales_collums = last_four_main_sales()
    before_sales_rate = evaluate_before_sales(main_sales_collums)
    modify_before_sales(before_sales_rate)
    # sales_prediction = (modify_before_sales)

print("Welcome to Afro_styles rate automation")

main_functions() 
sales_prediction(modify_before_sales)
