import os
from functions.led_acquire import ledAcquireAll
from functions.epd_draw_pic import epdDrawImage


key1, key2, key3, key4 = 5,6,13,19

def interrupt(channel):
    print("interrupt", channel)
    
    if channel == key1:
        print("TOP\n")
        ledAcquireAll(epd, 1)
    elif channel == key2:
        print("MIDDLE\n")
        ledAcquireAll(epd, 2)
    elif channel == key3:
        print("BOTTOM\n")
        ledAcquireAll(epd, 3)
    elif channel == key4:
        print("SHUTDOWN\n")
        epdDrawImage('shutdown_screen.bmp')
        os.system("sudo shutdown -h now")
    else:
        print("ERROR: Unknown key interrupt")
    