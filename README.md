# Udacity_04 Capstone Project Backend

## Overview

The project has three tables that store information about teachers, their school classes and students who are in those classes.  There are three types of users being administrators, teachers and students.  Students can upload and view their own achievements.  Teachers can view their classes, class achievements and individual student achievements.  Administrators can set up information and users.

The project demonatrates a full understanding of creating a backend application using Auth(0) for authentication and written in Python making use of the following key dependancies for the main framework, database handling and authorisation.

## Getting Started

### Key Dependencies

- [Flask](http://flask.pocoo.org/)  which is a lightweight backend microservices framework. Flask is required to handle the routing of requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) and [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/) which are libraries to handle the lightweight sqlite database. The heavy lift of the database handling is done in `./src/database/models.py`.

- [jose](https://python-jose.readthedocs.io/en/latest/) JavaScript Object Signing and Encryption for JWTs. This is used for encoding, decoding, and verifying JWTS.

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

Note that this project should be run using Python 3.7 (not the latest version)

#### Virtual Environment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

On Windows 

check that pip is installed

```bash
py -m pip --version
pip 20.1.1 from F:\Program Files\Python3.7.9\lib\site-packages\pip (python 3.7)
```
set up your virtual environment for the project and create a venv directory 

```bash
py -m venv venv
```

##### Activating a virtual environment

Before you can start installing or using packages in your virtual environment you’ll need to activate it. Activating a virtual environment will put the virtual environment-specific python and pip executables into your shell’s PATH.

###### To activate on Windows you can enter

```bash
./venv/Scripts/activate
```
You should see the name of your virtual environment in brackets on your terminal command line e.g.  `(venv)`.

Any python commands you use will now work with your virtual environment

###### To activate when using vscode

For more information about using Python in VSCode please refer to:
https://code.visualstudio.com/docs/python/environments 

Open vscode in your project folder that contains your venv folder.
Then open Python Terminal `(Ctrl + Shift + P: Python: Create Terminal)` and you'll see that venv is getting picked up; e.g.: `(venv)` ...

Any python commands you use will now work with your virtual environment

##### To deactivate the virtual environment

To decativate the virtual environment and use your original Python environment, simply type:

```bash
deactivate
```

##### To keep track of what is installed in the virtual environment 

```bash
pip freeze > requirements.txt
```

Then review the requirements.txt file.

#### PIP Dependencies

You can install the dependancies already specified in `requirements.txt` or install them individually.

##### Install dependancies specified in requirements.txt

Once you have your virtual environment setup and running, navigate to your project directory and install dependencies by running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages that are specified within the `requirements.txt` file.

##### Manually install dependancies

Once you have your virtual environment setup and running, navigate to your project directory and install dependencies by running:

```bash
pip install Flask
pip install 
```

## Start your Postgres Database server

### Postgres Database admin using laragon 

Start the laragon app
Click `Start` All to start the web server and the database server(s)
Choose `Menu -> PostgresSQL -> pgAdmin 4`

