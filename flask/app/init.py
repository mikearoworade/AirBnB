#!/usr/bin/python3
from flask import Flask, jsonify, request
from sqlalchemy import Column, Integer, Float, String 
from flask_sqlalchemy import SQLAlchemy
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import JWTManager


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///country.db'
app.config['JWT_SECRET_KEY'] = 'secret_key'
db = SQLAlchemy(app)
auth = HTTPBasicAuth()
jwt = JWTManager(app)


from app.controllers import country_controller
from app import commands
from app.controllers import user_controller