import feedparser
from PIL import Image, ImageFont, ImageDraw

items=[]
displayItems=[]
feeds=[
    "http://www.postimees.ee/rss/",
    "http://feeds.feedburner.com/delfiuudised?format=xml",
    ]
 
def populateItems():
    #first clear out everything
    del items[:]
    del displayItems[:]
    os.system("find . -name \*.ppm -delete")
    for url in feeds:
        feed=feedparser.parse(url)
        posts=feed["items"]
        for post in posts:
            items.append(post)


def createLinks():
    try:
        populateItems()
        bitlink=getConnection()
        for idx, item in enumerate(items):
            data=bitlink.shorten(item["link"])
            writeImage(unicode(item["title"])+" bit.ly/"+data["hash"], idx)
            print(unicode(item["title"]))
            print("bit.ly/"+data["hash"]+"\n")
    except ValueError:
        print("Bummer :( I couldn't make you 'dem links :(")
    finally:
        print("\nWill get more news next half hour!\n\n")

def writeImage(url, count):
    bitIndex=url.find("bit.ly")
    link, headLine=url[bitIndex:], url[:bitIndex]
    def randCol():
        return (random.randint(0,255), random.randint(0,255), random.randint(0,255))
    text = ((headLine, randCol()), (link, (10, 10, 255)))
    font = ImageFont.truetype("/usr/share/fonts/truetype/freefont/FreeSans.ttf", 16)
    all_text = ""
    for text_color_pair in text:
        t = text_color_pair[0]
        all_text = all_text + t
    width, ignore = font.getsize(all_text)
    im = Image.new("RGB", (width + 30, 16), "black")
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
    threading.Timer(3600, run).start()
    showOnLEDDisplay()

def showOnLEDDisplay():
    for disp in displayItems[:60]:
        os.system("sudo ./led-matrix -r 16 -t 60 -D 1 "+disp)

if __name__ == '__main__':
    run()
