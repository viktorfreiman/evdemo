import evdev
from evdev import ecodes
from time import sleep

# flash the numlock, capslock, and scroll lock LEDs
# on the keyboard in a repeating pattern

dev = evdev.InputDevice('/dev/input/event0')

short_delay = 0.1
long_delay = 0.3

while True:
    dev.set_led(ecodes.LED_NUML, 1)
    sleep(short_delay)
    dev.set_led(ecodes.LED_CAPSL, 1)
    sleep(short_delay)
    dev.set_led(ecodes.LED_SCROLLL, 1)
    sleep(long_delay)
    dev.set_led(ecodes.LED_NUML, 0)
    sleep(short_delay)
    dev.set_led(ecodes.LED_CAPSL, 0)
    sleep(short_delay)
    dev.set_led(ecodes.LED_SCROLLL, 0)
    sleep(long_delay)