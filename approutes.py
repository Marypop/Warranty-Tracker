#!/usr/local/bin/python3


# This file should contain all the routes that will be called in the warranty tracker web-application
from application import WarrantyApp
from flask import render_template, request


# Default home screen route
warApp = WarrantyApp()
app = warApp.app

print('Trying routes now')

@app.route('/')
def indexScreen():
    return(render_template('index.html'))
