from functions.led_illuminate_acquire import ledIlluminateAcquire
from functions.epd_draw_pic import epdDrawTable
from time import gmtime, strftime
from models.olive_readings import OliveReadingsManager

def ledAcquireAll(tree_pos):
    led_freqs = [525, 680, 740, 980, 1450]

    positions = {1:"ALTO", 2:"CENTRO", 3:"BASSO"}
    tree_pos_text = positions[tree_pos] if tree_pos > 0 and tree_pos < 4 else "UNKNOWN"
    pd_avg = [ledIlluminateAcquire(led_freq) for led_freq in led_freqs]
    sampling_time_utc = strftime("%Y-%m-%d %H:%M:%S", gmtime())
    print("LedAcquireAll:", pd_avg)    
  
    manager = OliveReadingsManager()
    manager.createReading(sample_time=sampling_time_utc, nm_525_ON=pd_avg[0][0], nm_525_OFF=pd_avg[0][1],
                            nm_680_ON=pd_avg[1][0], nm_680_OFF=pd_avg[1][1], nm_740_ON=pd_avg[2][0], nm_740_OFF=pd_avg[2][1],
                            nm_980_ON=pd_avg[3][0], nm_980_OFF=pd_avg[3][1], nm_1450_ON=pd_avg[4][0], nm_1450_OFF=pd_avg[4][1])    
    epdDrawTable(pd_avg, tree_pos_text, sampling_time_utc)  
  # return pdav
