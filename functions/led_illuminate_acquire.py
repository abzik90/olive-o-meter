import RPi.GPIO as GPIO
from functions.acquire_avg import acquireAndAverage
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

def ledIlluminateAcquire(ledFreq):
    numSamples = 10
    # Rewrite using a dict
    if ledFreq == 525:
        gpioOutput = 22
        gain006 = 16
        gain1450 = 0
    elif ledFreq == 680:
        gpioOutput = 26
        gain006 = 4
        gain1450 = 0
    elif ledFreq == 740:
        gpioOutput = 16
        gain006 = 4
        gain1450 = 0
    elif ledFreq == 980:
        gpioOutput = 23
        gain006 = 2
        gain1450 = 0
    elif ledFreq == 1450:
        gpioOutput = 27
        gain006 = 0
        gain1450 = 8
    else:
        gpioOutput = -1

    GPIO.output(gpioOutput,GPIO.HIGH)
    resultOn = acquireAndAverage(numSamples, gain006, gain1450)

    GPIO.output(gpioOutput,GPIO.LOW)
    resultOff = acquireAndAverage(numSamples, gain006, gain1450)

    return [resultOn, resultOff]
