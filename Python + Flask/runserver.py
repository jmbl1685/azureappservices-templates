"""
This script runs the FlaskWebProject1 application using a development server.
"""

from os import environ
from src import app
from flask_cors import CORS,cross_origin
from flask_restful import Api, marshal

api = Api(app)
cors = CORS(app)

if __name__ == '__main__':
    HOST = environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)
