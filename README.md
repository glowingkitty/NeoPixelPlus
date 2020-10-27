![NeoPixelPlus](https://raw.githubusercontent.com/marcoEDU/NeoPixelPlus/master/images/headerimage.jpg "NeoPixelPlus")

The NeoPixel library plus animations and terminal testing mode - so you can see how your LEDs would behave directly in the terminal, without any microcontroller.

Want to support the development and stay updated?

<a href="https://www.patreon.com/bePatron?u=24983231"><img alt="Become a Patreon" src="https://raw.githubusercontent.com/marcoEDU/NeoPixelPlus/master/images/patreon_button.svg"></a> <a href="https://liberapay.com/glowingkitty/donate"><img alt="Donate using Liberapay" src="https://liberapay.com/assets/widgets/donate.svg"></a>

## Overview
1. [Installation](#installation)

2. [Example](#example)

3. [NeoPixel class](#neopixel-class)

    - [pin](#neopixel_pin)

    - [n](#neopixel_n)

    - [start_led](#neopixel_start_led)

    - [test](#neopixel_test)

    - [overwrite_line](#neopixel_overwrite_line)

    - [debug](#neopixel_debug)

    - [target](#neopixel_target)


4. [NeoPixel functions (animations)](#neopixel-functions-animations)

    4.1 [rainbow_animation()](#rainbow_animation)

    - [brightness](#rainbow_animation_brightness)

    - [loop_limit](#rainbow_animation_loop_limit)

    - [duration_ms](#rainbow_animation_duration_ms)

    - [pause_ms](#rainbow_animation_pause_ms)

    - [customization_json](#rainbow_animation_customization_json)

    4.2 [beats()](#beats)

    - [brightness](#beats_brightness)

    - [brightness_fixed](#beats_brightness_fixed)

    - [loop_limit](#beats_loop_limit)

    - [duration_ms](#beats_duration_ms)

    - [pause_ms](#beats_pause_ms)

    - [start](#beats_start)

    - [rgb_colors](#beats_rgb_colors)

    - [num_random_colors](#beats_num_random_colors)

    - [max_height](#beats_num_max_height)

    - [customization_json](#beats_customization_json)

    4.3 [moving_dot()](#moving_dot)

    - [brightness](#moving_dot_brightness)

    - [loop_limit](#moving_dot_loop_limit)

    - [duration_ms](#moving_dot_duration_ms)

    - [pause_a_ms](#moving_dot_pause_a_ms)

    - [pause_b_ms](#moving_dot_pause_a_ms)

    - [start](#moving_dot_start)

    - [rgb_colors](#moving_dot_rgb_colors)

    - [num_random_colors](#moving_dot_num_random_colors)

    - [customization_json](#moving_dot_customization_json)

    4.4 [light_up()](#light_up)

    - [brightness](#light_up_brightness)

    - [loop_limit](#light_up_loop_limit)

    - [duration_ms](#light_up_duration_ms)

    - [pause_ms](#light_up_pause_ms)

    - [sections](#light_up_start)

    - [rgb_colors](#light_up_rgb_colors)

    - [num_random_colors](#light_up_num_random_colors)

    - [customization_json](#light_up_customization_json)

    4.5 [transition()](#transition)

    - [brightness](#transition_brightness)

    - [loop_limit](#transition_loop_limit)

    - [duration_ms](#transition_duration_ms)

    - [pause_ms](#transition_pause_ms)

    - [sections](#transition_start)

    - [rgb_colors](#transition_rgb_colors)

    - [num_random_colors](#transition_num_random_colors)

    - [customization_json](#transition_customization_json)

5. [NeoPixel functions (other)](#neopixel-functions-other)

    5.1 [get_sections()](#get_sections)

    5.2 [get_led_selectors()](#get_led_selectors)

    - [sections](#get_led_selectors_sections)

    5.3 [write()](#write)

    - [s_after_wait](#write_s_after_wait)

    5.4 [get_led()](#get_led)

    - [i](#get_led_i)

    - [start](#get_led_start)

    5.5 [off()](#off)

    5.6 [on()](#on)

    - [num](#on_num)

    5.7 [color()](#color)

    - [rgb_color](#color_rgb_color)

    - [customization_json](#color_customization_json)

    5.8 [test_animations()](#test_animations)

    5.9 [get_pin()](#get_pin)


## Installation
Make sure Python 3 is installed. 

`Recommended: always create a Python Virtual Environment for your project and install neopixel_plus in that environment.`
```
pip install neopixel_plus
```

## Example

IMPORTANT: 

To use NeoPixel+ on Raspberry Pi (using target='adafruit'), you need to make sure you execute python with sudo.
For example:
```
sudo python
```
or from a virtual environment
```
sudo ./pyvenv/bin/python
```


```
from neopixel_plus import NeoPixel

# Example 1 - Changing the color of a physical LED
pixel = NeoPixel(pin=5, n=30)
pixel.leds[0] = (219,100,222)
pixel.write()

# Example 2 - Testing a rainbow animation in the terminal
NeoPixel(test=True).rainbow_animation()

# Example 3 - Playing a rainbow animation on physical LEDs
NeoPixel(pin=5, n=30).rainbow_animation()

```
## NeoPixel class

#### Input:

##### NeoPixel(pin=...)
```python 
type = int
default = 10
purpose = 'The GPIO pin the data wire of the LED strip is connected to'
```

##### NeoPixel(n=...)
```python 
type = int
default = 30
purpose = 'The number of RGB LEDs on your LED strip'
```

##### NeoPixel(start_led=...)
```python 
type = int
default = 0
purpose = 'With which LED should the animation start'
```

##### NeoPixel(test=...)
```python 
type = bool
default = False
purpose = 'If True: show LED simulation in terminal output. If False: connect to real LED strip and play animation.'
```

##### NeoPixel(overwrite_line=...)
```python 
type = bool
default = True
purpose = 'If False: show all steps of LED animation in terminal ouput. Useful for debugging.'
```

##### NeoPixel(debug=...)
```python 
type = bool
default = False
purpose = 'If True: prints all function calls and their input variables, for better debugging.'
```

##### NeoPixel(target=...)
```python 
type = str
default = 'micropython'
options = ['micropython','adafruit']
purpose = 'Defines what kind of NeoPixel library is targeted: the default micropython NeoPixel or adafruits NeoPixel for Raspberry Pi.'
```


## NeoPixel functions (animations)

### rainbow_animation()
![rainbow](https://raw.githubusercontent.com/marcoEDU/NeoPixelPlus/master/images/rainbow.png "rainbow")

#### Input:

##### rainbow_animation(brightness=...)
```python 
type = float
default = 1.0
purpose = 'Set the maximum brightness of the LEDs. 0 == off, 1.0 == 100%'
```

##### rainbow_animation(loop_limit=...)
```python 
type = int
default = None
purpose = 'If set, defines how often animation should repeat, else: animation runs in infinite loop.'
```

##### rainbow_animation(duration_ms=...)
```python 
type = int
default = 1000
purpose = 'Defines many ms should the animation last'
```

##### rainbow_animation(pause_ms=...)
```python 
type = int
default = None
purpose = 'If set, defines if a pause should be made after animation and how long that lasts.'
```

##### rainbow_animation(customization_json=...)
```python 
type = dict
default = {}
purpose = 'If you like, you can also give the customization options via a dict as an imput. Example: {"duration_ms":2000}'
```


### beats()
![beats](https://raw.githubusercontent.com/marcoEDU/NeoPixelPlus/master/images/beats.png "beats")

#### Input:

##### beats(brightness=...)
```python 
type = float
default = 1.0
purpose = 'Set the maximum brightness of the LEDs. 0 == off, 1.0 == 100%'
```

##### beats(brightness_fixed=...)
```python 
type = bool
default = False
purpose = 'If False: the brightness will start low and become high at the end. If True: the brightness stays the same during the animation, for all LEDs.'
```

##### beats(loop_limit=...)
```python 
type = int
default = None
purpose = 'If set, defines how often animation should repeat, else: animation runs in infinite loop.'
```

##### beats(duration_ms=...)
```python 
type = int
default = 200
purpose = 'Defines many ms should the animation last'
```

##### beats(pause_ms=...)
```python 
type = int
default = 300
purpose = 'If set, defines if a pause should be made after animation and how long that lasts.'
```

##### beats(start=...)
```python 
type = str
default = 'start'
options = ['start','end','start + end','center']
purpose = 'Defines from where the animation should start'
```

##### beats(rgb_colors=...)
```python 
type = list
default = list of randomly selected RGB colors (example: [[140,140,144],[240,100,0]])
purpose = 'Define what RGB colors the animation will use'
```

##### beats(num_random_colors=...)
```python 
type = int
default = 5
purpose = 'Defines how many random RGB colors the animation will switch between, if no RGB colors are manually defined'
```

##### beats(max_height=...)
```python 
type = float
default = 1.0
purpose = 'Defines how high the beat animation can go. 1.0 == 100% of all LEDs, 0 == no LEDs.'
```

##### beats(customization_json=...)
```python 
type = dict
default = {}
purpose = 'If you like, you can also give the customization options via a dict as an imput. Example: {"duration_ms":2000}'
```


### moving_dot()
![moving_dot](https://raw.githubusercontent.com/marcoEDU/NeoPixelPlus/master/images/moving_dot.png "moving_dot")

#### Input:

##### moving_dot(brightness=...)
```python 
type = float
default = 1.0
purpose = 'Set the maximum brightness of the LEDs. 0 == off, 1.0 == 100%'
```


##### moving_dot(loop_limit=...)
```python 
type = int
default = None
purpose = 'If set, defines how often animation should repeat, else: animation runs in infinite loop.'
```

##### moving_dot(duration_ms=...)
```python 
type = int
default = 200
purpose = 'Defines many ms should the animation last'
```

##### moving_dot(pause_a_ms=...)
```python 
type = int
default = 0
purpose = 'Defines if pause A should be made and how long that lasts.'
```

##### moving_dot(pause_b_ms=...)
```python 
type = int
default = 300
purpose = 'Defines if pause B should be made and how long that lasts.'
```

##### moving_dot(start=...)
```python 
type = str
default = 'start'
options = ['start','end']
purpose = 'Defines from where the animation should start'
```

##### moving_dot(rgb_colors=...)
```python 
type = list
default = list of randomly selected RGB colors (example: [[140,140,144],[240,100,0]])
purpose = 'Define what RGB colors the animation will use'
```

##### moving_dot(num_random_colors=...)
```python 
type = int
default = 5
purpose = 'Defines how many random RGB colors the animation will switch between, if no RGB colors are manually defined'
```

##### moving_dot(customization_json=...)
```python 
type = dict
default = {}
purpose = 'If you like, you can also give the customization options via a dict as an imput. Example: {"duration_ms":2000}'
```

### light_up()
![light_up](https://raw.githubusercontent.com/marcoEDU/NeoPixelPlus/master/images/light_up.png "light_up")

#### Input:

##### light_up(brightness=...)
```python 
type = float
default = 1.0
purpose = 'Set the maximum brightness of the LEDs. 0 == off, 1.0 == 100%'
```


##### light_up(loop_limit=...)
```python 
type = int
default = None
purpose = 'If set, defines how often animation should repeat, else: animation runs in infinite loop.'
```

##### light_up(duration_ms=...)
```python 
type = int
default = 200
purpose = 'Defines many ms should the animation last'
```

##### light_up(pause_ms=...)
```python 
type = int
default = 200
purpose = 'Defines if pause should be made and how long that lasts.'
```

##### light_up(sections=...)
```python 
type = str or list
default = 'all'
options = ['all',0,1,2,3]
purpose = 'Defines what sections of the LED strip should glow up (one section is 15 LEDs).'
```

##### light_up(rgb_colors=...)
```python 
type = list
default = list of randomly selected RGB colors (example: [[140,140,144],[240,100,0]])
purpose = 'Define what RGB colors the animation will use'
```

##### light_up(num_random_colors=...)
```python 
type = int
default = 5
purpose = 'Defines how many random RGB colors the animation will switch between, if no RGB colors are manually defined'
```

##### light_up(customization_json=...)
```python 
type = dict
default = {}
purpose = 'If you like, you can also give the customization options via a dict as an imput. Example: {"duration_ms":2000}'
```

### transition()
![transition](https://raw.githubusercontent.com/marcoEDU/NeoPixelPlus/master/images/transition.png "transition")

#### Input:

##### transition(brightness=...)
```python 
type = float
default = 1.0
purpose = 'Set the maximum brightness of the LEDs. 0 == off, 1.0 == 100%'
```

##### transition(loop_limit=...)
```python 
type = int
default = None
purpose = 'If set, defines how often animation should repeat, else: animation runs in infinite loop.'
```

##### transition(duration_ms=...)
```python 
type = int
default = 200
purpose = 'Defines many ms should the animation last'
```

##### transition(pause_ms=...)
```python 
type = int
default = 200
purpose = 'Defines if pause should be made and how long that lasts.'
```

##### transition(sections=...)
```python 
type = str or list
default = 'all'
options = ['all',0,1,2,3]
purpose = 'Defines what sections of the LED strip should glow up (one section is 15 LEDs).'
```

##### transition(rgb_colors=...)
```python 
type = list
default = list of randomly selected RGB colors (example: [[140,140,144],[240,100,0]])
purpose = 'Define what RGB colors the animation will use'
```

##### transition(num_random_colors=...)
```python 
type = int
default = 5
purpose = 'Defines how many random RGB colors the animation will switch between, if no RGB colors are manually defined'
```

##### transition(customization_json=...)
```python 
type = dict
default = {}
purpose = 'If you like, you can also give the customization options via a dict as an imput. Example: {"duration_ms":2000}'
```

## NeoPixel functions (other)

### get_sections()
![get_sections](https://raw.githubusercontent.com/marcoEDU/NeoPixelPlus/master/images/get_sections.png "get_sections")
Returns a list of all the LED strip sections (length: 15 LEDs per section).

### get_led_selectors()
![get_led_selectors](https://raw.githubusercontent.com/marcoEDU/NeoPixelPlus/master/images/get_led_selectors.png "get_led_selectors")
Returns a list of all the selector numbers to select specific LEDs in the strip.

#### Input:

##### get_led_selectors(sections=...)
```python 
type = str or list
default = 'all'
options = ['all','random',0,1,2,3]
purpose = 'Defines what sections should be returned.'
```

### write()
![write](https://raw.githubusercontent.com/marcoEDU/NeoPixelPlus/master/images/write.png "write")
Makes the LEDs glow in the color you defined. If test==True: simulates how the LEDs would glow.

#### Input:

##### write(s_after_wait=...)
```python 
type = float
default = 1.0/36.0
purpose = 'Defines how many seconds the code should wait after writing the LED status.'
```

### get_led()
![get_led](https://raw.githubusercontent.com/marcoEDU/NeoPixelPlus/master/images/get_led.png "get_led")
Get the number of an LED, to select it for changing its color.

#### Input:

##### get_led(i=...)
```python 
type = int
purpose = 'Defines which LED you want to get. If <0: LED from the end will be selected.'
```

##### get_led(start=...)
```python 
type = str
default = None
purpose = 'Defines from where your animation starts. If start==end: LEDs will be counted from the end of the LED strip.'
```

### off()
![off](https://raw.githubusercontent.com/marcoEDU/NeoPixelPlus/master/images/off.png "off")
Turns all LEDs off.

### on()
![on](https://raw.githubusercontent.com/marcoEDU/NeoPixelPlus/master/images/on.png "on")
Turns all or specific LEDs on (make them glow white, 100% brightness).

#### Input:

##### on(num=...)
```python 
type = int
default = None
purpose = 'Turn on only one specific LED.'
```

### color()
![color](https://raw.githubusercontent.com/marcoEDU/NeoPixelPlus/master/images/color.png "color")
Turn on all LEDs in a specific RGB color.

#### Input:

##### color(rgb_color=...)
```python 
type = list
purpose = 'Define an [r,g,b] list with the red, green and blue values (from 0-255).'
```

##### color(customization_json=...)
```python 
type = dict
default = {}
purpose = 'If you like, you can also give the customization options via a dict as an imput. Example: {"rgb_color":[100,200,200]}'
```

### test_animations()
![test_animations](https://raw.githubusercontent.com/marcoEDU/NeoPixelPlus/master/images/test_animations.png "test_animations")
Run all the different LED animations from NeoPixel+.

### get_pin()
Returns the class object for the GPIO pin (micropython's and adafruit's NeoPixel use different classes for that).