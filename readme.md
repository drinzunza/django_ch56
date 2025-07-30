# Important Notes
## Class 1

- Create empty folder and open a terminal
- run the following commands:
    1. Create Virtual Environment: python (or python3) -m venv venv
    2. Activate venv: source venv/bin/activate (MAC and Linux) or ./venv/Scripts/activate (Windows) 
    3. Install django: pip (or pip3) install django
    4. Creating the project: django-admin startproject NAME_OF_THE_PROJECT (common name would be config) .
    5. Add the folder for: templates, media, static
    6. Add the single files: .gitignore and readme.md
    7. Create the apps for the project: python (or python3) manage.py startapp NAME_OF_THE_APP
    8. Add the name of the app inside of setting.py


### Differences between makemigrations and migrate
We have to run always makemigrations first and then migrate
- python (or python3) manage.py makemigrations - this command would detect the changes from all of the models.py and create the migrations files
- python (or python3) manage.py migrate - this command would apply and make the changes to db from the migrations files