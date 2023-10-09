import numpy as np
from functions.read_adc import readAdc

def acquireAndAverage(numSamples, gain006, gain1450):
    pdSamples = []

    if gain006 > 0 and gain1450 == 0:
        channelRange = [0,1]
        gain = gain006
    elif gain006 == 0 and gain1450 > 0:
        channelRange = [2,3]
        gain = gain1450
    else:
        channelRange = []
        gain = 0

    for _ in range(numSamples):
        pdSamples.extend([readAdc(channel, gain) for channel in channelRange])
           
    #print(" ".join(debug_output))

    pdData = int(abs(round(np.mean(pdSamples),0)))

    return pdData
