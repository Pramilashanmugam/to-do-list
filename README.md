# To do List app 
## Welcome to my [To do list app](https://my-to-do-list-a8066c712807.herokuapp.com/)

![Screenshot 2024-03-13 10 59 48 AM](https://github.com/Pramilashanmugam/to-do-list/assets/150790058/0f664087-5cc6-453e-a800-710368ccf4c2)


## Introduction:
The purpose of developing this app is to keep track of our current and future appointments/plans. It is very important for each and everyone of us to stay organized and manage our day to day tasks effectively. I believe this app would help us achieve the same.

# Features:

## Technologies:

 * Python
   * This app is fully developed using Python.
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
As a busy Home maker, mother and a student, I want to use a to-do list app to organize my tasks and stay on top of my daily activities. 

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

### Flowchart:

![Screenshot 2024-03-04 11 55 50 AM](https://github.com/Pramilashanmugam/to-do-list/assets/150790058/e7e5d157-0c49-4697-9639-32a4d9576201)

## Existing Features:

### Main features of this app:

* `Adding tasks`: Users can add new tasks with a deadline.
* `Viewing tasks`: Users can view their existing tasks in a list format.
* `Deleting tasks`: Users can delete tasks they no longer need.
* `Updating tasks`: Users can edit existing tasks, by modifying the task description and deadline.
* `Validation`: It validates user inputs to ensure task descriptions are not empty and the date entered must be in current and are in the correct format dd/mm/yyyy. It validates the input 
Error messages should be displayed clearly to guide me in correcting any mistakes

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

* From single user need to extend it to multiple user.

## Testing:

### [Please click this link to view the testing file  ](TESTING.md)

## PageSpeedInsight Result:

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





