# importing dependencing libraries
import os, sys, logging
from pathlib import Path

# using While loop for get user input to make project name
while True:
    project_name_get_user = input("Enter your project name: ")
    if project_name_get_user != "":
        break
    
# creating project directory
# project_name/__init__.py
# project_name/components/__init__.py
# project_name/config/__init__.py
# project_name/constants/__init__.py
# project_name/exception/__init__.py
# project_name/logging/__init__.py
# project_name/pipeline/__init__.py
# project_name/utils/__init__.py
# project_name/entity/__init__.py
# config/config.yaml
# schema.yaml
# requirements.txt
# setup.py
# app.py

list_of_file = [
    f"{project_name_get_user}/__init__.py",
    f"{project_name_get_user}/components/__init__.py",
    f"{project_name_get_user}/config/__init__.py",
    f"{project_name_get_user}/constants/__init__.py",
    f"{project_name_get_user}/exception/__init__.py",
    f"{project_name_get_user}/logging/__init__.py",
    f"{project_name_get_user}/pipeline/__init__.py",
    f"{project_name_get_user}/utils/__init__.py",
    f"{project_name_get_user}/entity/__init__.py",
    f"config/config.yaml",
    f"schema.yaml",
    f"requirements.txt",
    f"setup.py",
    f"app.py"
]

# spliting project name to get package name using for loop
for file in list_of_file:
    filepath = Path(file)
    filedir, filename = os.path.split(filepath)

# checking if project name is valid or exsists if condition
    if filedir != "":
        os.makedirs(filedir,exist_ok=True)
        
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath,'w') as f:
            pass

# logging use
    else:
        logging.info('file is already exist',filepath)
        
        
        
        


