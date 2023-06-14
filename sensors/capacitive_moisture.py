import time
import board
import busio
import adafruit_ads1x15.ads1015 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

# print("------{:>5}\t{:>5}".format("raw", "moisture"))

def check_moisture():
    # Calibration constants
    # slope = -39.68
    slope = -73.20

    # y_intercept = 138.89
    y_intercept = 171.74

    # Create the I2C bus
    i2c = busio.I2C(board.SCL, board.SDA)

    # Create the ADC object using the I2C bus
    ads = ADS.ADS1015(i2c)

    # Create single-ended input on channel 2
    chan = AnalogIn(ads, ADS.P1)
    voltage = chan.voltage
    moisture = slope * voltage + y_intercept
    moisture = max(0, min(100, moisture))
    
    print("CHAN 2: "+"{:>5}\t{:>5.1f}".format(chan.value, round(moisture,2)))
    return round(moisture,2)
