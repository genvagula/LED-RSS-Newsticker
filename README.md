# led-rss-ampron-led-newsticker
Displays news from RSS feeds to a LED matrix displays

Works with LED-matrix library made by (c) Henner Zeller h.zeller@acm.org
https://github.com/hzeller/rpi-rgb-led-matrix

# Background Knowledge



# Perequisite Software
You will need to get into a command line via the HDMI monitor, ssh or console cable. You will also need to make sure your Pi is on the Internet via a WiFi or Ethernet connection.

To get started with the code, first install Python Imaging Library (PIL) to add support for drawing shapes (lines, circles, etc.) and loading images (GIF, PNG, JPEG, etc.). PIL is not always installed by default on some systems, so let's start with:

```
sudo apt-get update
sudo apt-get install python-dev python-imaging
```

PIL graphics do not have an immediate effect on the display. The image is drawn into a separate buffer, which is then copied to the matrix. On the plus side, this extra step affords us the opportunity for smooth animation and scrolling.
The rgbmatrix.so library only supports these image modes: RGB (full color) (RGBA is also supported but the alpha channel is ignored); color palette (such as GIF images use); and bitmap (black/white). Colorspaces like CMYK and YCbCr are not directly handled, but you might be able to convert these to RGB through other PIL functions.

Core PIL image functions are explained here: The Image Module /http://effbot.org/imagingbook/image.htm/
Graphics functions (lines, etc.) are here: The ImageDraw Module /http://effbot.org/imagingbook/imagedraw.htm/



Setup main code:
```
git clone https://github.com/hzeller/rpi-rgb-led-matrix
cd rpi-rgb-led-matrix
cd lib
nano Makefile
```

'/Work on this file is not yet finished and is ongoing/'
