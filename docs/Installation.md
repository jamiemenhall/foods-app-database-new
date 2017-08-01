# PREPARE OPERATING SYSTEM
## Off of a fresh ubuntu 16.04

```
$ sudo apt-get update
$ sudo apt-get upgrade
```

1. Install Pycharm, git, virtualenvwrapper, python-dev, pip

```
$ sudo add-apt-repository ppa:mystic-mirage/pycharm
$ sudo apt update
$ sudo apt install pycharm-community
$ sudo apt install git

$ git config --global user.name “jamiemenhall” # set github username
$ git config --global user.email “jamiemehall@mac.com” # set github user email
$ git config --global push.default simple
$ git config --global credential.helper cache # set default password keeper
$ git remote origin https://www.github.com/jamiemenhall/foods-app-database-new
.git # set git remote
$ git remote -v # check git remote

$ sudo apt install python-dev
$ sudo apt-get install python-pip
$ sudo -H pip install --upgrade pip
$ sudo -H pip install virtualenvwrapper
```

2. Create app directory:

```
$ mkdir github
$ cd github
$ mkdir foods-app-database
$ cd food-app-database
```

3. Set aliases in .bashrc

```
$ echo "alias python=python3" >> ~/.bashrc
$ echo "alias charm=pycharm-community" >> ~/.bashrc
$ source ~/.bashrc # restart .bashrc to enable new additions
$ python --version # check python version
```
----------------------------------------------------------
# GETTING DATABASE UP AND RUNNING

1. Install Postgres

```
$ sudo apt-get update
$ sudo apt-get upgrade
$ sudo apt-get install postgresql postgresql-contrib libpq-dev
```

2. Create database

```
$ sudo -i -u postgres psql
postgres$ ALTER USER postgres WITH PASSWORD 'password'; # give master-user, postgres, a password
postgres$ CREATE USER jmenhall WITH PASSWORD 'password'; # create admin user
postgres$ CREATE DATABASE usda OWNER jmenhall ENCODING 'utf-8'; # create 
database
```

-------------------------------------------------------------
# SET UP VIRTUAL ENVIRONMENT

1. Initialize git and virtual environment

```
$ git init
$ mkvirtualenv --python=/usr/bin/python3 food-env
# Activate env: workon food-env
```

2. Install python packages

```
$ pip install Flask psycopg2 Flask-SQLAlchemy Flask-Migrate requests
$ pip freeze > requirements.txt
```

-------------------------------------------------------------
# CREATE FILE STRUCTURE

1. Create File Structure

```
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
```

2. 

-------------------------------
# INITIALIZE DATABASE

1. initialize database

```
$ python manage.py db init
$ python manage.py db migrate
$ python manage.py db upgrade
```