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


### System Requirements:
1. Pending...


### Steps to run the project:
1. Create a new directory where you want clone the project by:
   ```
   mkdir new_project
   ```
2. Change the working directory to new_project by:
   ```
   cd new_project
   ```
3. Clone the project by using command:
   ```
   git clone https://github.com/suksham98/Ecommerce-Backend.git
   ```
4. Create virtual environment by command:
   ```
   python -m venv env
   ```
5. Now, activate virtual environment by command:
  -```
   env/Scripts/activate #(for windows)
  ```
     _if you see error saying:- venv/Scripts/activate : File C:\Users\Lenovo\OneDrive\Desktop\demo_backend\venv\Scripts\Activate.ps1 cannot be loaded because running scripts is disabled on this system. For more information, see about_Execution_Policies at https:/go.microsoft.com/fwlink/?LinkID=135170._
     1. For temporarily bypass the current script execution policy, use command:
        ```
        Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
        ```
     2. For global enable, use command:
       ```
        Set-ExecutionPolicy -ExecutionPolicy RemoteSigned
       ```
        RemoteSigned means that locally created scripts (scripts created on the local machine) can run without being digitally signed.
        And again run the env/Scripts/activate command for successfull activation.
  - ```
  source env/bin/activate #(for ubuntu)
  ```
  Your virtual environment name will be displayed in the terminal/command prompt.
6. Change the working directory to Ecommerce-Backend directory by using command:
   ```
   cd Ecommerce-Backend
   ```
7. Now, to install dependencies or packages that are used in this project, run the following command:
   ```
   python -m pip install -r requirements/base.txt
   ```
8. To check if project is setup correctly or run it, use command:
   ```
   python manage.py runserver
   ```


#### Important commands of this setup:
- First you need to activate the virtual environment by the following command:-
  - venv/Scripts/activate (for windows)    
  - source venv/bin/activate (for ubuntu)
- Change working directory to itwavesecom, then all following commands will work:-
- To run the project:
  - python manage.py runserver
- To add any other dependency:
  - python -m pip freeze > requirements/base.txt
- To install all the dependecies:
  - python -m pip install -r requirements/base.txt

_The last 2 commands are for the base file settings, if you want to add or install dependencies for different development or production settings, you would need to replace base.txt with dev.txt or prod.txt accordingly._

