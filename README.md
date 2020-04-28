# NeoPixelPlus
The NeoPixel library plus some extras, for example a testing mode - so you can see how your LEDs would behave directly in the terminal, without any extra hardware.

Want to support the development financially? Donations are always welcomed! 
[Click here to donate on Liberapay](https://liberapay.com/marcoEDU)

[<img src="http://img.shields.io/liberapay/receives/marcoEDU.svg?logo=liberapay">](https://liberapay.com/marcoEDU)

## Installation
```
pip install neopixel_plus
```

## Usage

```
from neopixel_plus import NeoPixel

# Example 1 - Changing the color of a physical LED
pixel = NeoPixel(pin=5, n=30, bpp=3)
pixel.leds[0] = (219,100,222)
pixel.write()

# Example 2 - Testing a rainbow animation in the terminal
NeoPixel(test=True).rainbow_animation()

# Example 3 - Playing a rainbow animation on physical LEDs
NeoPixel(pin=5, n=30, bpp=3).rainbow_animation()

```