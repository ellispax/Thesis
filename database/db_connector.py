#import mysql.connector as db
import pymysql as db
import time as t
import datetime as dt


# def getConnect():

#     mydb = db.connect(
#         host = "sql12.freesqldatabase.com",
#         user= "sql12592016",
#         password="ngsdriE1iD",
#         database="sql12592016")
#     return mydb


def getConnect():

    mydb = db.connect(
        host = "irrigation.cwikznmtsvgr.us-east-1.rds.amazonaws.com",
        user= "admin",
        password="ATEyspy2QIG)",
        database="irrigationdb")
    return mydb

DB = getConnect()
print(DB)