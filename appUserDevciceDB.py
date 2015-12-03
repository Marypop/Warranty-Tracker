#!/usr/local/bin/python3

__author__ = 'shreyas'


from pymongo import errors
from datetime import datetime, timedelta


class AppUserDeviceDB():

    def __init__(self, userid, deviceName, deviceType, devicePurchaseDate, warrantyPeriod):
        self.userid = userid
        self.deviceName = deviceName
        self.deviceType = deviceType
        self.devicePurchaseDate = devicePurchaseDate
        self.warrantyPeriod = warrantyPeriod


    # Method to add new device to db
    def addNewUserDevice(self, db):

        deviceCollection = db.deviceCollection
        find_query = {'_id': self.userid}

        warrantyDate = calculate_warranty_date(self.devicePurchaseDate, self.warrantyPeriod)

        device = [{ 'device_name'   : self.deviceName,
                    'device_type'   : self.deviceType, 
                    'purchase_date' : self.devicePurchaseDate,
                    'warranty_date' : warrantyDate}]


        try:
            userDevices = deviceCollection.find_one(find_query)
        except errors.PyMongoError as deviceNameError:
            print('No such collection exists or database connection issue', deviceNameError)

        if userDevices is None:
            deviceAttr = { '_id' : self.userid, 'devices' : device }
            try:
                name = deviceCollection.insert(deviceAttr)
            except errors.CollectionInvalid as collectionErr:
                print('No such collection exists', collectionErr)
        else:
            update_query = {'$addToSet' : {'devices': device}}
            try:
                name = deviceCollection.find_one_and_update(find_query, update_query)
            except errors.PyMongoError as Err:
                print('Device was not inserted', Err)

        return(name)



def calculate_warranty_date(purchaseDate, warrantyPeriod):
    # Convert the warranty period from months to weeks
    convertedWeeks = (int(warrantyPeriod)/12) * 52
    warrantyDate = purchaseDate + timedelta(weeks=convertedWeeks)

    return(warrantyDate)