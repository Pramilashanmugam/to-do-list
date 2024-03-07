"""
importing essential libraries for this project
"""
from datetime import datetime
import gspread
from google.oauth2.service_account import Credentials

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

    # Get the current date using library
    current_date = datetime.now().date()

    # Get the number of rows in the worksheet
    tasks = task_sheet.get_all_values()

    # Asking user to enter the task. Validating for text length and ensure its not empty.
    while True:
        task_input = input("Please add enter your task(max 100 Characters): ")
        if not task_input:
            print("Task cannot be empty. Please enter a task")
        elif len(task_input) > 100:
            print("Task cannot exceed 100 Characters. Please enter a shorter Task.")
        else:
            break
    # Checking for valid date and loops until valid date is received
    while True:
        date = input("Please enter the date for completion(dd/mm/yyyy):")
        # Validate date format
        if not validate_date(date):
            print("Invalid date format. Please enter date in dd/mm/yyyy format.")
            continue
        # Convert the input date string to a datetime object
        deadline = datetime.strptime(date, '%d/%m/%Y').date()

        # Check if the deadline date is in the past
        if deadline < current_date:
            print(
                "Deadline date for completion cannot be in the past. Please enter a future date.")
        else:
            break

    # Append a new row with the task details
    tasks = task_sheet.get_all_values()
    task_sheet.append_row([task_input, date])
    print(f"\nA new task '{task_input}' with deadline {date} has been successfully added 👍")


def list_tasks():
    """
    list done the tasks in the spreadsheet
    """
    tasks = task_sheet.get_all_values()
    if not tasks:
        print("There is no tasks currently")
    else:
        print("Current tasks:")
        print("Index:Tasks                    : Deadline")
        for index, task in enumerate(tasks[1:], start=1):
            print(f"{index}:    {task[0]}            (Deadline: {task[1]})")


"""def m
    a function to modify an existing task
   
    # Fetch tasks from the worksheet
    tasks = task_sheet.get_all_values()
    list_tasks()
    try:
        task_to_modify = int(input("Enter the index no of the task to modify: "))
        if task_to_modify > 1 and task_to_modify <= len(tasks) - 1:"""


def delete_task():
    """
    A function to delete a task
    """
    # Fetch tasks from the worksheet
    tasks = task_sheet.get_all_values()
    list_tasks()
    try:
        task_to_delete = int(input("Enter the index no to delete the task: "))
        if task_to_delete > 1 and task_to_delete <= len(tasks) - 1:
            # Delete the corresponding row from the worksheet
            # Adding 1 to match the indexing used in list_tasks
            task_sheet.delete_rows(task_to_delete + 1)
            print(f"Task'{task_to_delete}'has been deleted")
        else:
            print(f"Task '{task_to_delete}' not found")
    except ValueError:
        print("Invalid input. Please enter a valid index.")


def main():
    """
    This function has the options to be chosen by the user.
    Depending on the input received, the program will call the respective function.
    """
    while True:
        print("\nPlease choose an option from below: ")
        print("--------------------------------------------------------------")
        print("1. Add Task")
        print("2. Modify Task")
        print("3. View Tasks")
        print("4. Delete Task")
        print("5. Exit")
        choice = int(input("Enter your choice: "))
        print("--------------------------------------------------------------")
        if choice == 1:
            add_task()
        elif choice == 2:
            print("currently under process")
        elif choice == 3:
            list_tasks()
        elif choice == 4:
            delete_task()
        elif choice == 5:
            break
        else:
            print("Please enter the valid number")


main()
