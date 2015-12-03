#!/usr/local/bin/python3

__author__ = 'shreyas'

from flask import Flask
from approutes import *

class WarrantyApp:
    # Initialize the class instance
    def __init__(self):
        self.app = Flask(__name__)
        self.wsgi_app = self.app.wsgi_app


# Start the App
if __name__ == '__main__':
    app = warApp.app
    app.run(host='localhost', port=5555, debug=True)
