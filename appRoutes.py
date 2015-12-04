#!/usr/local/bin/python3

__author__ = 'shreyas'

# This file should contain all the routes that will be called in the warranty tracker web-application

import os, dateutil.parser

from datetime import datetime
from runApplication import WarrantyApp
from flask import render_template, request, url_for, redirect, Response, session
from appUserDB import *
from appUserSess import *
from appUserDevciceDB import *


# Application object initialization
warApp = WarrantyApp()
app = warApp.app

# Establish a connection with the database, Later we might add this code __init__ with Try...Except for connection
conn = MongoClient(host='localhost',port=27017)
db = conn.test
session = AppUserSession(db)

# Default home screen route
# This will be the home screen of the app
@app.route('/')
@app.route('/index')
def index():
    return(render_template('index.html'))


# This route will get executed while user opens up the homepage for the application
@app.route('/home')
def home():
    session_id = request.cookies['session']
    user = session.getSessionUserInfo(session_id)

    if user is None:
        template = 'index.html'
    else:
        # Now if there is a user before rendering the template we would like to populate the table
        table = populate_user_device_table(user, db)
        template = 'user_screen.html'

        in_warranty_table = table[0]
        out_warranty_table = table[1]

    return(render_template(template, in_warranty_table=in_warranty_table,\
                                     out_warranty_table=out_warranty_table))


# Routes to Log-in existing, Register new user and logging out of the application
@app.route('/login', methods=['POST'])
def userAppLogin():
    # We should not ideally check for the method, since only allowed method is 'POST'.But still to be
    # safe and to maintain sanity in flask coding convention, we will do it :)
    if(request.method == 'POST'):
        userid = request.form['email']
        pwd = request.form['passwd']
        appuser = AppUserDB(userid, pwd)

    can_login = appuser.validate_user(userid, pwd, db)

    if can_login:
        redirect_url = 'home'
        session_id = session.startUserSession(userid)
    else:
        redirect_url = 'index'
        session_id = ''

    response = redirect(url_for(redirect_url), code=302)
    response.set_cookie('session', session_id)

    return(response)


@app.route('/register', methods=['POST'])
def addNewAppUser():
    if(request.method == 'POST'):
        userid = request.form['email']
        pwd = request.form['passwd']
        conf_pwd = request.form['cnfpasswd']

    if(pwd == conf_pwd):
        appusr = AppUserDB(userid, pwd)
        print(appusr.userid)
    else:
        return(redirect(url_for('index'), code=302))

    created_usr = appusr.add_new_user(db)

    if created_usr is None:
        redirect_url = 'index'
        session_id = ''
    else:
        redirect_url = 'home'
        session_id = session.startUserSession(userid)

    response = redirect(url_for(redirect_url), code=302)
    response.set_cookie('session', value=session_id)

    return(response)


@app.route('/logout', methods=['POST'])
def usrLogout():
    session_id = request.cookies['session']
    session.removeUserSession(session_id)

    response = redirect('index', code=302)
    response.set_cookie('session', '')

    return(response)


# Routes to Add/Delete new devices for a given user
@app.route('/addnewdevice', methods=['POST'])
def addNewDevice():
    if(request.method == 'POST'):
        dvcName = request.form['dvcName']
        dvcType = request.form['dvcType']
        dvcPurDate = request.form['dvcPurDate']
        dvcWarPeriod = request.form['dvcWarPeriod']

    # Convert date time string to ISODate.
    dvcPurDate = dateutil.parser.parse(dvcPurDate)

    session_id = request.cookies['session']
    userid = session.getSessionUserInfo(session_id)

    appuserdevice = AppUserDeviceDB(userid, dvcName, dvcType, dvcPurDate, dvcWarPeriod)

    appuserdevice.addNewUserDevice(db)

    return(redirect(url_for('home'), code=302))


