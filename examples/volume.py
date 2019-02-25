#!/usr/bin/env python

import signal
import buttonshim
import subprocess
import time
from sys import version_info

DEVICE = "PCM"
VOL_REPEAT = 0.2

print("""
Button SHIM: volume.py

Control the audio volume on your Raspberry Pi!

A = Unmute
B = Mute
C = Volume Up
D = Volume Down
E = Hold to power off

Press Ctrl+C to exit.

""")

volume = 0


def set(action):
    subprocess.Popen(
        ["amixer", "set", DEVICE, action],
        stdout=subprocess.PIPE, stderr=subprocess.PIPE)


def get_volume():
    actual_volume = subprocess.check_output(
        "amixer get '{}' | awk '$0~/%/{{print $4}}' | tr -d '[]%'".format(DEVICE),
        shell=True)

    if version_info[0] >= 3:
        actual_volume = actual_volume.strip().decode('utf-8')
    else:
        actual_volume = actual_volume.strip()

    actual_volume = int(actual_volume)
    actual_volume = min(100, actual_volume)
    actual_volume = max(0, actual_volume)

    return actual_volume


# Unmute
@buttonshim.on_press(buttonshim.BUTTON_A)
def button_a(button, pressed):
    global volume

    print("Status: Unmute")
    set("unmute")

    volume = get_volume()
    scale = volume / 100.0

    buttonshim.set_pixel(int(0xff * (1.0 - scale)), int(0xff * scale), 0x00)


# Mute
@buttonshim.on_press(buttonshim.BUTTON_B)
def button_b(button, pressed):
    print("Status: Mute")
    set("mute")

    buttonshim.set_pixel(0xff, 0x00, 0x00)


# Volume Up
@buttonshim.on_press(buttonshim.BUTTON_C, repeat=True, repeat_time=VOL_REPEAT)
def button_c(button, pressed):
    global volume

    volume = get_volume()
    volume += 1
    volume = min(100, volume)

    print("Volume: {}%".format(volume))
    set("{}%".format(volume))

    scale = volume / 100.0

    buttonshim.set_pixel(int(0xff * (1.0 - scale)), int(0xff * scale), 0x00)


# Volume Down
@buttonshim.on_press(buttonshim.BUTTON_D, repeat=True, repeat_time=VOL_REPEAT)
def button_d(button, pressed):
    global volume

    volume = get_volume()
    volume -= 1
    volume = max(0, volume)

    print("Volume: {}%".format(volume))
    set("{}%".format(volume))

    scale = volume / 100.0

    buttonshim.set_pixel(int(0xff * (1.0 - scale)), int(0xff * scale), 0x00)


# Soft Power Off?
@buttonshim.on_press(buttonshim.BUTTON_E)
def button_e_press(button, pressed):
    buttonshim.set_pixel(0xff, 0x00, 0x00)


@buttonshim.on_hold(buttonshim.BUTTON_E, hold_time=2)
def button_e(button):
    print("Held for 2sec!")
    time.sleep(0.1)
    for x in range(3):
        buttonshim.set_pixel(0xff, 0x00, 0x00)
        time.sleep(0.1)
        buttonshim.set_pixel(0x00, 0x00, 0x00)
        time.sleep(0.1)


signal.pause()
