import time
import board
import adafruit_dht
import psutil
import RPi.GPIO as GPIO


def get_tem_humidty():
    for proc in psutil.process_iter():
        if proc.name() == 'libgpio_pusein' or proc.name() == 'libgpiod_pulsei':
            proc.kill()

    sensor_temp = adafruit_dht.DHT11(board.D23)
    # sensor_humid = adafruit_dht.DHT11(board.D12)

    
    try:
        temp = sensor_temp.temperature
        humidity = sensor_temp.humidity
        print("Temperature: {}*C Humidity {}%".format(temp, humidity))
    except RuntimeError as error:
        print(error.args[0])
        time.sleep(2)
    
    except Exception as error:
        # sensor_humid.exit()
        sensor_temp.exit()
        raise error
    #time.sleep(2)

    return temp, humidity

    
def get_values():
    temp, hum = get_tem_humidty()
    pH = 7
    moisture = 25

    return temp, hum, pH, moisture



