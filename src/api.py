import logging
import logging.config
from flask import Flask, request, jsonify, abort
from sqlalchemy import exc
from flask_cors import CORS

from .database.models import (setup_db)

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

@app.route('/')
def index():
    '''
    GET / is a public endpoint that displays 'Welcome to AbiMath'.

    This is normally just used to check if the web server is responding.

    Returns
        status code 200 and the html text 'Welcome to AbiMath'
    '''
    return 'Welcome to AbiMath\n'

