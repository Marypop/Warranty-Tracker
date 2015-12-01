#!/usr/local/bin/python3


# This file should contain all the routes that will be called in the warranty tracker web-application
from application import WarrantyApp
from flask import render_template, request, url_for, redirect
from appUserDB import *

# Default home screen route
warApp = WarrantyApp()
app = warApp.app


# This will be the home screen of the app
@app.route('/')
@app.route('/index')
def index():
    return(render_template('index.html'))


# This route will get executed while user is logged in the app
@app.route('/home')
def home():
    return(render_template('user_screen.html'))


@app.route('/login', methods=['POST'])
def userAppLogin():
    # We should not ideally check for the method, since only allowed method is 'POST'.But still to be
    # safe and to maintain sanity in flask coding convention, we will do it :)
    if(request.method == 'POST'):
        userid = request.form['email']
        pwd = request.form['passwd']
        appuser = AppUserDB(userid, pwd)

    can_login = appuser.validate_user(userid, pwd)

    if can_login:
        redirect_url = 'home'
    else:
        redirect_url = 'index'

    return(redirect(url_for(redirect_url), code=302))


@app.route('/register', methods=['POST'])
def addNewAppUser():
    if(request.method == 'POST'):
        userid = request.form['email']
        pwd = request.form['passwd']
        conf_pwd = request.form['cnfpasswd']

    if(pwd == conf_pwd):
        appusr = AppUserDB(userid, pwd)
    else:
        return(redirect(url_for('index'), code=302))

    created_usr = appusr.add_new_user()

    if created_usr is not None:
        redirect_url = 'home'
    else:
        redirect_url = 'index'

    return(redirect(url_for(redirect_url), code=302))

