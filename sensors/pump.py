import RPi.GPIO as GPIO
from time import sleep
from gpiozero import LED
from capacitive_moisture import check_moisture
import time

from database.db_connector import getConnect
import mysql.connector as db
import datetime

mydb = getConnect()
def insert(water):
    

    now = datetime.datetime.now()

    time = now.strftime("%H:%M:%S")
    date = now.strftime("%Y-%m-%d")
    
    try:
        
        query ="INSERT INTO analytics_water_used (water_amnt, date, time,farm_id) VALUES ('"+ str(water) +"', '"+date+"', '"+time+"', '1')"
        cursor=mydb.cursor()#cursor.execute(add_word.format(table=atable).data_word)
        cursor.execute(query)
        mydb.commit()
        print(cursor.rowcount, "Water used record inserted successfull")
        cursor.close()
    except db.Error as error:
        print("Failed to insert record into table{}".format(error))

def run_pump(moisture_threshold):
    GPIO.setmode(GPIO.BCM)
    # Define the pin number for the yellow LED
    yellow_pin = 18   

    pump_pin = 4
    led_pin = 27

    GPIO.setup(pump_pin, GPIO.OUT)
    GPIO.setup(led_pin, GPIO.OUT)
    GPIO.setup(yellow_pin, GPIO.OUT)
    p = GPIO.PWM(pump_pin, 100)
    q = GPIO.PWM(led_pin, 100)
    moisture = check_moisture()

    start_time = time.time()
    while moisture <= moisture_threshold + 10:
        GPIO.output(yellow_pin, GPIO.HIGH)    
        p.start(0)
        p.ChangeDutyCycle(100)  # set maximum duty cycle for full power
        print('\nWater Pump On - Irrigating until moisture level increases')
        moisture = check_moisture()
        sleep(3)
        

    p.stop()
    # q.start(0)  
    GPIO.output(yellow_pin, GPIO.LOW)    
    print("Water Pump turning Off")     
    q.stop()  
    GPIO.cleanup()  # clean up GPIO resources
    run_time = time.time() - start_time
    print("The pump ran for {} seconds.".format(round (run_time,2)))
    water = run_time*4
    print("{} ml of water was used to irrigate crop.".format(round(water,2)))
    insert(round(water,2))

    

# run_pump(77)
