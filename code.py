import board
import displayio
import terminalio
import time
import random
from adafruit_display_text import label

display = board.DISPLAY
font = terminalio.FONT
color = 0x0000FF

while True:
    text = "HELLO WORLD " + str(random.randint(0,250))
    text_area = label.Label(font, text=text, color=0x00FF00)
    text_area.x = random.randint(0,250)
    text_area.y = random.randint(0,230)
    display.show(text_area)
    time.sleep(1)
