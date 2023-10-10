from PIL import Image,ImageDraw,ImageFont
from config.config import OLIVOMETER_RES
from models.olive_readings import OliveReadingsManager
from lib.epd import EPD

import os

# Font initialization
font18 = ImageFont.truetype(os.path.join(OLIVOMETER_RES, 'DINCondensed-Bold.ttf'), 18)
font35 = ImageFont.truetype(os.path.join(OLIVOMETER_RES, 'DINCondensed-Bold.ttf'), 35)

epd = EPD()
epd.fast_refresh = True

def epdDrawImage(path):
    epd.init()
    Himage = Image.open(os.path.join(OLIVOMETER_RES, path))
    epd.display_frame_full(Himage)
    epd.sleep()
def epdDrawLogo(path):
    epd.init()
    Limage = Image.new('1', (epd.width, epd.height), 255)  # 255: clear the frame
    bmp = Image.open(os.path.join(OLIVOMETER_RES, path))
    Limage.paste(bmp, (0,0))

def epdDrawTable(pd_avg, tree_pos_text, sampling_time_utc):
    entryID = OliveReadingsManager.getLastReadingId()
    epdDrawImage('olivometer_logo_black.bmp')
    
    draw = ImageDraw.Draw(Limage)
    draw.line((5, 60, 40, 60), fill = 0)
    draw.line((45, 60, 100, 60), fill = 0)
    draw.line((105, 60, 160, 60), fill = 0)

    draw.text((5, 40), 'f nm', font = font18, fill = 0)
    draw.text((5, 65), '525', font = font18, fill = 0)
    draw.text((5, 85), '680', font = font18, fill = 0)
    draw.text((5, 105), '740', font = font18, fill = 0)
    draw.text((5, 125), '980', font = font18, fill = 0)
    draw.text((5, 145), '1450', font = font18, fill = 0)

    draw.text((50, 40), 'ACCESO', font = font18, fill = 0)   #ON
    draw.text((50, 65), f"{pd_avg[0][0]}", font = font18, fill = 0)
    draw.text((50, 85), f"{pd_avg[1][0]}", font = font18, fill = 0)
    draw.text((50, 105), f"{pd_avg[2][0]}", font = font18, fill = 0)
    draw.text((50, 125), f"{pd_avg[3][0]}", font = font18, fill = 0)
    draw.text((50, 145), f"{pd_avg[4][0]}", font = font18, fill = 0)

    draw.text((110, 40), 'SPENTO', font = font18, fill = 0)     #OFF
    draw.text((110, 65), f"{pd_avg[0][1]}", font = font18, fill = 0)
    draw.text((110, 85), f"{pd_avg[1][1]}", font = font18, fill = 0)
    draw.text((110, 105), f"{pd_avg[2][1]}", font = font18, fill = 0)
    draw.text((110, 125), f"{pd_avg[3][1]}", font = font18, fill = 0)
    draw.text((110, 145), f"{pd_avg[4][1]}", font = font18, fill = 0)

    draw.line((0, 170, 176, 170), fill = 0)
    draw.text((5, 175), f'Nr. di lettura ({tree_pos_text})', font = font18, fill = 0)
    draw.text((5, 195), f'{entryID}', font = font35, fill = 0)

    draw.line((0, 235, 176, 235), fill = 0)
    draw.text((5, 240), f"{sampling_time_utc} UTC", font = font18, fill = 0)

    epd.display_frame(Limage)
    epd.sleep()

    Limage = Image.new('1', (epd.width, epd.height), 255)  # 255: clear the frame
    draw = ImageDraw.Draw(Limage)
    
    
    # os.path.join(olivometer_lib, 'olivometer_logo_black.bmp')
    
