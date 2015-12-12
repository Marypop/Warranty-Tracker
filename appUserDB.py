#!/usr/local/bin/python3


# Copyright (c) 2015 Shreyas Patil
# The MIT License (MIT). Please refer to License.md


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
        userid = self.userid
        pwd = self.hashPwd

        usercollection = db.userdb

        try:
            user = usercollection.find_one({'_id' : userid})
        except errors.PyMongoError as err:
            print('Could not connect to specified database', err)

        if user is None:
            try:
                result = usercollection.insert({'_id' : userid, 'password' : pwd})
            except errors.PyMongoError as err:
                print('Could not connect to specified database', err)
        else:
            return

        return(result)


    def validate_user(self, userid, pwd, db):
        usercollection = db.userdb

        try:
            user = usercollection.find_one({'_id' : userid})
        except errors.PyMongoError as err:
            print('Coud not connect to specified database', err)

        if user is None:
            print('No such user present')
            saved_pwd = ''
        else:
            saved_pwd = user['password']

        if(check_password_hash(saved_pwd, pwd)):
            return(True)
        else:
            return(False)


    def update_user_pwd(self, userid, new_pwd, db):
        userCollection = db.userdb

        updated_pwd = generate_password_hash(new_pwd)

        # Since we have validated password already, which implies user object won't be None
        try:
            result = userCollection.find_one_and_update({'_id' : userid}, {'$set' : {'password' : updated_pwd}})
        except errors.PyMongoError as err:
            print('Coud not connect to specified database', err)

        return(result)
