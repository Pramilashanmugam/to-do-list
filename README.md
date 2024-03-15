# To do List app 
## Welcome to my [To do list app](https://my-to-do-list-a8066c712807.herokuapp.com/)

![Screenshot 2024-03-13 10 59 48 AM](https://github.com/Pramilashanmugam/to-do-list/assets/150790058/0f664087-5cc6-453e-a800-710368ccf4c2)


## Introduction:
The purpose of developing this app is to keep track of our current and future appointments/plans. It is very important for each and everyone of us to stay organized and manage our day to day tasks effectively. I believe this app would help us achieve the same.

# Features:

## Technologies:

 * Python
   * This app is developed using Python.
 * Visual Studio Code
   * This website was developed using Gitpod IDE and also used the code institute template.
 * Github
   * Source code is hosted on GitHub.
 * Git
   * Used to commit and push code during the development of the Website.
 * Heroku
   * Deployment is done on Heroku.

## UX Design

### User Story:

As a multitasking homemaker, professional, parent, or student, I want a to-do list app that efficiently organizes tasks and manages daily responsibilities so that I can stay on top of my workload and accomplish my goals effectively. 

#### As an User:
* I want the app to add the task with a deadline.
* I want the app to list down all the tasks in the database.
* I want the app to delete the task which is no longer needed.
* I want the app to allow me to edit the existing task.
* I want the app to validate the input datas like date and have a control over the length of the task.
* I want a message after every action when successfully implemented.
* I want a error message incase of invalid data.

#### As the App Administrator:

* I want the app to be presentable as well as readable.
* I want the app to be user friendly.
* I want the output to be clear and not clumpsy.
* I want the user to differentiate between valid and invalid data received by adding text colors.
* I want the app to display the task in a numerical order.

### Acceptance Criteria:

* Adding Tasks:

  * I should be able to add a new task to my list.
When adding a task, I should provide a brief description and specify a deadline.

* Viewing Tasks:

  * I should be able to view all my tasks in a clear and organized manner.
Each task should display its description and deadline.

* Deleting Tasks:

  * I should be able to remove a task from my list if I no longer need to complete it.

* Updating Tasks:

  * I should be able to edit the description or deadline of an existing task if needed.

* Validation:

  * The app should validate user inputs to ensure task descriptions are not empty and date are in the correct format.
Error messages should be displayed clearly to guide me in correcting any mistakes.

### Design:

* Due to the fact that this application is terminal based and also relies on code institute template. I have not made any addition to design and sticking to the default template provided by Code institute.
* However i have used emoji's and text colours in the output to give a better visual experience.


### Flowchart:

![Screenshot 2024-03-13 5 33 11 PM](https://github.com/Pramilashanmugam/to-do-list/assets/150790058/0b463fc7-8f3e-4745-a954-9a8927ec19bb)

## Existing Features:

### Main features of this app:

### `Choose an option`: Choose between 5 given options to perform a particular function.

  ![Screenshot 2024-03-13 12 09 43 PM](https://github.com/Pramilashanmugam/to-do-list/assets/150790058/582bdfe5-b156-441c-9909-87a6b284b2b5)

### `Adding tasks`: User opt for option 1 to add new tasks with a deadline.

  ![Screenshot 2024-03-13 12 06 54 PM](https://github.com/Pramilashanmugam/to-do-list/assets/150790058/7e16667c-bcbc-4872-87ee-0d5dbaf6e23f)

Task within 100 Characters accepted and if exceeds more than 100 characters or character is 0 then a error message displays for user to enter a short message and this continues until the condition is true.

![Screenshot 2024-03-13 12 19 36 PM](https://github.com/Pramilashanmugam/to-do-list/assets/150790058/d857757f-f655-417a-b2d0-3450377eeab7)

The data gets added and stored in Google spread sheet.

![Screenshot 2024-03-13 12 22 41 PM](https://github.com/Pramilashanmugam/to-do-list/assets/150790058/d70c2e6f-7dee-4fc3-aa22-42859e53816c)

If the character was more than 100 character the following error message will display

![Screenshot 2024-03-13 12 25 02 PM](https://github.com/Pramilashanmugam/to-do-list/assets/150790058/9975b1b7-9105-4b0c-adc2-182c59406d8a)

If the task is empty the following error message will display

![Screenshot 2024-03-13 12 26 02 PM](https://github.com/Pramilashanmugam/to-do-list/assets/150790058/7efb940a-c1cd-4fef-9528-bf1a2a8eff23)

Only current date in the format of dd/mm/yyyy is accepted if the date is past or other special characters and error message will display.

* Current date

  ![Screenshot 2024-03-13 12 28 34 PM](https://github.com/Pramilashanmugam/to-do-list/assets/150790058/f236cf4f-fdd9-4ea7-83bd-1d1472456b2a)

* Invalid date
![Screenshot 2024-03-13 12 32 27 PM](https://github.com/Pramilashanmugam/to-do-list/assets/150790058/66eb4b18-6635-43ab-bbaa-16aa203ab46f)

* Past date
![Screenshot 2024-03-13 12 33 20 PM](https://github.com/Pramilashanmugam/to-do-list/assets/150790058/0199545b-5729-4482-ae52-423eea065655)

### `Viewing tasks`: Users can view their existing tasks in a list format.

![Screenshot 2024-03-13 12 35 10 PM](https://github.com/Pramilashanmugam/to-do-list/assets/150790058/da4eeb92-a129-4897-a699-d8e5e383072c)

### `Deleting tasks`: Users can delete tasks they no longer need.

![Screenshot 2024-03-13 12 36 11 PM](https://github.com/Pramilashanmugam/to-do-list/assets/150790058/d92e4349-6ec8-4fc8-9f54-0fcb6ebb6433)

Choose the task which needs to be deleted using index number.

![Screenshot 2024-03-13 12 37 36 PM](https://github.com/Pramilashanmugam/to-do-list/assets/150790058/d65676c6-c2c4-428e-9054-a02a19d6937c) 

To confirm the task is no more use view task option

![Screenshot 2024-03-13 12 39 05 PM](https://github.com/Pramilashanmugam/to-do-list/assets/150790058/d6b11560-d2d3-45a1-8cb7-a9bc0c98c34b)

If the index number entered is not available in the data, an error message will display

![Screenshot 2024-03-13 12 41 11 PM](https://github.com/Pramilashanmugam/to-do-list/assets/150790058/fb131767-ecef-4047-bb83-44897d730480)

### `Updating tasks`: Users can edit existing tasks, by modifying the task description and deadline.

![Screenshot 2024-03-13 12 42 43 PM](https://github.com/Pramilashanmugam/to-do-list/assets/150790058/39b1d231-e015-4e74-bbff-337a5470889a)

Displays the list of task, once index of task to modified inputed, it displays the data to be modified and then ask to enter new task and deadline

If index was an invalid input

![Screenshot 2024-03-13 5 46 33 PM](https://github.com/Pramilashanmugam/to-do-list/assets/150790058/c22d7bc9-c6b1-4988-bdea-85a57faef149)

New task is accepted only when the length of the character doesnot exceeds 100 character

![Screenshot 2024-03-13 5 35 26 PM](https://github.com/Pramilashanmugam/to-do-list/assets/150790058/302203bb-90b4-4142-83d3-71db82902f88)

Once valid data entered task will be modified

![Screenshot 2024-03-13 5 38 22 PM](https://github.com/Pramilashanmugam/to-do-list/assets/150790058/ebe71b99-4d07-42f6-b9be-a4b865afdfc0)

on clicking view task you get a confirmation on updated data

![Screenshot 2024-03-13 5 39 45 PM](https://github.com/Pramilashanmugam/to-do-list/assets/150790058/ffb11a38-6dcd-4206-ad99-7315a79764e7)

If invalid data like text longer than 100 character and not a current date or wrong index number - same as Add function the error message will display.

![Screenshot 2024-03-13 5 47 56 PM](https://github.com/Pramilashanmugam/to-do-list/assets/150790058/2afbc362-c115-4b00-bd70-90033390409b)

If the task is empty the following error message will display

![Screenshot 2024-03-13 12 26 02 PM](https://github.com/Pramilashanmugam/to-do-list/assets/150790058/7efb940a-c1cd-4fef-9528-bf1a2a8eff23)

* Invalid date
![Screenshot 2024-03-13 12 32 27 PM](https://github.com/Pramilashanmugam/to-do-list/assets/150790058/66eb4b18-6635-43ab-bbaa-16aa203ab46f)

* Past date
![Screenshot 2024-03-13 12 33 20 PM](https://github.com/Pramilashanmugam/to-do-list/assets/150790058/0199545b-5729-4482-ae52-423eea065655)

### Exit function:
on choosing exit option, the program end its functionality and displays a bye message as well as instruction to restart the application again.

![Screenshot 2024-03-13 9 55 48 PM](https://github.com/Pramilashanmugam/to-do-list/assets/150790058/7be74f4f-58be-4656-a24a-f642fa02ae0e)

### `Validation`: 

User inputs are validated to ensure task descriptions are not empty and the date entered must be in current and are in the correct format dd/mm/yyyy. It also validates user input on the options to be entered is integer and not any other data type.

Screenshots for validation are already shown in every functions

I have used try and exception in most of the function to catch the invalid datas and simultaneouly displays the error messages should be displayed clearly to guide me in correcting any mistakes

### Libraries used:
- `datetime` from the standard Python library for date and time manipulation.
- `Fore` from the Colorama library for terminal color formatting.
- `tabulate` from the Tabulate library for displaying data in tabular format.
- `gspread` for interacting with Google Sheets.
- `Coloroma` for text colors
- `Credentials` from the Google OAuth2 library for handling authentication.

### Tools:

- [Lucid Chart](https://www.lucidchart.com/) used to create app flowchart.
- [Google](https://www.google.ie/), [Youtube](https://www.youtube.com/) and [WW3schools](https://www.w3schools.com) used for references to help and solve issues when needed.
- Emoji used to make it more attractive on terminal
- [Code institutes Pep8 linter](https://pep8ci.herokuapp.com/) used to ensure the pep8 style guidelines are followed.
- [Heroku](https://heroku.com/) is used for deployment.

## Features Planned to Implement in Future:

* From single user app to be extend to multiple users.
* The task to get updated with the time.
* The task to get linked to calendar.

## Testing:

### [Please click this link to view the testing file  ](TESTING.md)

## PageSpeedInsight Result:

![Screenshot 2024-03-13 5 53 40 PM](https://github.com/Pramilashanmugam/to-do-list/assets/150790058/14017b1d-35ee-48b6-bdf2-0fefe71acaa6)

## Deployment:

### Heroku Deployment

This application was created using the [Code Institute Python Essentials Template](https://github.com/Code-Institute-Org/p3-template). This template creates a webpage based template that can run python code. For the application to run using the template, the follow changes need to be made to the python code.

1. The newline char(\n) must be added at the end of the text inside all occurrences of the input method, e.g. data=input("text\n")
2. The requirements.txt must be populated with a list of dependencies that the project needs to run. This can be done using the terminal command pip3 freeze > requirements.txt

This application was deployed on Heroku using the following steps,

1. Create a Heroku account and log in.
2. Select create new app from the dashboard.
3. Enter a name for the app, select a region and press create app.
4. From the app homepage select settings.
5. Select reveal config vars.
6. Add a config var with a key and a value.
7. Optional - If using google sheets create a config var with a key of CREDS. For the value, paste in the credentials for the google sheet used by the app. For this project a CREDS variable was created using the contents of the creds.json file.
8. From settings select add build pack, select python from the pop up window and press add buildpack.
9. From settings select add build pack, select nodejs from the pop up window and press add buildpack.
10. Select the deploy section from the app homepage.
11. Select Github as the deployment method and connect to Github.
12. In the search bar, enter the name of the repo used for the app and click search.
13. Press connect to link the Heroku app to the repo.
14. Deploy using automatic or manual deployment options at the bottom of the deploy section.

### Local Deployment:
* The site is created using the Gitpod IDE and then added and commited to git. Later pushed to github.
* The following git commands were used throughout development to push code to the remote repo:
  * git add <file>/.- This command was used to add the file(s) to the staging area before they are committed.
  * git commit -m “commit message” - This command was used to commit changes to the local repository queue ready for the final step.
  * git push - This command was used to push all committed code to the remote repository on github.

### How to Fork

To fork this repository,

1. Log into or signup at [Github](https://github.com).
2. Select the repository for this app.
3. Click the fork button (upper right).

### How to Clone

To clone this repository,

1. Log into or signup at [Github](https://github.com).
2. Select the repository for this app
3. Click the green code button (upper right).
4. Copy the URL using the copy button.
5. Open the terminal in your editor (or of your choosing) and move to the directory which you want to clone to.
6. Type git clone and paste the repository link, then press enter.

## Credits

I would like to give credit to the study materials i used in Google and youtubes for accomplishing this project

* [Shaun Halverson Youtube channel](https://www.youtube.com/watch?v=aEIHZDv_23U)
* [W3schools](https://www.w3schools.com/python/default.asp)
* [Error makes clever academy, a Youtube python tutorial channel](https://www.youtube.com/watch?v=m67-bOpOoPU&t=1679s)
* Love Sandwich Walkthrough project. I have used the google sheet for my datas to get stored as it was guided in the walkthrough tutorial.

## Acknowledgement:

* I would like to acknowledge my mentor `Rory Patrick` his continuous support and guidance during this project.
* Also members from Slack team, who answered my questions when support was needed.




