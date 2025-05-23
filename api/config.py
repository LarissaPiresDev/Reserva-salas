import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['HOST'] = '0.0.0.0'
app.config['PORT']=5001
app.config['DEBUG'] = True
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///reservas.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)