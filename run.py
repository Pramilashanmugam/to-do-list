"""
Imports necessary libraries for the To-Do List application.

This section imports the following libraries:
- `datetime` from the standard Python library for date and time manipulation.
- `Fore` from the Colorama library for terminal color formatting.
- `tabulate` from the Tabulate library for displaying data in tabular format.
- `gspread` for interacting with Google Sheets.
- `Credentials` from the Google OAuth2 library for handling authentication.
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
    """\n
╔═══════════════════════════════════════════════════════════════╗
║███████████            █████          ████  ███        █████   ║
║█░░░███░░░█           ░░███           ░███ ░░░        ░░███    ║
║   ░███  ░██████    ███████   ██████  ░███ ████  ████████████  ║
║   ░███  ███░░███  ███░░███  ███░░███ ░███░░███ ███░░░░░███░   ║
║   ░███ ░███ ░███ ░███ ░███ ░███ ░███ ░███ ░███░░█████ ░███    ║
║   ░███ ░███ ░███ ░███ ░███ ░███ ░███ ░███ ░███ ░░░░███░███ ███║
║   █████░░██████  ░░████████░░██████  ████████████████ ░░█████ ║
║  ░░░░░  ░░░░░░    ░░░░░░░░  ░░░░░░   ░░░░░░░░░░░░░░░   ░░░░░  ║
╚═══════════════════════════════════════════════════════════════╝
""" + Fore.RESET)
print("\nWelcome to your To do list app!💡")
print("\nThis app helps you to keep track on your day to day activities.\n")
print("You can add, delete, view or modify your tasks in this app\n")


def validate_task_input():
    """
    Validates the task input provided by the user.

    This function prompts the user to enter a task description and ensures
    that it does not exceed 100 characters.
    If the task description is empty or exceeds 100 characters, appropriate
    error messages are displayed, and the user is prompted again until a valid
    task description is provided.
    """
    while True:
        task_input = input(
            Fore.LIGHTCYAN_EX +
            "\nPlease add enter your task 🗒 (max 100 Characters): "
            + Fore.RESET)
        if not task_input:
            print(Fore.LIGHTRED_EX +
                  "\nTask cannot be empty. Please enter a task" + Fore.RESET)
        elif len(task_input) > 100:
            print(Fore.LIGHTRED_EX + "\nTask cannot exceed 100 Characters.")
            print("Please enter a shorter Task.\n" + Fore.RESET)
        else:
            return task_input


def validate_date(date_str):
    """
    Validates the format of a date string.

    This function attempts to parse the input date string in the format of
    DD/MM/YYYY using the `datetime.strptime` method. If the parsing is
    successful, it returns True, indicating that the date format is valid.
    If the parsing fails, indicating an invalid date format, it returns False.
    """
    try:
        datetime.strptime(date_str, '%d/%m/%Y')
        return True
    except ValueError:
        return False


def add_task():
    """
    Adds a task to the task list.

    This function prompts the user to enter the task description and
    ensures that it does not exceed 100 characters.
    It then prompts the user to enter the deadline for the task in the
    format of DD/MM/YYYY.
    The function validates the date format and ensures that the deadline
    is not in the past.
    If the task and date are valid, the task is added to the list with
    its deadline.
    If the date is invalid or in the past, or if the task description exceeds
    100 characters, appropriate error messages are displayed.
    """

    # Get the current date using library
    current_date = datetime.now().date()

    # Validate task input
    task_input = validate_task_input()

    # Checking for valid date and loops until valid date is received
    while True:
        date = input(Fore.LIGHTCYAN_EX +
                     "\nPlease enter the date 📅 for completion(dd/mm/yyyy): " +
                     Fore.RESET)
        # Validate date format
        if not validate_date(date):
            print(Fore.LIGHTRED_EX + "\nInvalid date format.")
            print("Please enter valid date 📅 in dd/mm/yyyy" + Fore.RESET)
            continue
        # Convert the input date string to a datetime object
        deadline = datetime.strptime(date, '%d/%m/%Y').date()

        # Check if the deadline date is in the past
        if deadline < current_date:
            print(Fore.LIGHTRED_EX +
                  "\nDeadline date for completion cannot be in the past.")
            print("Please enter a future date." + Fore.RESET)
        else:
            break

    # Append a new row with the task details
    task_sheet.append_row([task_input, date])
    print(Fore.LIGHTYELLOW_EX + f"\nA new task '{task_input}' with deadline "
          f"{date} has been successfully added 👍" + Fore.RESET)


def list_tasks():
    """
    Displays the list of tasks stored in the spreadsheet.

    Retrieves all tasks from the spreadsheet and checks if any tasks exist.
    If no tasks are found, a message indicating no tasks are present
    is displayed. If tasks are found, they are displayed in a tabulated
    format with index, task description, and deadline.
    """
    tasks = task_sheet.get_all_values()
    if not tasks[1:]:
        print(Fore.RED + "\nNo task found 😥" + Fore.RESET)
    else:
        table_data = [[Fore.LIGHTCYAN_EX + "Index",
                       "Tasks", "Deadline" + Fore.RESET]]
        for index, task in enumerate(tasks[1:], start=1):
            task_input = task[0]
            deadline = task[1]
            table_data.append([index, task_input, deadline])
        print(Fore.LIGHTYELLOW_EX + "\nCurrent tasks: " + Fore.RESET)
        print(tabulate(table_data, headers="firstrow", tablefmt="grid"))


def delete_task():
    """
    Deletes a task from the task list.

    This function prompts the user to enter the index number of the task
    they want to delete. It then checks if the entered index is valid
    and corresponds to an existing task.
    If the task exists, it is removed from the task list.
    If the index is invalid or the task doesn't exist, an appropriate
    error message is displayed.

    Raises:
        ValueError: If the user enters a non-integer value or an index that
        is out of range.
    """
    # Fetch tasks from the worksheet
    tasks = task_sheet.get_all_values()
    list_tasks()
    try:
        user_input_delete = int(input(
            Fore.LIGHTGREEN_EX +
            "\nEnter the index no to delete the task: " + Fore.RESET))
        task_to_delete = user_input_delete + 1
        if task_to_delete > 1 and task_to_delete <= len(tasks):
            # Delete the corresponding row from the worksheet
            # Adding 1 to match the indexing used in list_tasks
            task_sheet.delete_rows(task_to_delete)
            print(Fore.RED + f"\nTask no '{user_input_delete}' "
                  f"has been successfully deleted" + Fore.RESET)
        else:
            print(Fore.LIGHTRED_EX +
                  f"\nTask not found: '{user_input_delete}' " + Fore.RESET)
    except ValueError:
        print(Fore.LIGHTRED_EX +
              "\nInvalid input. Please enter a valid index." + Fore.RESET)


def update_task():
    """
    Updates an existing task in the To-Do List.

    This function allows the user to update an existing task by
    providing the index number of the task to be updated.
    It retrieves the current task details, including the task description
    and deadline, displays them to the user, and prompts for updated
    information. After validating the updated task details,
    including the task description and deadline format, it updates
    the corresponding row in the worksheet with the new information.

    Raises:
        ValueError: If the index provided by the user is invalid or not
        a number.
    """
    # Fetch tasks from the worksheet
    tasks = task_sheet.get_all_values()
    list_tasks()
    try:
        task_to_update = int(input(
            Fore.LIGHTGREEN_EX +
            "\nEnter the index no of the task to update: " + Fore.RESET))

        if task_to_update >= 1 and task_to_update < len(tasks):
            # Retrieve task information
            task_to_modify = tasks[task_to_update]
            print(f"\nCurrent Task: {task_to_modify[0]}"
                  f" with Deadline: {task_to_modify[1]}")
            # Prompt user for updated task details
            updated_task = validate_task_input()
            updated_deadline = input(
                Fore.LIGHTCYAN_EX +
                "\nEnter the updated deadline (dd/mm/yyyy): " + Fore.RESET)
            while not validate_date(updated_deadline):
                print(
                    Fore.LIGHTRED_EX +
                    "\nInvalid date format. Please enter date in dd/mm/yyyy."
                    + Fore.RESET)
                updated_deadline = input(
                    Fore.LIGHTCYAN_EX +
                    "Enter the updated deadline (dd/mm/yyyy): " + Fore.RESET)
                # Update the corresponding row in the worksheet
            task_sheet.update([[updated_task, updated_deadline]],
                              f'{task_to_update+1}:{task_to_update+1}')
            print(Fore.LIGHTYELLOW_EX +
                  "\nTask updated successfully." + Fore.RESET)
        else:
            print(Fore.LIGHTRED_EX +
                  f"\nTask '{task_to_update}' not found" + Fore.RESET)
    except ValueError:
        print(Fore.LIGHTRED_EX +
              "\nInvalid input. Please enter a valid index." + Fore.RESET)


def main():
    """
    Main function for the To-Do List application.

    This func presents a menu of options for the user
    to choose from, including:
    1. Add Task
    2. View Tasks
    3. Delete Task
    4. Edit Task
    5. Exit

    The user is prompted to enter their choice,
    and based on the input received,
    the corresponding function is called to perform the selected action.
    """
    while True:
        print(Fore.LIGHTGREEN_EX +
              "\nPlease choose an option from below(enter only number ex:1): ")
        print("--------------------------------------------------------------"
              + Fore.RESET)
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Edit Task")
        print("5. Exit")
        try:
            choice = int(
                input(Fore.LIGHTGREEN_EX + "\nEnter your choice: "
                      + Fore.RESET))
        except ValueError:
            # if value other than integer received then error message reflects
            print(Fore.LIGHTRED_EX +
                  "Invalid input. Please enter a valid number." + Fore.RESET)
            continue
        print(Fore.LIGHTGREEN_EX +
              "--------------------------------------------------------------"
              + Fore.RESET)
        if choice == 1:
            add_task()
        elif choice == 2:
            list_tasks()
        elif choice == 3:
            delete_task()
        elif choice == 4:
            update_task()
        elif choice == 5:
            break
        else:
            print(Fore.LIGHTRED_EX +
                  "Please enter the valid number" + Fore.RESET)
    print("\nGood Bye 👋 👋")
    print(Fore.LIGHTBLUE_EX +
          "\nTo start the app again, Press the Run Program button above\n")


main()
