## Making the virtual env for python
pip install pipenv
pipenv shall 
pipenv install django

## Creating django project 
django-admin startproject todo 

## Project build up 
cd todo 
python3 manage.py runserver 8081
python3 manage.py migrate

## Creating first app 
python3 manage.py startapp tasks