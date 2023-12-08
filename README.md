# Django Demo Backend Project
### This is a _demo backend_, we can start any Django Backend Project from this setup.

You can also check my other repositories on My [GitHub Account](https://github.com/suksham98/)

I will be creating common functions which can be used in any project, Like:
1. Signup
1. Login 
1. Image Upload
1. Sending Email,
1. Custom User Model
1. Database Connectivity
1. User Authentication etc. 

#### Important commands of this setup:
- First you need to activate the virtual environment by the following command:-
  - source venv/Scripts/activate (for windows)    
  - source venv/bin/activate (for ubuntu)
- Change working directory to itwavesecom, then all following commands will work:-
- To run the project:
  - python manage.py runserver
- To add any other dependency:
  - python -m pip freeze > requirements/base.txt
- To install all the dependecies:
  - python -m pip install -r requirements/base.txt

_The last 2 commands are for the base file settings, if you want to add or install dependencies for different development or production settings, you would need to replace base.txt with dev.txt or prod.txt accordingly._

