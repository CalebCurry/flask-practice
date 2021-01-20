from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_bcrypt import Bcrypt
import os
app = Flask(__name__)
bcrypt = Bcrypt(app)

# Setup the Flask-JWT-Extended extension
app.config['JWT_SECRET_KEY'] = 'super-secret'  # Change this!
jwt = JWTManager(app)

#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////data.db'
#db = SQLAlchemy(app)

# https://flask-sqlalchemy.palletsprojects.com/en/2.x/config/#connection-uri-format
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://flaskpractice:SXR4Vt3MbFvMqhfDP3IA@flask-practice.cyr69gg58bpb.us-east-2.rds.amazonaws.com/postgres'
#db = SQLAlchemy(app)

DB_NAME = os.environ.get('RDS_DB_NAME')
DB_USER = os.environ.get('RDS_USERNAME')
DB_PASSWORD = os.environ.get('RDS_PASSWORD')
DB_HOSTNAME = os.environ.get('RDS_HOSTNAME')
#DB_PORT = os.environ['RDS_PORT'],

app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOSTNAME}/{DB_NAME}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
from drink_ratings.models import Testimonial
db.create_all()

import drink_ratings.routes
