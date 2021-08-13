import os
from sqlalchemy import Column, String, Integer, JSON
from flask_sqlalchemy import SQLAlchemy
import json

from sqlalchemy.sql.sqltypes import JSON

database_filename = "database.db"
project_dir = os.path.dirname(os.path.abspath(__file__))
database_path = "sqlite:///{}".format(os.path.join(project_dir, database_filename))

db = SQLAlchemy()

def setup_db(app):
    '''
    Binds a flask application and a SQLAlchemy service.
    '''
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)

def db_drop_and_create_all():
    '''
    Drops the database tables and starts a fresh database.

    Can be used to initialize a clean the database.
    Two dummy students are inserted to the student table for testing.

    !!NOTE you can change the database_filename variable to have
    multiple versions of a database
    '''
    db.drop_all()
    db.create_all()

    # set up a table of results set to zero
    w = 10
    h = 10
    results = [[0 for x in range(w)] for y in range(h)]

    # insert two dummy classes for testing
    class_name = 'Test Class1 Unallocated'
    schoolclass = Class(
        classname=class_name,
        addresults = results,
        subresults = results,
        mulresults = results,
        divresults = results
    )
    schoolclass.insert()

    class_name = 'Test Class2'
    schoolclass = Class(
        classname=class_name,
        addresults = results,
        subresults = results,
        mulresults = results,
        divresults = results
    )
    schoolclass.insert()

    # insert three dummy students for testing
    student_name = 'Test Student1 Class1'
    student = Student(
        class_id = 1,
        name=student_name,
        addresults = results,
        subresults = results,
        mulresults = results,
        divresults = results
    )
    student.insert()

    student_name = 'Test Student2 Class1'
    student = Student(
        class_id = 1,
        name=student_name,
        addresults = results,
        subresults = results,
        mulresults = results,
        divresults = results
    )
    student.insert()

    student_name = 'Test Student3 Class2'
    student = Student(
        class_id = 2,
        name=student_name,
        addresults = results,
        subresults = results,
        mulresults = results,
        divresults = results
    )
    student.insert()

def db_rollback():
    '''
    Rollbacks the database in the event of an error while updating/deleting
    '''
    db.session.rollback()


class Class(db.Model):
    '''
    Class - a persistent Class entity, extends the base SQLAlchemy Model.
    '''
    # Autoincrementing, unique primary key
    id = Column(Integer().with_variant(Integer, "sqlite"), primary_key=True)
    # String Name
    classname = Column(String(80), unique=True)
    classmembers = db.relationship('Student', backref="schoolclass", lazy=True)
    # the results
    # the required datatype is a two dimension list representing processing two numbers together
    # [ [1+1, 1+2, 1+3, ...], [2+1, 2+2, 2+3, ...], etc]
    addresults =  Column(JSON, nullable=False)
    subresults =  Column(JSON, nullable=False)
    mulresults =  Column(JSON, nullable=False)
    divresults =  Column(JSON, nullable=False)

    def short(self):
        '''
        Short form representation of the Class model
        '''
        return {
            'id': self.id,
            'name': self.classname
        }

    def long(self):
        '''
        Long form representation of the Class model
        '''
        return {
            'id': self.id,
            'name': self.classname,
            'addresults': self.addresults,
            'subresults': self.subresults,
            'mulresults': self.mulresults,
            'divresults': self.divresults
        }

    def insert(self):
        '''
        Inserts a new model into a database.

        The model must have a unique name.
        The model must have a unique id or null id

        EXAMPLE
            schoolclass = Class(name=req_name, addresults=req_addresults)
            schoolclass.insert()
        '''
        db.session.add(self)
        db.session.commit()

    def update(self):
        '''
        Updates a new model into a database.

        The model must exist in the database.

        EXAMPLE
            schoolclass = Class.query.filter(Class.id == id).one_or_none()
            schoolclass.classname = 'Updated Class Name'
            schoolclass.update()
        '''
        db.session.commit()

    def delete(self):
        '''
        Deletes a new model into a database.

        The model must exist in the database.

        EXAMPLE
            schoolclass = Class.query.filter(Class.id == id).one_or_none()
            if schoolclass is not None:
                schoolclass.delete()
        '''
        db.session.delete(self)
        db.session.commit()


class Student(db.Model):
    '''
    Student - a persistent Student entity, extends the base SQLAlchemy Model.
    '''
    # Autoincrementing, unique primary key
    id = Column(Integer().with_variant(Integer, "sqlite"), primary_key=True)
    class_id = Column(Integer().with_variant(Integer, "sqlite"), db.ForeignKey('class.id'), nullable=False)
    # String Name
    name = Column(String(80), unique=True)
    # the results
    # the required datatype is a two dimension list representing processing two numbers together
    # [ [1+1, 1+2, 1+3, ...], [2+1, 2+2, 2+3, ...], etc]
    addresults =  Column(JSON, nullable=False)
    subresults =  Column(JSON, nullable=False)
    mulresults =  Column(JSON, nullable=False)
    divresults =  Column(JSON, nullable=False)

    def short(self):
        '''
        Short form representation of the Student model
        '''
        return {
            'id': self.id,
            'class_id': self.class_id,
            'name': self.name
        }

    def long(self):
        '''
        Long form representation of the Student model
        '''
        return {
            'id': self.id,
            'class_id': self.class_id,
            'name': self.name,
            'addresults': self.addresults,
            'subresults': self.subresults,
            'mulresults': self.mulresults,
            'divresults': self.divresults
        }

    def insert(self):
        '''
        Inserts a new model into a database.

        The model must have a unique name.
        The model must have a unique id or null id

        EXAMPLE
            student = Student(name=req_name, addresults=req_addresults)
            student.insert()
        '''
        db.session.add(self)
        db.session.commit()

    def update(self):
        '''
        Updates a new model into a database.

        The model must exist in the database.

        EXAMPLE
            student = Student.query.filter(Student.id == id).one_or_none()
            student.name = 'Updated Name'
            student.update()
        '''
        db.session.commit()

    def delete(self):
        '''
        Deletes a new model into a database.

        The model must exist in the database.

        EXAMPLE
            student = Student.query.filter(Student.id == id).one_or_none()
            if student is not None:
                student.delete()
        '''
        db.session.delete(self)
        db.session.commit()
