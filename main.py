import time
import board
import digitalio
from PIL import ImageGrab


print(dir(board))

redLed = digitalio.DigitalInOut(board.C0)
redLed.direction = digitalio.Direction.OUTPUT

greenLed = digitalio.DigitalInOut(board.C1)
greenLed.direction = digitalio.Direction.OUTPUT
 
blueLed = digitalio.DigitalInOut(board.C2)
blueLed.direction = digitalio.Direction.OUTPUT


def TurnOnRed():
    redLed.value = True
    greenLed.value = False
    blueLed.value = False
   
def TurnOnGreen():
    redLed.value = False
    greenLed.value = True
    blueLed.value = False

def TurnOnBlue():
    redLed.value = False
    greenLed.value = False
    blueLed.value = True

def CalcAverageRgb():
  
    image = ImageGrab.grab()
    totals = [0,0,0]
    width = image.size[0]
    height = image.size[1]
    scale = 32

    for x in range(0, width, 32):
        for y in range(0, height, 32):

            rgb = image.getpixel((x,y))
            totals[0] += rgb[0]
            totals[1] += rgb[1]
            totals[2] += rgb[2]
    
    w = width / scale
    h = height / scale

    avgR = totals[0] / (w*h)
    avgG = totals[1] / (w*h)
    avgB = totals[2] / (w*h)
    
    return [avgR, avgG, avgB]

while True:
    avgRgb = CalcAverageRgb()
    maxValue = max(avgRgb)
    maxIndex = avgRgb.index(maxValue)
    print(maxIndex)

    if maxIndex == 0:
        TurnOnRed()
    elif maxIndex == 1:
        TurnOnGreen()
    else:
        TurnOnBlue()
    time.sleep(0.5)

    # TurnOnRed()
    # time.sleep(0.5)
    # TurnOnGreen()
    # time.sleep(0.5)
    # TurnOnBlue()
    # time.sleep(0.5)