from flask import Flask
from flask.ext.bootstrap import Bootstrap


app_var = Flask(__name__)
bootsrap_var = Bootstrap(app_var)

from app import views


