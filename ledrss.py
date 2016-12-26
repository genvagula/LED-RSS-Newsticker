# THIS SCRIPT USES THE LIBRARY AT:
# https://github.com/hzeller/rpi-rgb-led-matrix
# BE SURE TO CLONE IT AND READ THE README


import os, time, threading, random, signal
import feedparser
from PIL import Image, ImageFont, ImageDraw
from random import shuffle

items=[]
displayItems=[]
feeds=[
    #enter all news feeds you want here
    "http://www.postimees.ee/rss"
    ]

def colorRed():
    return (255, 255, 0)

def colorGreen():
    return (0, 255, 0)

def colorBlue():
    return (0, 0, 255)

def colorRandom():
    return (random.randint(0,255), random.randint(0,255), random.randint(0,255))

def populateItems():
    #first clear out everything
    del items[:]
    del displayItems[:]

    #delete all the image files
    os.system("find . -name '*.ppm' -type f -delete")
    for url in feeds:
        feed=feedparser.parse(url)
        posts=feed["items"]
        for post in posts:
            items.append(post)
    shuffle(items)

def createLinks():
    try:
        populateItems()
        for idx, item in enumerate(items):
            writeImage(unicode(item["title"]), idx)
    except ValueError:
        print("Bummer :( I couldn't make you 'dem links :(")
    finally:
        print("\nWill get more news next half hour!\n\n")

def writeImage(url, count):
    bitIndex=0
    link, headLine="", url[:]
    def randCol(index = -1):
        if index % 3 == 0:
            return colorRed()
        elif index % 3 == 1:
            return colorGreen()
        elif index % 3 == 2:
            return colorBlue()
        else:
            return colorRandom()
    text = ((headLine, randCol(count)), (link, colorRandom()))
    font = ImageFont.truetype("/usr/share/fonts/truetype/freefont/Lato-Regular.ttf", 14)
    all_text = ""
    for text_color_pair in text:
        t = text_color_pair[0]
        all_text = all_text + t
    width, ignore = font.getsize(all_text)
    im = Image.new("RGB", (width + 35, 16), "black")
    draw = ImageDraw.Draw(im)
    x = 0;
    for text_color_pair in text:
        t = text_color_pair[0]
        c = text_color_pair[1]
        draw.text((x, 0), t, c, font=font)
        x = x + font.getsize(t)[0]
    filename=str(count)+".ppm"
    displayItems.append(filename)
    im.save(filename)

def run():
    print("News Fetched at {}\n".format(time.ctime()))
    createLinks()
    threading.Timer(len(items) * 900, run).start()
    showOnLEDDisplay()

def showOnLEDDisplay():
    for disp in displayItems[:900]:
        os.system("sudo ./demo --led-rows=16 --led-chain=3 --led-pwm-bits=5 --led-pwm-lsb-nanoseconds 200 --led-show-refresh --led-brightness=40 -t 25 -D1 "+disp)


#Ctrl-C stuff
def sigint_handler(signum, frame):
	Print ("Stop pressing the CTRL+C!")

signal.signal(signal.SIGINT, sigint_handler)

def main():
	while True:
		Print (".")
		time.sleep(1)


if __name__ == '__main__':
    run()
