# !/usr/local/bin/python3

__author__ ='shreyas'


from flask_table import Table, Col, ButtonCol, DateCol


class UserDeviceTable(Table):
    # Declare the table columns
    # serial_no     = Col('serial_no')
    device_name   = Col('device_name')
    device_type   = Col('device_type')
    purchase_date = Col('purchase_date')
    warranty_date = Col('warranty_date')
    # delete_btn    = ButtonCol('delete_btn')


class UserDevice(object):
    def __init__(self, devices):
        self.devices = devices
        self.counter = 0 # Initialize the counter

    def __iter__(self):
        return(self)

    def __next__(self):
        max_count = len(self.devices)
        if(self.counter < max_count):
            self.counter+=1
            return(self.devices[self.counter - 1])
        else:
            raise StopIteration


def create_user_device_objects(devices):
    

    user_device = UserDevice(devices)

    print(user_device)

    user_device_table = UserDeviceTable(user_device)
    return(user_device_table)

