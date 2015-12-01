#!/usr/local/bin/python3


# This file should contain all the routes that will be called in the warranty tracker web-application
from application import WarrantyApp
from flask import render_template, request, url_for
from appUserDB import *

# Default home screen route
warApp = WarrantyApp()
app = warApp.app


# This will be the home screen of the app
@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['POST'])
def indexScreen():
    return(render_template('index.html'))


# This route will get executed while user is logged in the app
@app.route('/home/<user_name>')
def displayUserScreen(user_name):
    return(render_template('user_screen.html', user_name=user_name))

@app.route('/login', methods=['POST'])
def userAppLogin():
    # We should not ideally check for the method, since only allowed method is 'POST'.But still to be
    # safe and to maintain sanity in flask coding convention, we will do it :)
    userid = request.form['email']
    pwd = request.form['passwd']

    can_login = validate_user(userid, pwd)
    print(can_login)

    if can_login:
        return(render_template('user_screen.html'))
    else:
        return(render_template('index.html'))
