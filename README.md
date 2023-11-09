# Project Overview
This is a web app for my Personal Portfolio Website.

# Features and Functionality
## Pages (Sections)
- About Me
- Skills 
- Projects
- Contact Information

## Installation
- Clone the project to your machine
- Run the command below in the project's root directory to activate the project's virtual environment (virtualenv)
```bash
$ source ./venv/bin/activate
```
- Run the following command to install the Python packages used in this project 
```bash
$ pip install -r requirements.txt
```
- Create a `.env` file at the root directory of the project and fill it with the contents below. (NB. Remember to replace the values in square brackets with your own values. A sample can be found in [.env.example](.env.example) file)
```bash
MAIL_USERNAME=[your-email@gmail.com]
MAIL_PASSWORD=[you-gmail-app-secure-password]
FLASH_SECRET_KEY=[your-secret-key]
```
## Running the Application
```bash
$ python app.py
```

# Technologies Used
- Flask (Python3 with Virtualenv)
- HTML
- CSS
- Javascript

# Screenshots or Demo
1. [Flow chart](./my_personal_portfolio_flow_chart.png)
2. [Low fidelity design](./my_personal_portfolio_low_fidelity_design.png)

# Roadmap and future enhancements
- Adding loader to the button when submitting contact information and message
- Enabling scrolling to exact position when the navigation link are clicked
- Adding my custom log in the top navigation bar instead of the name initials 

# Contact information
- <a href="https://github.com/AdongoJr2" target="_blank">GitHub</a>
- <a href="https://linkedin.com/in/moses-adongo-754b201b8" target="_blank">LinkedIn</a>
- <a href="https://twitter.com/mosesadongo23" target="_blank">Twitter</a>
