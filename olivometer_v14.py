import time
import logging
from lib.epd import EPD
import RPi.GPIO as GPIO
from functions.interrupt_callbacks import interrupt
from functions.epd_draw_pic import epd_draw_image

epd = EPD()
epd.fast_refresh = True

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# eInk display setup key inputs
keys_in = [5,6,13,19]
keys_out = [16,22,23,26,27]

for key in keys_in:
    GPIO.setup(key, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.add_event_detect(key, GPIO.FALLING, callback=interrupt, bouncetime=200)

# LED pin setup (outputs)
for key in keys_out:
    GPIO.setup(key,GPIO.OUT)
    GPIO.output(key,GPIO.LOW)
print("ALL OFF\n")

logging.basicConfig(level=logging.DEBUG)


def main():
    epd_draw_image(epd, 'ready_screen.bmp')

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print(" detected. ALL OFF and QUIT.")
        for key in keys_out:
            GPIO.output(key,GPIO.LOW)
        GPIO.cleanup()

if __name__ == "__main__":
    main()