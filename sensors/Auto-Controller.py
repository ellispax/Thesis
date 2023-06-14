import RPi.GPIO as GPIO
import mysql.connector as db
from database.db_connector import getConnect
import time as t
from time import sleep
import datetime as dt

#GPIO.setmode(GPIO.BOARD)
from irrigation_events import compare
from sensors import get_sensor_values

mydb = getConnect()

def get_stamp():
    yy = dt.datetime.today().year
    mm = dt.datetime.today().month
    dd = dt.datetime.today().day
    hh = dt.datetime.today().hour
    m = dt.datetime.today().minute
    ss = dt.datetime.today().second

    Tstamp = (str(yy) + '-' + str(mm) + '-' + str(dd) + " "+ str(hh) + ':' + str(m) + ':' + str(ss))
    date = str(yy) + '-' + str(mm) + '-' + str(dd)
    time = str(hh) + ':' + str(m) + ':' + str(ss)
    return Tstamp, time, date

def check_status():
    mydb = getConnect()
    try:
        query = "SELECT status FROM home_farm WHERE id = '6'"
        cursor = mydb.cursor()
        cursor.execute(query)
        data = cursor.fetchall()
        data = list(data)
        out = data[0][0]
        
        if out == 0:
            #print(out)
            return False
        else:       
            #print(out)     
            return True            
           
    except db.Error as error:
        print("Failed to get record from table{}".format(error))


def insert_values(temp,pH,humidity,moisture,desc):
    stamp, time, date = get_stamp()
    try:
        
        query ="INSERT INTO analytics_measurements (date, time, temp,pH, humidity, moisture, farm_id, timeStamp,description) VALUES ('"+ date +"', '"+time+"', '"+str(temp)+"', '"+str(pH)+"', '"+str(humidity)+"', '"+str(moisture)+"','6', '"+stamp+"', '"+desc+"')"
        cursor=mydb.cursor()#cursor.execute(add_word.format(table=atable).data_word)
        cursor.execute(query)
        mydb.commit()
        print(cursor.rowcount, "Record inserted successfull")
        cursor.close()
    except db.Error as error:
        print("Failed to insert record into table{}".format(error))

while True:
    green_pin = 12

    GPIO.setup(green_pin, GPIO.OUT)

    GPIO.output(green_pin, GPIO.HIGH)

    # Get the current time
    now = dt.datetime.now()

    # Check if the current time is on the hour
    if now.minute == 0 and now.second == 0:
       
        temp, hum, pH, moisture = get_sensor_values()
        if check_status() == True:
            desc = "Irrigation analyzer Online"
        else:
            desc = "Irrigation analyzer Offline"

        print ("Sensor Values: ","\nTemp: ",temp,"\nHumidity: ", hum,"\npH: ", pH, "\nMoisture: ",moisture)


        insert_values(temp, pH,hum, moisture, desc)
        fStatus = check_status()
        if fStatus == True:
            print("Irrigation Comparison Started ... \n")
            compare(temp, moisture,pH,hum)
        else:
            print("Irrigation Status Turned Off")
    else:
        # Calculate the number of seconds until the next hour
        next_hour = (now + dt.timedelta(hours=1)).replace(minute=0, second=0, microsecond=0)
        time_to_wait = (next_hour - now).total_seconds()

        # Wait until the next hour
        print(f"Waiting {time_to_wait} seconds until the next hour...")
        t.sleep(time_to_wait)


    
    
   
