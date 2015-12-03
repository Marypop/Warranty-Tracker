#!/usr/local/bin/python3

__author__ = 'shreyas'

from flask import render_template, session
from pymongo import MongoClient, errors
from werkzeug.security import generate_password_hash, check_password_hash
from appUserSess import *


class AppUserDB():
    # Initialize the user data with user id and password
    def __init__(self, username, pwd):
        self.userid = username
        self.hashPwd = generate_password_hash(pwd)

    # Methods to check the validate user and password
    def add_new_user(self, db):
        user = self.userid
        pwd = self.hashPwd

        usercollection = db.userdb

        try:
            user = usercollection.find_one({'userid' : user})
        except errors.PyMongoError as err:
            print('Could not connect to specified database', err)

        if user is None:
            try:
                result = usercollection.insert({'userid': user, 'password': pwd})
            except errors.PyMongoError as err:
                print('Could not connect to specified database', err)
        else:
            return

        return(result)


    def validate_user(self, userid, pwd, db): 
        usercollection = db.userdb
        try:
            user = usercollection.find_one({'userid': userid})
        except errors.PyMongoError as err:
            print('Coud not connect to specified database', err)

        if user is None:
            print('No such user present')
        else:
            saved_pwd = user['password']

        if(check_password_hash(saved_pwd, pwd)):
            return(True)
        else:
            return(False)
