import logging
import logging.config
from flask import Flask, request, jsonify, abort
from sqlalchemy import exc
from flask_cors import CORS

from .database.models import (Student, setup_db, db_drop_and_create_all, db_rollback)

# Set up the app
app = Flask(__name__)
setup_db(app)
CORS(app)

print("Starting the AbiMath server")

# Set up logging
logging.config.fileConfig(fname='logfile.conf', disable_existing_loggers=False)

# Get the logger specified in the file
logger = logging.getLogger(__name__)
logger.debug('STARTING the AbiMath backend')

'''
@TODO uncomment the following line to initialize the datbase
!! NOTE THIS WILL DROP ALL RECORDS AND START YOUR DB FROM SCRATCH
!! NOTE THIS MUST BE UNCOMMENTED ON FIRST RUN
'''

db_drop_and_create_all()

# ###################################################################
@app.route('/')
def index():
    '''
    GET / is a public endpoint that displays 'Welcome to AbiMath'.

    This is normally just used to check if the web server is responding.

    Returns
        status code 200 and the html text 'Welcome to AbiMath'
    '''
    return 'Welcome to AbiMath\n'

# ###################################################################
@app.route('/students', methods=['GET'])
# @requires_auth('get:students')
# def students(jwt):
def students():
    '''
    GET /students is a public endpoint returning a list of students.

    This is used to get a list of students in the student.short() data format
    and is used to display the names of the students.

    Returns
        status code 200 and json {"success": True, "students": students}
            where students is the list of students
        status code 404 if there are no students
        status code 422 if there is a database error
    '''
    logger.debug('GET /students')
    # get all the students
    try:
        all_students = Student.query.all()
    except Exception as e:
        abort(422, "Unexpected error accessing the database.")

    # return a 404 error if there are no students
    if len(all_students) is 0:
        abort(404, 'There are no students')

    # get the short form of the students list
    students = [student.short() for student in all_students]

    return jsonify({
        'success': True,
        'students': students
    }), 200

# ###################################################################
@app.route('/students-detail', methods=['GET'])
# @requires_auth('get:students')
# def students_detail(jwt):
def students_detail():
    '''
    GET /students is a public endpoint returning a list of students.

    This is used to get a list of students in the student.short() data format
    and is used to display the names of the students.

    Returns
        status code 200 and json {"success": True, "students": students}
            where students is the list of students
        status code 404 if there are no students
        status code 422 if there is a database error
    '''
    logger.debug('GET /students')
    # get all the students
    try:
        all_students = Student.query.all()
    except Exception as e:
        abort(422, "Unexpected error accessing the database.")

    # return a 404 error if there are no students
    if len(all_students) is 0:
        abort(404, 'There are no students')

    # get the short form of the students list
    students = [student.long() for student in all_students]

    return jsonify({
        'success': True,
        'students': students
    }), 200

# ###################################################################
@app.route('/students/<int:id>', methods=['GET'])
# @requires_auth('patch:students')
# def students_patch(jwt, id):
def students_get(id):
    '''
    GET /students/<id> is an endpoint to get the corresponding row for <id>.

    This is used to access a specific student in the students table using the <id>
    supplied.

    A student with the same <id> must already be in the students table otherwise a
    404 error is returned if <id> is not found in the students table.

    Requires the 'get:students' permission.

    Returns
        status code 200 and json {"success": True, "students": student}
            where student is an array containing only the requested student
        status code 400 if there is an error in the submitted data
        status code 400 if there are no permissions in the JWT
        status code 401 if the user does not have permission to do this
        status code 404 if <id> is not found in the database
        status code 422 if there is a database error
    '''
    logger.debug('GET/students/' + str(id))

    # get the student to be returned
    student = Student.query.filter(Student.id == id).one_or_none()
    if student is None:
        abort(404, "id not found in the database.")


    # return the long form of the student just retrieved
    return jsonify({
        'success': True,
        'students': [student.long()]
    }), 200

# ###################################################################
@app.route('/students/<int:id>', methods=['DELETE'])
# @requires_auth('delete:students')
# def students_delete(jwt, id):
def students_delete(id):
    '''
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
    '''
    logger.debug('DELETE/students/' + str(id))

    # get the student to be deleted
    student = Student.query.filter(Student.id == id).one_or_none()
    if student is None:
        abort(404, "id '" + str(id) + "' not found in the database.")
    try:
        # start of a rollbackable transaction
        # delete the student from the database
        student.delete()

        # return the id of the deleted item
        return jsonify({
            'success': True,
            'delete': id
        }), 200

    except Exception as e:
        db_rollback()
        abort(422, "Unexpected error deleting the student from the database.")

# ###################################################################
@app.route('/students', methods=['POST'])
# @requires_auth('post:students')
# def students_create(jwt):
def students_create():
    '''
    POST /students is an endpoint to create a new row in the students table.

    This is used to add a new student to the students table using the data
    supplied in the student.short() data representation.

    A student with the same name must not already be in the students table.

    Requires the 'post:students' permission.

    Returns
        status code 200 and json {"success": True, "students": student}
            where student is an array containing only the newly created student
        status code 400 if there is an error in the submitted data
        status code 400 if there are no permissions in the JWT
        status code 401 if the user does not have the required permission
        status code 422 if there is a database error
    '''
    logger.debug('POST/students')

    # get the input data
    try:
        body = dict(request.form or request.json or request.data)
        new_name = body.get('name', None)
        new_class_id = body.get('class_id', None)
    except Exception as e:
        abort(400, "Invalid input data. (name and class_id are required.)")

    # check that all fields have been submitted
    if new_name is None and new_class_id is None:
        abort(400, "Missing input field(s). (name and class_id are required.)")
    if new_name is None:
        abort(400, "Missing input field(s). (name is required.)")
    if new_class_id is None:
        abort(400, "Missing input field(s). (class_id is required.)")

    # check that none of the fields are blank
    if new_name == '':
        abort(400, description="The name must not be blank.")
    if new_class_id == '':
        abort(400, description="The class_id must not be blank.")

    # ensure that the name is unique
    existing_student = Student.query.filter(Student.name == new_name).one_or_none()
    if existing_student is not None:
        abort(400, description="Cannot add '" + new_name +
              "'. That student already exists in the datbase.")
    try:
        # start of a rollbackable transaction
        # set up a table of results set to zero
        w = 10
        h = 10
        new_results = [[0 for x in range(w)] for y in range(h)]

        # insert the new student
        student = Student(
            name=new_name,
            class_id=new_class_id,
            addresults = new_results,
            subresults = new_results,
            mulresults = new_results,
            divresults = new_results
        )
        student.insert()
        # return the long form of the student just inserted
        return jsonify({
            'success': True,
            'students': [student.long()]
        }), 200
    except Exception as e:
        db_rollback()
        abort(422, "Unexpected error inserting the student into the database.")

