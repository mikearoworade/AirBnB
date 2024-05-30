#!/usr/bin/python3
from flask import Flask, jsonify, request
from sqlalchemy import Column, Integer, Float, String 
from flask_sqlalchemy import SQLAlchemy
from flask_httpauth import HTTPBasicAuth


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///country.db'
db = SQLAlchemy(app)
auth = HTTPBasicAuth() 

from app.controllers import country_controller
from app import commands
from app.controllers import user_controller
