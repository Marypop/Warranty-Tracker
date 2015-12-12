# !/usr/local/bin/python3


# Copyright (c) 2015 Shreyas Patil
# The MIT License (MIT). Please refer to License.md


__author__ ='shreyas'


from flask_table import Table, Col, ButtonCol, DateCol


class UserDeviceTable(Table):
    # Declare the table columns
    # serial_no     = Col('serial_no')
    classes = ['table', 'table-striped']
    device_name   = Col('Device Name')
    device_type   = Col('Device Type')
    purchase_date = Col('Purchase Date')
    warranty_date = Col('Warranty Date')
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

    user_device_table = UserDeviceTable(user_device)
    return(user_device_table)
