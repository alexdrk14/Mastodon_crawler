#!/usr/bin/env python

"""Configuration of MongoDB connector, used for storing the data in DB and filtering already seen users and tweets"""
DBCONFIG={
          "address"   : '127.0.0.1',   #IP address of MongoDB, like '127.0.0.1' in string type"""
          "port"      : 27017, #Port of MongoDB, like 27017 in integer type"""
          "db"        : 'Your_DB_Name', #Name of MongoDB Database, like 'CollectedDatabase' in string type"""
          }

ACCOUNT = {"mail":   'Your_Account_Email',
           "passwd": 'Your_Account_Password',
           "file": 'pytooter_usercred.secret'}
