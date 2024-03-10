"""
importing essential libraries for this project
"""
from datetime import datetime
from colorama import Fore
# library used to display the data in tabular column in view list
from tabulate import tabulate
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


print(
    Fore.BLUE +
    """\n▐▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▌
▐  ███████████                 █████             ████   ███           █████    ▌
▐ ░█░░░███░░░█                ░░███             ░░███  ░░░           ░░███     ▌
▐ ░   ░███  ░   ██████      ███████   ██████     ░███  ████   █████  ███████   ▌
▐     ░███     ███░░███    ███░░███  ███░░███    ░███ ░░███  ███░░  ░░░███░    ▌
▐     ░███    ░███ ░███   ░███ ░███ ░███ ░███    ░███  ░███ ░░█████   ░███     ▌
▐     ░███    ░███ ░███   ░███ ░███ ░███ ░███    ░███  ░███  ░░░░███  ░███ ███ ▌
▐     █████   ░░██████    ░░████████░░██████     █████ █████ ██████   ░░█████  ▌
▐    ░░░░░     ░░░░░░      ░░░░░░░░  ░░░░░░     ░░░░░ ░░░░░ ░░░░░░     ░░░░░   ▌
▐▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▌""" + Fore.RESET)
print("\nWelcome to your To do list app!💡")
print("\nThis app helps you to keep track on your day to day activities.\n")
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

    # Asking user to enter the task. Validating for text length and ensure its not empty.
    while True:
        task_input = input(
            Fore.LIGHTCYAN_EX + "Please add enter your task 🗒 (max 100 Characters): " + Fore.RESET)
        if not task_input:
            print("Task cannot be empty. Please enter a task")
        elif len(task_input) > 100:
            print("Task cannot exceed 100 Characters. Please enter a shorter Task.")
        else:
            break
    # Checking for valid date and loops until valid date is received
    while True:
        date = input(Fore.LIGHTCYAN_EX +
                     "Please enter the date 📅 for completion(dd/mm/yyyy): " + Fore.RESET)
        # Validate date format
        if not validate_date(date):
            print("Invalid date format. Please enter date 📅 in dd/mm/yyyy format.")
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
    task_sheet.append_row([task_input, date])
    print(Fore.LIGHTCYAN_EX + f"\nA new task '{task_input}' with deadline "
          f"{date} has been successfully added 👍" + Fore.RESET)


def list_tasks():
    """
    list done the tasks in the spreadsheet
    """
    tasks = task_sheet.get_all_values()
    if not tasks[1:]:
        print(Fore.RED + "No task found 😥" + Fore.RESET)
    else:
        table_data = [[Fore.LIGHTCYAN_EX + "Index",
                       "Tasks", "Deadline" + Fore.RESET]]
        for index, task in enumerate(tasks[1:], start=1):
            task_input = task[0]
            deadline = task[1]
            table_data.append([index, task_input, deadline])
        print(Fore.LIGHTYELLOW_EX + "\nCurrent tasks:" + Fore.RESET)
        print(tabulate(table_data, headers="firstrow", tablefmt="grid"))


def delete_task():
    """
    A function to delete a task
    """
    # Fetch tasks from the worksheet
    tasks = task_sheet.get_all_values()
    list_tasks()
    try:
        task_to_delete = int(input(Fore.GREEN +
                                   "\nEnter the index no to delete the task: " + Fore.RESET))
        if task_to_delete >= 1 and task_to_delete <= len(tasks):
            # Delete the corresponding row from the worksheet
            # Adding 1 to match the indexing used in list_tasks
            task_sheet.delete_rows(task_to_delete + 1)
            print(Fore.RED + f"\nTask no '{task_to_delete}' "
                  f"has been successfully deleted" + Fore.RESET)
        else:
            print(f"\nTask not found: '{task_to_delete}' ")
    except ValueError:
        print("\nInvalid input. Please enter a valid index.")


def main():
    """
    This function has the options to be chosen by the user.
    Depending on the input received, the program will call the respective function.
    """
    while True:
        print(Fore.GREEN + "\nPlease choose an option from below: ")
        print("--------------------------------------------------------------" + Fore.RESET)
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Exit")
        try:
            choice = int(
                input(Fore.GREEN + "\nEnter your choice: " + Fore.RESET))
        except ValueError:
            # if any value other than integer received then error message reflects
            print("Invalid input. Please enter a valid number.")
            continue
        print(Fore.GREEN +
              "--------------------------------------------------------------" + Fore.RESET)
        if choice == 1:
            add_task()
        elif choice == 2:
            list_tasks()
        elif choice == 3:
            delete_task()
        elif choice == 4:
            break
        else:
            print("Please enter the valid number")
    print("\nGood Bye 👋 👋")
    print(Fore.LIGHTGREEN_EX +
          "\nTo start the app again, Press the Run Program button")


main()
