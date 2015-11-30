#!/usr/local/bin/python3


# This file should contain all the routes that will be called in the warranty tracker web-application
from application import WarrantyApp
from flask import render_template, request


# Default home screen route
warApp = WarrantyApp()
app = warApp.app


# This will be the home screen of the app
@app.route('/')
def indexScreen():
    return(render_template('index.html'))


# This route will get executed while user is logged in the app
@app.route('/home/<user_name>')
def displayUserScreen(user_name):
    return(render_template('user_screen.html', user_name=user_name))
