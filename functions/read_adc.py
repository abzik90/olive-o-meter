from adafruit_ads1x15.analog_in import AnalogIn
import adafruit_ads1x15.ads1015 as ADS
import board
import busio

def readAdc(channel, gain):
    # ADS1015 Address and Registers
    ADS1015_ADDRESS = 0x49  # Changed address to 0x49
    i2c = busio.I2C(board.SCL, board.SDA)

    ads = ADS.ADS1015(i2c, address = ADS1015_ADDRESS)
    ads.gain = gain

    if channel == 0:
        value = AnalogIn(ads, ADS.P0).value
    elif channel == 1:
        value = AnalogIn(ads, ADS.P1).value
    elif channel == 2:
        value = AnalogIn(ads, ADS.P2).value
    elif channel == 3:
        value = AnalogIn(ads, ADS.P3).value
    else:
        value = -1
    return value
