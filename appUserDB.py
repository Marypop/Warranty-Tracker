#!/usr/local/bin/python3

from flask import render_template, session
from pymongo import MongoClient, errors
from werkzeug.security import generate_password_hash, check_password_hash


# Establish a connection with the database, Later we might add this code __init__ with Try...Except for connection
conn = MongoClient(host='localhost',port=27017)
db = conn.test

class AppUserDB():
    # Initialize the user data with user id and password
    def __init__(self, username, pwd):
        self.userid = username
        self.hashPwd = generate_password_hash(pwd)

    # Methods to check the validate user and password
    def add_new_user(self):
        user = self.userid
        pwd = self.hashPwd

        collection = db.userdb

        try:
            doc = collection.find_one({'userid' : user})
        except errors.PyMongoError as err:
            print('Could not connect to specified database', err)

        print(doc)

        if doc is None:
            try:
                result = collection.insert({'userid': user, 'password': pwd})
            except errors.PyMongoError as err:
                print('Could not connect to specified database', err)
        else:
            return

        return(result)


    def validate_user(self, userid, pwd): 
        collection = db.userdb
        try:
            doc = collection.find_one({'userid': userid})
        except errors.PyMongoError as err:
            print('Coud not connect to specified database', err)

        if doc is None:
            print('No such user present')
        else:
            saved_pwd = doc['password']

        if(check_password_hash(saved_pwd, pwd)):
            return(True)
        else:
            return(False)
