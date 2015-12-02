#!/usr/local/bin/python3


# This file should contain all the routes that will be called in the warranty tracker web-application
from application import WarrantyApp
from flask import render_template, request, url_for, redirect, Response, session
from appUserDB import *
import os

# Generate a random secret key and store it with application
secret_key = os.urandom(32)

# Application object initialization
warApp = WarrantyApp()
app = warApp.app
warApp.app.secret_key = secret_key

# Default home screen route
# This will be the home screen of the app
@app.route('/')
@app.route('/index')
def index():
    return(render_template('index.html'))


# This route will get executed while user opens up the homepage for the application
@app.route('/home')
def home():
    return(render_template('user_screen.html'))


# Routes to Log-in existing, Register new user and logging out of the application
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
        session['user'] = userid
    else:
        redirect_url = 'index'

    response = redirect(url_for(redirect_url), code=302)
    return(response)


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


@app.route('/logout', methods=['POST'])
def usrLogout():
    session.clear()
    return(redirect('index', code=302))

# Routes to Add/Delete new devices for a given user
@app.route('/addnewdevice', methods=['POST'])
def addNewDevice():
    if(request.method == 'POST'):
        dvcName = request.form['dvcName']
        dvcType = request.form['dvcType']
        dvcPurDate = request.form['dvcPurDate']
        dvcWarPeriod = request.form['dvcWarPeriod']

    print(dvcName, dvcType, dvcPurDate, dvcWarPeriod)

    return(redirect(url_for('home'), code=302))


