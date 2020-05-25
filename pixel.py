import time
import mss
from PIL import ImageGrab, Image
import board
import neopixel_spi as neopixel
import win32gui

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

def get_pixel_colour(i_x, i_y):
	long_colour = win32gui.GetPixel(i_desktop_window_dc, i_x, i_y)
	i_colour = int(long_colour)
	return (i_colour & 0xff), ((i_colour >> 8) & 0xff), ((i_colour >> 16) & 0xff)


def CalcAverageRgbOfArea( dx):
    #im = Image.frombytes("RGB", image.size, image.bgra, "raw", "BGRX")

    totals = [0,0,0]
    for x in range(dx, dx + areaWidth, colScale):
        for y in range(areaHeight + areaHeight, areaHeight + areaHeight + areaHeight, rowScale):            
            rgb = get_pixel_colour(x,y)
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

sct = mss.mss()

monitor = { "top": areaHeight * 2, "left": 0, "width": width, "height": areaHeight }

i_desktop_window_id = win32gui.GetDesktopWindow()
i_desktop_window_dc = win32gui.GetWindowDC(i_desktop_window_id)

while True:
    #image = ImageGrab.grab()    
    #image = sct.grab(monitor)

    for i in range(0,NUM_PIXELS):
        rgb = CalcAverageRgbOfArea(int(i * areaWidth))
        color = getIfromRGB(rgb)         
        print(color)
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