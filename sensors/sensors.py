import time
import adafruit_dht
import psutil
import RPi.GPIO as GPIO
from board import D23
import board
import busio
import time
import sys
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
import adafruit_ads1x15.ads1015 as ADS


# Soil Moisture Calibration constants
slope = -73.20
y_intercept = 171.74

# Create the I2C bus
i2c = busio.I2C(board.SCL, board.SDA)

# Create the ADC object using the I2C bus
ads = ADS.ADS1015(i2c)

chan = AnalogIn(ads, ADS.P1)
def get_soil_moisture():
    voltage = chan.voltage
    moisture = slope * voltage + y_intercept
    moisture = max(0, min(100, moisture))  # Constrain moisture to between 45% and 100%
    
    return round(moisture,2)

def run_pump():
    p = GPIO.PWM(7, 50)
    q = GPIO.PWM(11, 50)
    p.start(0)
    q.start(0)
    p.ChangeDutyCycle(100)  # set maximum duty cycle for full power
    print('water running')
    time.sleep(5)  # run for 30 seconds
    q.ChangeDutyCycle(100)
    print("clean pipe")
    time.sleep(3)
    p.stop()
    q.stop()  # stop PWM output
    GPIO.cleanup()  # clean up GPIO resources


#Temperature & Humidity setup
dht_device = adafruit_dht.DHT11(D23)


def get_temperature_humidity():
    try:
        temperature_c = dht_device.temperature
        humidity = dht_device.humidity

        # print("Temperature: ", temperature_c)
        # print("Humidity: ", humidity)

        return temperature_c, humidity

    except RuntimeError as error:
        # handle runtime errors that may occur when reading from the sensor
        print("Error: ", error)
        return None, None

    except Exception as error:
        # handle any other exceptions that may occur
        print("Error: ", error)
        return None, None

#Reading voltage for pH sensor
def read_voltage(channel):
    while True:
        buf = list()
        
        for i in range(10): # Take 10 samples
            buf.append(channel.voltage)
        buf.sort() # Sort samples and discard highest and lowest
        buf = buf[2:-2]
        avg = (sum(map(float,buf))/6) # Get average value from remaining 6

        volt = round(avg,2)
        ph = (-6.0638* volt)+ 22.262
        #print('Voltage = ',volt,'V & pH = ',ph )
        return round(ph,2)


def get_pH():
    channel = AnalogIn(ads, ADS.P0)

    ph = read_voltage(channel)
    return ph

#Collecting all Sensor values
def get_sensor_values():
    temp, hum = get_temperature_humidity()
    moisture = get_soil_moisture()
    pH = get_pH()
    
    while temp is None or hum is None:
        print("Error obtaining values from humidity and temperature sensor")
        time.sleep(3)
        temp, hum = get_temperature_humidity()

    return temp, hum, pH, moisture
