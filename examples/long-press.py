#!/usr/bin/env python

import signal
import buttonshim


print("""
Buttom SHIM: Long Press

Demonstrates how you might handle both a
short and long press on the same button.

Press or hold the A button.

Press Ctrl+C to exit!

""")


button_was_held = False


@buttonshim.on_press(buttonshim.BUTTON_A)
def press_handler(button, pressed):
    global button_was_held    # So we change the global var defined above
    button_was_held = False   # Reset the button held state


@buttonshim.on_release(buttonshim.BUTTON_A)
def release_handler(button, pressed):
    if not button_was_held:
        print("Short press detected!")


@buttonshim.on_hold(buttonshim.BUTTON_A, hold_time=2)
def hold_handler(button):
    global button_was_held
    button_was_held = True
    print("Long press detected!")


signal.pause()  # Stop script from immediately exiting
