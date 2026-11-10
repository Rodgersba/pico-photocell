# ============================================
#  NIGHTLIGHT
#  This program reads a light sensor
#  (called a photocell). When it gets DARK,
#  the LED turns ON, just like a nightlight!
# ============================================

# Any line that starts with # is a COMMENT.
# Comments are notes for people to read.
# The computer skips them!


# ---- STEP 1: Get our tools ----

# "ADC" lets the Pico read a sensor and turn it into a number.
# "Pin" lets the Pico turn things on and off, like our LED.
from machine import ADC, Pin

# "time" lets us tell the Pico to wait.
import time


# ---- STEP 2: Set up the sensor and the light ----

# Our photocell is plugged into pin GP26.
sensor = ADC(26)

# Our LED is plugged into pin GP15.
# Pin.OUT means the Pico SENDS power OUT to the LED.
led = Pin(15, Pin.OUT)


# ---- STEP 3: Choose when the light turns on ----

# This is our "limit" number.
# Bright light = BIG number. Dark = SMALL number.
# When the reading goes BELOW this number, it is dark,
# so the LED turns on.
# If the light acts strange, try changing this number!
limit = 1500


# ---- STEP 4: Check the sensor over and over ----

# "while True:" means "repeat this FOREVER".
# Everything indented underneath it will repeat.
while True:

    # Ask the sensor for a number (between 0 and 65535).
    # We save it in a box called "reading".
    reading = sensor.read_u16()

    # Show the number on the screen.
    print("Light:", reading)

    # Now the Pico makes a DECISION.
    # "if" asks a yes-or-no question:
    # Is the reading smaller than our limit? (Is it dark?)
    if reading < limit:
        # YES: it is dark, so turn the LED ON.
        led.on()
    else:
        # NO: it is bright, so turn the LED OFF.
        led.off()

    # Wait 1 second, then check again.
    time.sleep(1)


# ---- TRY THIS! ----
# 1. Cover the photocell with your hand. Does the LED turn on?
# 2. Watch the numbers in a bright room and a dark room.
#    Change "limit" so the light turns on at just the right time.
# 3. Challenge: can you make the LED turn on when it is BRIGHT
#    instead? Hint: change just ONE symbol!
