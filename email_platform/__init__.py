import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__, template_folder="templates")
app.config.from_mapping(
        SQLALCHEMY_ECHO=True,
        SQLALCHEMY_DATABASE_URI='sqlite:////' + os.path.join(basedir,
            'contacts.db'),
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
)

# Create the SQLAlchemy db instance
db = SQLAlchemy(app)

# Initialize Marshmallow
ma = Marshmallow(app)

import email_platform.index
