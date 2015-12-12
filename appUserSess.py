#!/usr/local/bin/python3


# Copyright (c) 2015 Shreyas Patil
# The MIT License (MIT). Please refer to License.md


__author__ = 'shreyas'

import os
from pymongo import collection, errors


class AppUserSession:

    def __init__(self, db):
        # Connect to database and create a session collection to manage the user sessions
        self.db = db
        self.session = db.session

    # Will be called during user login route to keep track of user sessions
    def startUserSession(self, userid):
        user = userid.split('@')
        chars = len(user[0])
        secret_key = os.urandom(chars)
        session = {'_id' : str(secret_key), 'user_id' : userid}

        try:
            result = self.session.insert(session)
        except errors.CollectionInvalid as collectionErr:
            print('Invalid collection name', collectionErr)
            return None

        return(result)


    # We need to remove the session from the db, when user logs out of the application
    def removeUserSession(self, session_id):
        if session_id is None:
            return

        self.session.remove({'_id' : session_id})


    # Helper function to get session information
    def getSessionInfo(self, session_id):
        if session_id is None:
            return('Invalid session ID')

        session = self.session.find_one({'_id' : session_id})

        if session is None:
            return('Invalid session ID')
        else:
            return(session)

    # Helper function to get information about the user in the session
    def getSessionUserInfo(self, session_id):
        if session_id is None:
            return

        session = self.session.find_one({'_id' : session_id})

        if session is None:
            return None
        else:
            return(session['user_id'])
