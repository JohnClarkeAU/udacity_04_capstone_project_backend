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
pip install SQLAlchemy
pip install Flask-SQLAlchemy
pip install Flask-Cors
pip install jose
```

---
## Start your Postgres Database server

### Postgres Database admin using laragon 

#### Start the laragon app

Click the `Start All` button to start the web server and the postgress database server

#### Load `pgadmin` the postgres admin interface

Choose `Menu -> PostgresSQL -> pgAdmin 4`

---
## Configuring the server

### Run from the src directory

Ensure that you are in the `src` directory before trying to configure and run the server.

```bash
cd src
```

### Configure the logging level

In the `src` and `src/auth` directories review the `logfile.conf` files and amend as necessary.  

You will normally just need to set the logging level by changing the default level of INFO to one of the following:

    CRITICAL
    ERROR
    WARNING
    INFO
    DEBUG

### Set the Authorization Environment Variables

The following authorization variables need to be set up to conform with the settings you set up at Auth0.
For example:

```bash
export AUTH0_DOMAIN="yourdomain.au.auth0.com"
export API_AUDIENCE="yourproject"
export ALGORITHM="RS256"
```

---
## Running the server

Before running up the server ensure that you are in the `src` directory and that you are working using your created virtual environment.

Each time you open a new terminal session you need to export the environment variables.

To tell Flask which module to run (you only need to do this once per terminal session):

```bash
export FLASK_APP=api.py;
```

To run the server, execute:

```bash
flask run --reload
```

The `--reload` flag will detect and source file changes and restart the server automatically.

To stop the server press CTRL+C

---

## Testing Pre-requisits

The backend uses the Auth0 authentication system to check that the user has the necessary permission to perform the various tasks.

When running the frontend application the logging on and storage of credentials is done by asking the user to log in, which redirects to Auth0 and stores the returned JWT token so you do not need to manually get the JWT tokens.

To test the backend without using the frontend application you will need to get a JWT token manually and either store it as an environment variable for use within your cURL requests or store it in the Postman configuration.

The process to manually get the JWT token and store it is described below.

### To manually get a JWT token

Open a terminal session and set the environment variables to be used to get a JWT token.

```bash
export YOUR_DOMAIN="yourdomain.au.auth0.com"
export YOUR_API_IDENTIFIER="yourproject"
export YOUR_CLIENT_ID="DB....MoS"
export YOUR_CALLBACK_URI="http://localhost:8080/login-results"
```

Open a web browser in incognito mode and use the following URL template to log in as a user and get a token.  (Note that you must use incognito mode or the browser will just renew the token without displaying it in the URL bar.)

Use the following template to create the URL required.

```bash
https://{{YOUR_DOMAIN}}/authorize?audience={{YOUR_API_IDENTIFIER}}&response_type=token&client_id={{YOUR_CLIENT_ID}}&redirect_uri={{YOUR_CALLBACK_URI}}
```

For example:

```bash
https://yourdomain.au.auth0.com/authorize?audience=yourproject&response_type=token&client_id=DB....MoS&redirect_uri=http://localhost:8080/login-results
```

The browser will attempt to redirect to the redirect_uri (which will not be found) with various parameters which will be displayed in the browser's URL field.  From here you can extract the JWT access token.

```
http://localhost:8080/login-results#access_token=eyJ...PoQ&expires_in=86400&token_type=Bearer
```

If you are testing with cURL you will need to set environment variables to contain the JWT token and your backend test host address, as shown below.

```bash
export TEST_TOKEN="eyJ...PoQ"

export TEST_HOST="http://127.0.0.1:5000"
```

---
## Check the Server is running
You can now ensure that the backend server is running correctly by trying a simple enquiry.

Using your browser navigate to:

```
http://127.0.0.1:5000/
```

You should see the response:
```
Welcome to AbiMath
```

---
## Base URL
At present this app can only be run locally and is not hosted as a base URL. 

The backend app is hosted at the default, http://127.0.0.1:5000/

The following API documentation assumes that the base URL has been set as an environment variable as follows:

```bash
export TEST_HOST="http://127.0.0.1:5000"
```

---
## Errors
Errors are returned as JSON objects in the following format:
```json
{
    "success": false, 
    "error": 400,
    "message": "bad request"
}
```

### Error Index
The following error types can be returned by the API when requests fail:
```
200 Good response
400 Bad Request
404 Not Found
405 Method Not Allowed
422 Unprocessable, usually a database access error
500 Internal Error
```

---
## Endpoints

### Endpoints Index
The following endpoints are accepted by the API

    GET    '/'                       # Gets a welcome message
    GET    '/students'               # Gets a list of students in short format
    GET    '/students-detail'        # Gets a list of students in long format
    GET    '/students/<students_id>' # Gets a student in long format
    POST   '/students'               # Adds a new student in long format
    PATCH  '/students/<students_id>' # Amends a student
    DELETE '/students/<students_id>' # Deletes a student

---
### GET '/'
Accesses the home page of the backend which just displays "Welcome to AbiMath".
This is normally just used to check if the web server is responding correctly.

#### curl
```bash
curl ${TEST_HOST}/
```
#### response
```
Welcome to AbiMath
```
#### errors
```
none
```
---
### GET '/students'
GET /students is a public endpoint returning a list of students.

This is used to get a list of students in the student.short() data format
and is used to display the names and class_id of the students.

#### curl
```bash
curl ${TEST_HOST}/students
```
#### response
```json
{"students":[{"class_id":1,"id":1,"name":"Test Student1 Class1"},{"class_id":1,"id":2,"name":"Test Student2 Class1"},{"class_id":2,"id":3,"name":"Test Student3 Class2"}],"success":true}
```
#### errors
```json
{
    "error": 404,
    "message": "404 Not Found: There are no students",
    "success": false
}

