from flask import Flask, render_template, redirect, current_app
from flask_sqlalchemy import SQLAlchemy
import os, pytest
from flask_login import LoginManager
import pymysql

secret_key = os.urandom(32)

app = Flask(__name__)
        
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost/school'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = secret_key
app.config['UPLOAD_FOLDER'] = "E:/Student Attainment Project/Student Attainment Analyzer/Student-Performance-Analyzer/Student-Performance-Analyzer/Teacher/static/uploads/"
app.config['SAMPLES_FOLDER'] = "E:/Student Attainment Project/Student Attainment Analyzer/Student-Performance-Analyzer/Student-Performance-Analyzer/Teacher/static/samples/"

db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)

from Teacher import routes
