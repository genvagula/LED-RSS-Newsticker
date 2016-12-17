# led-rss-ampron-led-newsticker
Displays news from RSS feeds to a LED matrix displays


1. Perequisite Software

You will need to get into a command line via the HDMI monitor, ssh or console cable. You will also need to make sure your Pi is on the Internet via a WiFi or Ethernet connection.

First, let's install some prerequisite software for compiling the code:

sudo apt-get update
sudo apt-get install python-dev python-imaging

Then download and uncompress the matrix code package from github:

Copy Code
wget https://github.com/adafruit/rpi-rgb-led-matrix/archive/master.zip
unzip master.zip
The LED-matrix library is (c) Henner Zeller h.zeller@acm.org with GNU General Public License Version 2.0 http://www.gnu.org/licenses/gpl-2.0.txt