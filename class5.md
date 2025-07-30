# Steps for Class 5 

# - local - not for class
- create venv
- activate
- install requirements: python3 -m pip install -r requierements.txt

------------------------

# Roll call and stand up
Welcome students, 
explain that you will give them 5 mins for they to create the plan for the class

## explain your plain
explain that you will create a new app (notes)
and will implement List and Create funcionality
they can follow you or not, is their decission


## Do the roll call
When calling each student, ask then what is the plan for the class
they should tell you what are they planning to work on today


------------------------


# Create Notes app
Explain to student that we will do a notes app as a recap on CRUD funcionality.
They can follow exactly or then can create an app and models for their projects.

## create app
python3 manage.py startapp notes

## register app
register the app on settings.py

## create notes > urls.py
```python

from django.urls import path
from . import views

urlpatterns = [
]

```

## register urls with config > urls
```python
path('notes/', include('notes.urls')),
```

## install pillow
django does not support image on models,
install pillow for that:
python3 -m pip install pillow


## create the model
```python

class Note(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    image = models.ImageField(upload_to="media/notes/", blank=True, null=True)
    file = models.FileField(upload_to="media/files/", blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)

``` 

## make migrations
Explain that every time they change anything on models
they need to run migrations:
python3 manage.py makemigrations
python3 manage.py migrate


## add the model to admin.py
```python

from django.contrib import admin
from . import models

admin.site.register(models.Note)

```

## create a super user
python3 manage.py createsuperuser


## Run it, go to admin and create a few records



------------------------


# Create list view

## create the list view
## create the template
## create the url
## Test: http://127.0.0.1:8000/
## create notes.css
Add some simple rules for it to look better
## Test again


###  Common issue:
if the image is not loading, check config > urls.py
at the end should have:
``` 
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

------------------------


# Create the create view

## create the form
## create the view
## create the template
## create the url
## Test: http://127.0.0.1:8000/notes/create

### common issue:
the image is not being saved because the form is missing the enctype


------------------------

# Students to improve
ask students to dedicate some time to improve the presentation


------------------------


# Rest of the class
the rest of the class is just being there
in case students have any question/issue with their capstone