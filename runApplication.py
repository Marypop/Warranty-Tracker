#!/usr/local/bin/python3


# Copyright (c) 2015 Shreyas Patil
# The MIT License (MIT). Please refer to License.md


__author__ = 'shreyas'

from flask import Flask
from appRoutes import *

class WarrantyApp:
    # Initialize the class instance
    def __init__(self):
        self.app = Flask(__name__)
        self.wsgi_app = self.app.wsgi_app


# Start the App
if __name__ == '__main__':
    app = warApp.app
    app.run(host='localhost', port=5555)
