import RPi.GPIO as GPIO
from time import sleep
import mysql.connector as db
from database.db_connector import getConnect
from pump import run_pump
import datetime

mydb = getConnect()
    
def send_notification(notification):
    now = datetime.datetime.now()

    time = now.strftime("%H:%M:%S")
    date = now.strftime("%Y-%m-%d")
    try:
        
        query ="INSERT INTO home_notifications (notification, date, time,farm_id) VALUES ('"+ notification +"', '"+date+"', '"+time+"', '1')"
        cursor=mydb.cursor()#cursor.execute(add_word.format(table=atable).data_word)
        cursor.execute(query)
        mydb.commit()
        print(cursor.rowcount, "Notification send successfull")
        cursor.close()
    except db.Error as error:
        print("Failed to insert record into table{}".format(error))

def get_presets():
    statement = "SELECT temp, humidity, moisture, ph_min, ph_max FROM manager_manage WHERE farm_id = '1'"
    try:
        cursor = mydb.cursor()
        cursor.execute(statement)
        data = cursor.fetchall()
        data = list(data)
        
        #print(data)
        #print(type(data))
        cursor.close()
        return data #return the parking record ID

    except db.Error as error:
        print("Failed to get record from table{}".format(error))

thresholds = get_presets()
temp_threshold = thresholds[0][0]
humidity_threshold = thresholds[0][1]
moisture_threshold= thresholds[0][2]
pHMin_threshold = thresholds[0][3] 
pHMax_threshold = thresholds[0][4] 
#print (humidity_threshold,moisture_threshold,pH_threshold)




def compare(temp,moisture, pH, humidity):
    notification_Low = "pH is lower than required. Consider Seeking Advice."
    notification_high = "pH is higer than required. Consider Seeking Advice."
    if pH < pHMin_threshold:
        send_notification(notification_Low)
    elif pH > pHMax_threshold:
        send_notification(notification_high)
    else:
        pass
    
    # Check if moisture level is below threshold
    if moisture < moisture_threshold:
        print("Moisture level lower than required!\n")
        sleep(2)
        print("Starting Irrigation Procedure . . .")
        run_pump(moisture_threshold)
        
        
    # Check if pH level is outside of acceptable range
    elif pH < pHMin_threshold or pH > pHMax_threshold and moisture <= moisture_threshold + 5:
        
        print("pH level is outside of acceptable range & Soil moisture is within irrigation accepted range!\n")
        sleep(2)
        print("Starting Irrigation Procedure . . .")
        run_pump(moisture_threshold)

    elif temp > temp_threshold and moisture <= moisture_threshold + 5:
        print("Temperature Higher than expected & Soil moisture is within irrigation accepted range.!\n")
        sleep(2)
        print("Starting Irrigation Procedure . . .")
        run_pump(moisture_threshold)   
        
    # Check if humidity level is below threshold
    # elif humidity < humidity_threshold and moisture < moisture_threshold + 3:
    #     print("Air Humidity lower than expected & Soil moisture is within irrigation accepted range!\n")
    #     sleep(2)
    #     print("Starting Irrigation Procedure . . .")
    #     run_pump()
        
        
    else:
        print("Everything seems normal no irrigation is required at the moment.")



