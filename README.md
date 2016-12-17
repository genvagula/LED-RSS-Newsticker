# led-rss-ampron-led-newsticker
Displays news from RSS feeds to a LED matrix displays


Code is originally (c) Henner Zeller h.zeller@acm.org, and I grant you the permission to do whatever you want with it :) 2013-12 - changed to drive a 16x32 matrix (half the original intended)


# Background Knowledge

##Rows
The # of rows is indicated with -r
If you are using a 16 pixel tall matrix (a 16x32) use -r 16
If you are using 32 pixel tall matrix (64x32 or 32x32) use -r 32
j,jn,
##Chained
Each matrix is considered 32 pixels wide. If you have multiple matrices chained use -c to increase the width. If you have 3 chained together, use -c 3 If you have a 64x32 matrix, it looks like 2 chained 32x32 so use -c 2
,.
##Time Running
You can run the demo for a given amount of time with -t e.g. -t 60 is 60 seconds

##Demo
There's a bunch of built-in demos you can run to test out the matrix, start with -D 0 which will show a spinning rainbow square or you can run the -D 1 scrolling image demo, just give it a ppm image to display.


# Perequisite Software
You will need to get into a command line via the HDMI monitor, ssh or console cable. You will also need to make sure your Pi is on the Internet via a WiFi or Ethernet connection.

To get started with the code, first install Python Imaging Library (PIL) to add support for drawing shapes (lines, circles, etc.) and loading images (GIF, PNG, JPEG, etc.). PIL is not always installed by default on some systems, so let's start with:

sudo apt-get update
sudo apt-get install python-dev python-imaging

PIL graphics do not have an immediate effect on the display. The image is drawn into a separate buffer, which is then copied to the matrix. On the plus side, this extra step affords us the opportunity for smooth animation and scrolling.
The rgbmatrix.so library only supports these image modes: RGB (full color) (RGBA is also supported but the alpha channel is ignored); color palette (such as GIF images use); and bitmap (black/white). Colorspaces like CMYK and YCbCr are not directly handled, but you might be able to convert these to RGB through other PIL functions.

Core PIL image functions are explained here: The Image Module /http://effbot.org/imagingbook/image.htm/
Graphics functions (lines, etc.) are here: The ImageDraw Module /http://effbot.org/imagingbook/imagedraw.htm/



Setup code:

git clone https://github.com/hzeller/rpi-rgb-led-matrix
cd rpi-rgb-led-matrix
cd lib
nano Makefile


#Options

$ make
$ sudo ./demo
usage: ./demo <options> -D <demo-nr> [optional parameter]
Options:
        -D <demo-nr>              : Always needs to be set
        -L                        : Large display, in which each chain is 'folded down'
                                    in the middle in an U-arrangement to get more vertical space.
        -R <rotation>             : Sets the rotation of matrix. Allowed: 0, 90, 180, 270. Default: 0.
        -t <seconds>              : Run for these number of seconds, then exit.
        --led-gpio-mapping=<name> : Name of GPIO mapping used. Default "regular"
        --led-rows=<rows>         : Panel rows. 8, 16, 32 or 64. (Default: 32).
        --led-chain=<chained>     : Number of daisy-chained panels. (Default: 1).
        --led-parallel=<parallel> : For A/B+ models or RPi2,3b: parallel chains. range=1..3 (Default: 1).
        --led-pwm-bits=<1..11>    : PWM bits (Default: 11).
        --led-brightness=<percent>: Brightness in percent (Default: 100).
        --led-scan-mode=<0..1>    : 0 = progressive; 1 = interlaced (Default: 0).
        --led-show-refresh        : Show refresh rate.
        --led-inverse             : Switch if your matrix has inverse colors on.
        --led-swap-green-blue     : Switch if your matrix has green/blue swapped on.
        --led-pwm-lsb-nanoseconds : PWM Nanoseconds for LSB (Default: 130)
        --led-no-hardware-pulse   : Don't use hardware pin-pulse generation.
        --led-slowdown-gpio=<0..2>: Slowdown GPIO. Needed for faster Pis and/or slower panels (Default: 1).
        --led-daemon              : Make the process run in the background as daemon.
        --led-no-drop-privs       : Don't drop privileges from 'root' after initializing the hardware.
Demos, choosen with -D
        0  - some rotating square
        1  - forward scrolling an image (-m <scroll-ms>)
        2  - backward scrolling an image (-m <scroll-ms>)
        3  - test image: a square
        4  - Pulsing color
        5  - Grayscale Block
        6  - Abelian sandpile model (-m <time-step-ms>)
        7  - Conway's game of life (-m <time-step-ms>)
        8  - Langton's ant (-m <time-step-ms>)
        9  - Volume bars (-m <time-step-ms>)
        10 - Evolution of color (-m <time-step-ms>)
        11 - Brightness pulse generator
Example:
        ./demo -t 10 -D 1 runtext.ppm
Scrolls the runtext for 10 seconds

