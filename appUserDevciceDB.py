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
    def addNewUserDevice(self, db, userid):
        deviceCollection = db.deviceCollection

        warrantyDate = calculate_warranty_date(self.devicePurchaseDate, self.warrantyPeriod)

        try:
            device = deviceCollection.find_one({'_id' : self.deviceName, 'userid' : userid})
        except errors.PyMongoError as deviceNameError:
            print('No such collection exists or database connection issue', deviceNameError)

        if device is None:
            devices = [{'device_name'   : self.deviceName,
                        'device_type'   : self.deviceType, 
                        'purchase_date' : self.devicePurchaseDate,
                        'warranty_date' : warrantyDate}]

            deviceAttr = { '_id' : userid, 'device' : devices }
                           
            try:
                name = deviceCollection.insert(deviceAttr)
            except errors.CollectionInvalid as collectionErr:
                print('No such collection exists', collectionErr)

        return(name)



def calculate_warranty_date(purchaseDate, warrantyPeriod):
    # Convert the warranty period from months to weeks
    convertedWeeks = (int(warrantyPeriod)/12) * 52
    warrantyDate = purchaseDate + timedelta(weeks=convertedWeeks)

    return(warrantyDate)