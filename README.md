# Project Overview
This is a simple Task Management web application for users based on this design.

# Features and Functionality
## Features
- Authentication
  - Signup 
  - Login
  - Logout
- Task Management
  - Adding Tasks
  - Updating Tasks
  - Deleting Tasks
  - Filtering Tasks by Category and/or Date
  - Marking tasks as complete/not complete

## Installation
- Run the command below in the projet's directory to activate the project's virtueal environment (virtualenv)
```bash
$ source ./venv/bin/activate
```
- Run the following command to install the Pyhton packages used in this project 
```bash
$ pip install -r requirements.txt
```
- Create a `.env` file at the root directory of the project and fill t with the contents below. (NB. Remember to replace the values in square brackets with your own values. A sample can be found in [.env.example](.env.example) file)
```bash
ACCESS_TOKEN_SECRET=
```
## Running the Application
```bash
$ python app.py
```

# Technologies Used
- Flask (Python with Virtualenv)
- MySQL
- HTML
- CSS
- Javascript

# Screenshots or Demo

# Roadmap and future enhancements

# Contact information
- GitHub - <a href="https://github.com/AdongoJr2" target="_blank">AdongoJr2</a>
