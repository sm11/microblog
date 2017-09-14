from app import app_var
from flask import render_template

@app_var.route('/')
@app_var.route('/index')
def index():
    return render_template('index.html')

@app_var.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)


