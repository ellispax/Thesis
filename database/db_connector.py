#import mysql.connector as db
import pymysql as db
import time as t
import datetime as dt


def getConnect():

    mydb = db.connect(
        host = "",
        user= "root",
        password="",
        database="",
        port = 3306
    )
    return mydb
