import time
from PIL import ImageGrab
import board
import neopixel_spi as neopixel


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
    
    return [int(avgR), int(avgG), int(avgB)]

def CalcAverageRgbOfArea(image, dx):
    totals = [0,0,0]
    for x in range(dx, dx + areaWidth, colScale):
        for y in range(areaHeight + areaHeight, areaHeight + areaHeight + areaHeight, rowScale):            
            rgb = image.getpixel((x,y))
            totals[0] += rgb[0]
            totals[1] += rgb[1]
            totals[2] += rgb[2]
    
    #print(totals)

    w = areaWidth / (colScale)
    h = height / (rowScale)
    avgR = totals[0] / (w*h)
    avgG = totals[1] / (w*h)
    avgB = totals[2] / (w*h)
    
    return [int(avgR), int(avgG), int(avgB)]

def getIfromRGB(rgb):
    red = rgb[0]
    green = rgb[1]
    blue = rgb[2]
    RGBint = (red<<16) + (green<<8) + blue
    return RGBint



NUM_PIXELS = 60
PIXEL_ORDER = neopixel.GRB
DELAY = 0.01

width = 3840
height = 2160
areaWidth = width//60
areaHeight  = height // 3
colScale = areaWidth // 25
rowScale = height // 50

spi = board.SPI()
 
pixels = neopixel.NeoPixel_SPI(spi,
                               NUM_PIXELS,
                               pixel_order=PIXEL_ORDER,
                               auto_write=False)

while True:
    image = ImageGrab.grab()    


    for i in range(0,NUM_PIXELS):
        rgb = CalcAverageRgbOfArea(image,  int(i * areaWidth))
        color = getIfromRGB(rgb)         
        #print(str(hex(color)) + ' - ' + str(color) + ' - ', rgb)
        pixels[NUM_PIXELS- i - 1] = color
        
    pixels.show()
    
    #color = getIfromRGB(CalcAverageRgb())
    #print(str(hex(color)))
    #pixels.fill(color)
    #time.sleep(DELAY)





    # for color in COLORS:
    #     for i in range(NUM_PIXELS):
    #         print (color)
    #         pixels[i] = color
    #         pixels.show()
    #         
    #         pixels.fill(0)