{
    "error": 404,
    "message": "422 Unexpected error accessing the database.",
    "success": false
}
```

---
### GET '/students-detail'
GET /students-detail is a protected endpoint returning a list of students.

This is used to get a list of students in the student.long() data format
and is used to display the results for each of the students.

Requires the 'get:students-detail' permission.

Returns

    status code 200 and json {"success": True, "students": students}
        where students is the list of students in the student.long() data format
    status code 400 if there are no permissions in the JWT
    status code 401 if the user does not have permission to do this
    status code 404 if there are no students
    status code 422 if there is a database error

#### curl
```bash
curl  ${TEST_HOST}/students-detail -H 'Accept: application/json' -H "Authorization: Bearer ${TEST_TOKEN}"

```
#### response
```json
{
    "students":
    [
        {
            "id":1,
            "class_id":1,
            "name":"Test Student1 Class1",
            "addresults":[[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]],
            "divresults":[[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]],
            "mulresults":[[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]],
            "subresults":[[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]]
        },
        {
            "id":2,
            "class_id":1,
            "name":"Test Student2 Class1",
            "addresults":[[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]],
            "divresults":[[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]],
            "mulresults":[[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]],
            "subresults":[[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]]
        },
    ],
    "success":true
}
```

#### errors
```json
{
  "error":401,
  "message":"Authorization header is expected.",
  "success":false
}

{
  "error":401,
  "message":"Token expired.",
  "success":false
}

{
  "error": 404,
  "message": "404 Not Found: There are no students",
  "success": false
}
```

---
### GET '/students/\<id>'
    GET /students/<id> is a protected endpoint to get the corresponding row for <id>.

    This is used to access a specific student in the students table using the <id>
    supplied.

    A student with the same <id> must already be in the students table otherwise a
    404 error is returned if <id> is not found in the students table.

    Requires the 'get:students-detail' permission.

    Returns
        status code 200 and json {"success": True, "students": student}
            where student is an array containing only the requested student
        status code 400 if there is an error in the submitted data
        status code 400 if there are no permissions in the JWT
        status code 401 if the user does not have permission to do this
        status code 404 if <id> is not found in the database
        status code 422 if there is a database error


#### curl
```bash
curl  ${TEST_HOST}/students/<id> -H 'Accept: application/json' -H "Authorization: Bearer ${TEST_TOKEN}"

#### response
```json
{
    "students":
    [
        {
            "id":1,
            "class_id":1,
            "name":"Test Student1 Class1",
            "addresults":[[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]],
            "divresults":[[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]],
            "mulresults":[[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]],
            "subresults":[[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]]
        }
    ],
    "success":true
}
```

#### errors
```json
{
  "error":401,
  "message":"Authorization header is expected.",
  "success":false
}

{
  "error":401,
  "message":"Token expired.",
  "success":false
}

{
  "error": 404,
  "message": "404 Not Found: There are no students",
  "success": false
}
```

---
### DELETE '/students/<id>'

DELETE /students/<id> is an endpoint to delete the existing row for <id>.

This is used to delete a student from the students table using the <id>
supplied.

A student with the same <id> must already be in the students table otherwise a
404 error is returned if <id> is not found in the students table.

Requires the 'delete:students' permission.

Returns

    status code 200 and json {"success": True, "delete": id}
        where id is the id of the deleted record
    status code 400 if there are no permissions in the JWT
    status code 401 if the user does not have permission to do this
    status code 404 if <id> is not found in the database
    status code 422 if there is a database error

#### curl to to delete a student
```bash
curl -X DELETE ${TEST_HOST}/students/1 -H 'Accept: application/json' -H "Authorization: Bearer ${TEST_TOKEN}"
```

#### response
```json
{
  "delete":1,
  "success":true
}
```

---
### POST '/students'
POST /students is an endpoint to create a new row in the students table.

This is used to add a new student to the students table using the data
supplied in the student.long() data representation.

A student with the same title must not already be in the students table.

Requires the 'post:students' permission.

Returns

    status code 200 and json {"success": True, "students": student}
        where student is an array containing only the newly created student
    status code 400 if there is an error in the submitted data
    status code 400 if there are no permissions in the JWT
    status code 401 if the user does not have the required permission
    status code 422 if there is a database error

#### curl to to add a student
```bash
curl -X POST ${TEST_HOST}/students -H 'Accept: application/json' -H "Authorization: Bearer ${TEST_TOKEN}" -H "Content-Type:application/json" -d '{"class_id":1,"name":"Test POSTED Student4 Class1"}'

curl -X POST ${TEST_HOST}/students -H 'Accept: application/json' -H "Authorization: Bearer ${TEST_TOKEN}" -H "Cont
ent-Type:application/json" -d '{"title":"Water3","recipe":[{"name":"Water","color":"blue","parts":1}]}'
```
#### response
```json
{
  "students":[
    {
      "id":3,
      "recipe":[
        {
          "color":"blue",
          "name":"Water",
          "parts":1
        }
      ],
      "title":"Water3"
    }
  ],
  "success":true
}
```
#### curl to generate an error
The students details are not supplied
```bash
curl  -X POST ${TEST_HOST}/students -H 'Accept: application/json' -H "Authorization: Bearer ${TEST_TOKEN}"
```
#### error response
```json
{
  "error":400,
  "message":"400 Bad Request: Missing input field(s). (title and recipe are required.)",
  "success":false
}
```
#### other errors
```json
{
    "error": 400,
    "message": "400 Bad Request: Cannot add 'Water3'. That student already exists in the datbase.",
    "success": false
}```

---
