-------------------------------
RESOURCES

Scrapy vs beautifulsoup
https://hexfox.com/p/scrapy-vs-beautifulsoup/

FLASK
https://realpython.com/blog/python/flask-by-example-part-2-postgres-sqlalchemy-and-alembic/

POSTGRES
https://www.digitalocean.com/community/tutorials/how-to-install-and-use-postgresql-on-ubuntu-16-04

flask
https://pythonspot.com/en/flask-web-app-with-python/

flask to docker
http://containertutorials.com/docker-compose/flask-compose.html

flask and postgres
https://www.theodo.fr/blog/2017/03/developping-a-flask-web-app-with-a-postresql-database-making-all-the-possible-errors/
http://newcoder.io/scrape/intro/
http://blog.sahildiwan.com/posts/flask-and-postgresql-app-deployed-on-heroku/
http://www.vertabelo.com/blog/technical-articles/web-app-development-with-flask-sqlalchemy-bootstrap-part-2

Directory structures for large flask apps

https://www.digitalocean.com/community/tutorials/
how-to-structure-large-flask-applications

http://exploreflask.com/en/latest/organizing.html
---------------------------------------------------------
PREPARE OPERATING SYSTEM
Off of a fresh ubuntu 16.04

$ sudo apt-get update
$ sudo apt-get upgrade

1. Install Pycharm, git, virtualenvwrapper, python-dev, pip

$ sudo add-apt-repository ppa:mystic-mirage/pycharm
$ sudo apt update
$ sudo apt install pycharm-community
$ sudo apt install git
$ git config --global user.name “francisglee”
$ git config --global user.email “francis.g.lee@gmail.com”
$ git config --global push.default simple
$ git config --global credential.helper cache
$ sudo apt install python-dev
$ sudo apt-get install python-pip
$ sudo -H pip install --upgrade pip
$ sudo -H pip install virtualenvwrapper

4. Create app directory:

$ mkdir github
$ cd github
$ mkdir foods-app-database
$ cd food-app-database

5. Switch from python2 to python3 in ~/.bashrc

$ echo "alias python=python3" >> ~/.bashrc
$ echo "alias charm=pycharm-community" >> ~/.bashrc
$ source ~/.bashrc
$ python --version
----------------------------------------------------------
GETTING DATABASE UP AND RUNNING

1. Install Postgres

$ sudo apt-get update
$ sudo apt-get upgrade
$ sudo apt-get install postgresql postgresql-contrib libpq-dev

2. Create database

$ sudo -i -u postgres psql
postgres$ ALTER USER postgres WITH PASSWORD 'password';
postgres$ CREATE USER ifrancium WITH PASSWORD 'password';
postgres$ CREATE DATABASE usda OWNER ifrancium ENCODING 'utf-8';
-------------------------------------------------------------
CREATE APP

1. Initialize git and virtual environment

$ git init
$ mkvirtualenv --python=/usr/bin/python3 food-env
# Activate env: workon food-env

2. Install python packages

$ pip install Flask psycopg2 Flask-SQLAlchemy Flask-Migrate
$ pip freeze > requirements.txt

4. Create File structure

$ touch run.py setup.py .gitignore README.md
$ mkdir instance app docs tests api
$ cd app
$ touch __init__.py config.py app.py views.py models.py forms.py utils.py manage.py scrape.py
$ mkdir static templates
$ cd templates
$ touch index.html
$ cd ~/foods-app-database/app/static
$ mkdir css js
$ cd css
$ touch style.css bootstrap.css
$ cd ~/foods-app-database/app/static/js
$ touch style.js bootstrap.js

5.

-------------------------------
INITIALIZE DATABASE

1. initialize database

$ python manage.py db init
$ python manage.py db migrate
$ python manage.py db upgrade


DIRECTORY STRUCTURE

foods-database
├── requirements.txt # This file lists all of the Python packages that your app depends on. You may have separate files for production and dev dep.
├── run.py # This is the file that is invoked to start up a development server. It gets a copy of the app from your package and runs it. This won't be used in production, but it will see a lot of mileage in development.
├── setup.py # like __init__.py for the larger application (functions as .env or .envrc)
├── instance
     └── config.py # This file contains configuration variables that shouldn't be in version control. This includes things like API keys and database URIs containing passwords. This also contains variables that are specific to this particular instance of your application. For example, you might have DEBUG = False in config.py, but set DEBUG = True in instance/config.py on your local machine for development. Since this file will be read in after config.py, it will override it and set DEBUG = True.
├── app # This is the package that contains your application.
     ├── __init__.py # This file initializes your application and brings together all of the various components.
     ├── config.py # This file contains most of the configuration variables that your app needs.
     ├── app.py # This file contains apps and routes; this gets split up into a bunch of different files
     ├── views.py # This is where the routes are defined. It may be split into a package of its own (yourapp/views/) with related views grouped together into modules.  Also can be referred to as controller.py
     ├── models.py # This is where you define the models of your application. This may be split into several modules in the same way as views.py.
     ├── forms.py # for security (WTForms, CSRF, SecureForms, reCAPTCHA)
     ├── static # This directory contains the public CSS, JavaScript, images and other files that you want to make public via your app. It is accessible from yourapp.com/static/ by default.
           ├── css
                ├── style.css
                └── bootstrap.css
           └── js
                ├── style.js
                └── bootstrap.js
     ├── templates # This is where you'll put the Jinja2 templates for your app.
           └── index.html
     └── manage.py # run database initiation, migrations and upgrades
├── docs
     ├── jupyter-notebooks
     ├── installation.md
     ├── develop.md
     └── api.md
├── .gitignore
├── tests
├── utility
     ├── utils.py # python class wrappers
     └── scrape.py # contains functions for webscraping
├── api
├── DOCKERFILE
└── README.md


