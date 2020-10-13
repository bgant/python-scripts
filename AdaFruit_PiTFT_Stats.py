#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# Original Script:
#    https://github.com/adafruit/Adafruit_CircuitPython_RGB_Display/blob/master/examples/rgb_display_minipitftstats.py
#
# Installation:
#    sudo apt-get install python3-pip
#    sudo pip3 install --upgrade setuptools
#    sudo pip3 install adafruit-circuitpython-rgb-display
#    sudo pip3 install --upgrade --force-reinstall spidev
#    sudo apt-get install ttf-dejavu python3-pil python3-numpy
#    vi /etc/rc.local
#       sudo nice python3 /home/pi/AdaFruit_PiTFT_Stats.py &
#
# Source: https://learn.adafruit.com/adafruit-mini-pitft-135x240-color-tft-add-on-for-raspberry-pi/python-setup
#

import time
import subprocess
import digitalio
import board
from PIL import Image, ImageDraw, ImageFont
import adafruit_rgb_display.st7789 as st7789


# Configuration for CS and DC pins (these are FeatherWing defaults on M0/M4):
cs_pin = digitalio.DigitalInOut(board.CE0)
dc_pin = digitalio.DigitalInOut(board.D25)
reset_pin = None

# Config for display baudrate (default max is 24mhz):
BAUDRATE = 64000000

# Setup SPI bus using hardware SPI:
spi = board.SPI()

# Create the ST7789 display:
disp = st7789.ST7789(
    spi,
    cs=cs_pin,
    dc=dc_pin,
    rst=reset_pin,
    baudrate=BAUDRATE,
    width=240,
    height=240,
    x_offset=0,
    y_offset=80,
)

# Create blank image for drawing.
# Make sure to create image with mode 'RGB' for full color.
height = disp.width  # we swap height/width to rotate it to landscape!
width = disp.height
image = Image.new("RGB", (width, height))
rotation = 180

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw a black filled box to clear the image.
draw.rectangle((0, 0, width, height), outline=0, fill=(0, 0, 0))
disp.image(image, rotation)
# Draw some shapes.
# First define some constants to allow easy resizing of shapes.
padding = -2
top = padding
bottom = height - padding
# Move left to right keeping track of the current x position for drawing shapes.
x = 0


# Alternatively load a TTF font.  Make sure the .ttf font file is in the
# same directory as the python script!
# Some other nice fonts to try: http://www.dafont.com/bitmap.php
font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 28)

# Turn on the backlight
backlight = digitalio.DigitalInOut(board.D22)
backlight.switch_to_output()
backlight.value = True


cpu_cores = subprocess.check_output("nproc", shell=True).decode("utf-8")
def load_color(value):  # Scales with multiple cores 
        if float(value) > (0.99 + int(cpu_cores)-1):
            return "#FF0000"
        elif float(value) > (0.79 + int(cpu_cores)-1):
            return "#FFFF00"
        else:
            return "#00FF00"


def percent_color(value):
        if float(value) > 89:
            return "#FF0000"
        elif float(value) > 49:
            return "#FFFF00"
        else:
            return "#00FF00"


def temp_color(value):
        if int(value) > 175:   # Pi throttles at 80C and has a Max Temp of 85C
            return "#FF0000"
        elif int(value) > 139: # Arbitrary Yellow Warning at 60C
            return "#FFFF00"
        else:
            return "#00FF00"


buttonA = digitalio.DigitalInOut(board.D23)
buttonB = digitalio.DigitalInOut(board.D24)
buttonA.switch_to_input()
buttonB.switch_to_input()

print('Press Ctrl+C to exit script...')

try:
    while True:
        # Draw a black filled box to clear the image.
        draw.rectangle((0, 0, width, height), outline=0, fill=0)

        # Playing with the buttons
        if buttonB.value and not buttonA.value:  # just button A pressed
            draw.rectangle((0, 0, width, height), outline=0, fill="#F65016")
        if buttonA.value and not buttonB.value:  # just button B pressed
            draw.rectangle((0, 0, width, height), outline=0, fill="#000044")
        if not buttonA.value and not buttonB.value:  # none pressed
            draw.rectangle((0, 0, width, height), outline=0, fill="#440044")

        # Shell scripts for system monitoring from here:
        # https://unix.stackexchange.com/questions/119126/command-to-display-memory-usage-disk-usage-and-cpu-load

        #cmd = "hostname -I | cut -d' ' -f1"
        #IP = "IP: " + subprocess.check_output(cmd, shell=True).decode("utf-8")
        cmd = "hostname"
        IP = subprocess.check_output(cmd, shell=True).decode("utf-8")

        #cmd = "top -bn1 | grep load | awk '{printf \"CPU Load: %.2f\", $(NF-2)}'"
        cmd = "top -bn1 | grep load | awk '{printf \"%.2f\", $(NF-2)}'"
        CPU = subprocess.check_output(cmd, shell=True).decode("utf-8")

        #cmd = "free -m | awk 'NR==2{printf \"Mem: %s/%s MB  %.0f%%\", $3,$2,$3*100/$2 }'"
        cmd = "free -m | awk 'NR==2{printf \"%.0f\", $3*100/$2 }'"
        MemUsage = subprocess.check_output(cmd, shell=True).decode("utf-8")

        #cmd = 'df -h | awk \'$NF=="/"{printf "Disk: %d/%d GB  %s", $3,$2,$5}\''
        cmd = 'df -h | awk \'$NF=="/"{print $5}\' | awk -F\'%\' \'{print $1}\''
        Disk = subprocess.check_output(cmd, shell=True).decode("utf-8")

        cmd = "cat /sys/class/thermal/thermal_zone0/temp |  awk '{printf \"%.0f\", $(NF-0)*9/5000 + 32}'"  # pylint: disable=line-too-long
        Temp = subprocess.check_output(cmd, shell=True).decode("utf-8")

        # Write four lines of text.
        y = top
        draw.text((x, y), "%s.local" % IP.rstrip(), font=font, fill="#FFFFFF")
        y += font.getsize(IP)[1] + 6
        draw.text((x, y), "cores:   %s" % cpu_cores, font=font, fill="#999999")
        y += font.getsize(IP)[1] + 6
        draw.text((x, y), "Load:    %2.2f" % float(CPU), font=font, fill=load_color(CPU))
        y += font.getsize(CPU)[1] + 6
        draw.text((x, y), "Mem:    %2i%%" % int(MemUsage), font=font, fill=percent_color(MemUsage))
        y += font.getsize(MemUsage)[1] + 6
        draw.text((x, y), "Disk:     %2i%%" % int(Disk), font=font, fill=percent_color(Disk))
        y += font.getsize(Disk)[1] + 6
        draw.text((x, y), "CPU Temp: %sF" % Temp, font=font, fill=temp_color(Temp))

        # Display image.
        disp.image(image, rotation)
        time.sleep(0.1)

except KeyboardInterrupt:
        # Draw a black filled box to clear the image.
        draw.rectangle((0, 0, width, height), outline=0, fill=0)
        disp.image(image, rotation)

