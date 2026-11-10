# ============================================
#  LIGHT READER
#  This program reads a light sensor
#  (called a photocell) and shows a number
#  on the screen once every second.
#  Bright light = BIG number
#  Dark         = SMALL number
# ============================================

# Any line that starts with # is a COMMENT.
# Comments are notes for people to read.
# The computer skips them!


# ---- STEP 1: Get our tools ----

# "ADC" lets the Pico read a sensor and turn it into a number.
from machine import ADC

# "time" lets us tell the Pico to wait.
import time


# ---- STEP 2: Set up the sensor ----

# Our photocell is plugged into pin GP26.
# We give it the name "sensor" so we can use it later.
sensor = ADC(26)


# ---- STEP 3: Read the sensor over and over ----

# "while True:" means "repeat this FOREVER".
# Everything that is indented (pushed in with spaces)
# underneath it will repeat.
while True:

    # Ask the sensor for a number.
    # The number will be between 0 and 65535.
    # We save it in a box called "reading".
    reading = sensor.read_u16()

    # Show the number on the screen.
    print("Light:", reading)

    # Wait 1 second before reading again.
    time.sleep(1)


# ---- TRY THIS! ----
# 1. Cover the photocell with your hand.
#    What happens to the number?
# 2. Shine a phone flashlight on it.
#    How big can you make the number?
