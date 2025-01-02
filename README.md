##
# Django : 
## 1. Ridiculously fast
## 2. Ressuringly secure 
## 3. Exceeding  scalable 


```
Easier to build better application 
more quickliy with less code.

1. create virtual env 
> python3 -m venv  .venv or
> virtualenv myenv

1.1  create venv using uv at .venv 
> uv venv .venv
```
# uv [package manager]
## it is extremely fast package manager written in rust 

## To activate virtual env ::
> source .venv/bin/activate

## To De-activate virtual env ::
> deactivate

> cd chaiaurDjango
> pip install django


> python3 manage.py runserver

# JINJA [django Template Language ]
## fast, customizable template language 

* variable in {{var }}


> python3 manage.py startapp chai

it create another folder name as chai 
* After making app ,to make aware main project to know the app
* Go to setting.py file > add installed apps
* App properly intalled and configured. 
* Each app itself a stand-alone app
which can have their own templates ans static folders 

> ctrl + comma 

## views 

# django tailwind 
> python -m pip install --upgrade pip

> python -m pip ensurepip --upgrade 

> python -m pip install django-tailwind

> python -m pip install 'django-tailwind[reload]'

* Add tailwind to setting (Installed apps)
>  python3 manage.py tailwind init
* Add theme to setting (Installed apps)

Install tailwind through  manage.py
> python3 manage.py tailwind install 

** create another terminal to generate tailwind in .venv
> source .venv/bin/activate

## to start tailwind start in another terminal 
> python3 manage.py tailwind start

## for production 
> python3 manage.py tailwind build

## In settings add npm bin path 

* tailwind is node base 
# Setting Configuration  
## Install django_browser_reload
* check docs 

=================================
# Features:
* highly configurable admin panel 
with high compability for all web browser

* It can be madifiable
* we can take django admin template
* It diractly communicate with model 

+++++++++++++++++++++++++++++++++++++++++++++++++++
# Migrations
* it can talk with database, a migration error 
* we cant talk directly with database behalf of that django ORM talk with DB 

commands 
> python3 manage.py migrate 

# Create superuser
> python3 manage.py createsuperuser 

+++++++++++++++++++++++++++++++++++++++++++++++++++++
# Models In Django :
* handle images 
*  Models Interact with DB 
* How models.py & admin.py associate with each other

 # Google :: reset django-admin password
not support directly, required 3rd party plug-in (Pillow)

# Install Pillow :
> python3 -m pip install Pillow

## set media urls and path (main urls )
MEDIA_URLS = '/media/'

MEDIA_ROOTS = [os.path.join(BASE_DIR, 'media')]

in root urls.py 

1. migration ::
create 
> python3 manage.py makemigrations chai 
