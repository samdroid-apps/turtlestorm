# About

Turtle Storm is a turtleblocksjs plugin for the lego mindstorms NXT.
It supports the motors, color sensor, touch sensor and ultrasonic sensor.

# Setup

1. Install deps

        yum install pyusb
        pip install nxt-python

2. Start the NXT server

        python server.py

3. Start turtle art (this plugin **does not** work with t.sl.o, as it is causes
   https mixed content warnings):

        git clone https://github.com/walterbender/turtleblocksjs
        cd turtleblocksjs
        python -m SimpleHTTPServer

4. Load `nxt.json` plugin and have fun!

# Turtle Storm API Docs

	GET /areyouarobot
   
Returns `yes`

	GET /about

Returns a list of motor letters and the number of sensor ports.  Eg:

    {
        "sensors": 4,
        "motors": ["A", "B", "C", "D"]
    }

## Motors

	GET /motor/<letter>/start/<power>

	GET /motor/<letter>/stop
	
	GET /motor/<letter>/idle
	
	GET /motor/<letter>/turn/<deg>/<power>

`power` always ranges from -127 to 128.

## Sensor

	GET /touch/<port>

Returns 1 if touched and 0 if not

	GET /ultrasonic/<port>

Returns the distance in centimeters

	GET /led/<port>/<color>

Change the color sensor LED.  Color options are `blue`, `red`, `green`, `all`, `none`.  `none` turns the light off.

NXT only

	GET /light/<port>

Returns the lightness from 13 to 0

	GET /light/<port>/reflect/<color>

Returns the reflected light using a given color.  From 0 to 1000 (probably).

**Note**: Broken in an odd way

	GET /color/<port>

Returns the color from 1 to 6.

    GET /gyro/angle/<port>

    GET /gyro/angle/<port>

The gyro apis do something... I don't really know.

EV3 only.
