import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime
from pprint import pprint

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

# Authenticate with Google account
CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)

# Open the spreadsheet
SHEET = GSPREAD_CLIENT.open('todolist')
    
# Select the tasks worksheet
task_sheet = SHEET.worksheet('tasks')


print("""\n▐▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▌
▐  ███████████                 █████             ████   ███           █████    ▌
▐ ░█░░░███░░░█                ░░███             ░░███  ░░░           ░░███     ▌
▐ ░   ░███  ░   ██████      ███████   ██████     ░███  ████   █████  ███████   ▌
▐     ░███     ███░░███    ███░░███  ███░░███    ░███ ░░███  ███░░  ░░░███░    ▌
▐     ░███    ░███ ░███   ░███ ░███ ░███ ░███    ░███  ░███ ░░█████   ░███     ▌
▐     ░███    ░███ ░███   ░███ ░███ ░███ ░███    ░███  ░███  ░░░░███  ░███ ███ ▌
▐     █████   ░░██████    ░░████████░░██████     █████ █████ ██████   ░░█████  ▌
▐    ░░░░░     ░░░░░░      ░░░░░░░░  ░░░░░░     ░░░░░ ░░░░░ ░░░░░░     ░░░░░   ▌
▐▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▌""")
print("\nWelcome to your To do list app!")
print("This app helps you to keep track of your day to day activities.\n")
print("You can add, delete, view or modify your tasks in this app\n")


"""tasks = []
while True:
    print("\nPlease choose an option:")
    print("1. Add Task")
    print("2. Modify Task")
    print("3. View Tasks")
    print("4. Delete Task")
    print("5. Exit")
    choice = input("Enter your choice: ")
    
    if choice==1:
        add_task()
    elif choice==2:
    
    elif choice==3:

    elif choice==4:

    elif choice==5:
    
    else:
        print("Please enter the valid number")
        """


def validate_date(date_str):
    """ 
    This function is to validate the date format entered by user is valid or not
    """
    try:
        datetime.strptime(date_str, '%d/%m/%Y')
        return True
    except ValueError:
        return False


def add_task():
    """
    A function is to add task by the user with the date for completion,
    I have used a loop to ensure the user enters the valid date in the format of DD/MM/YYYY
    """

    # Get the number of rows in the worksheet
    index_length = task_sheet.get_all_values()
    num_rows = 0
    for row in index_length:
        num_rows +=1

    # Asking user to enter the task. Validating for text length and ensure its not empty.
    while True:
        task_input = input("Please add enter your task(max 100 Characters): ")
        if not task_input:
            print("Task cannot be empty. Please enter a task")
        elif len(task_input)>100:
            print("Task cannot exceed 100 Characters. Please enter a shorter Task.")
        else:
            break
    # Checking for valid date and loops until valid date is received
    while True:
        date = input("Please enter the date for completion(dd/mm/yyyy):")
        # Validate date
        if validate_date(date):
            print("")
            break
        else:
            print("Invalid date format. Please enter date in dd/mm/yyyy format.")

    # Append a new row with the task details
    task_sheet.append_row([num_rows,task_input, date])

add_task()
