#!/usr/local/bin/python3

__author__ = 'shreyas'


from pymongo import errors


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

        # Try to check if device with same exists already in the db in such cases prevent addition of devices
        try:
            device = deviceCollection.find_one({'_id' : self.deviceName})
        except errors.PyMongoError as deviceNameError:
            print('No such collection exists or database connection issue', deviceNameError)

        if device is None:
            deviceAttr = { '_id' : self.deviceName, 'device_type' : self.deviceType, 
                           'purchase_date' : self.devicePurchaseDate }
            try:
                name = deviceCollection.insert(deviceAttr)
            except errors.CollectionInvalid as collectionErr:
                print('No such collection exists', collectionErr)

        return(name)
