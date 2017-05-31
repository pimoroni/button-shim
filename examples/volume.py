#!/usr/bin/env python

import signal
import buttonshim
import subprocess
from sys import version_info

DEVICE = "PCM"

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
    subprocess.Popen(["amixer","set",DEVICE,action],stdout=subprocess.PIPE,stderr=subprocess.PIPE)

def get_volume():
    actual_volume = subprocess.check_output("amixer get '{}' | awk '$0~/%/{{print $4}}' | tr -d '[]%'".format(DEVICE), shell=True)

    if version_info[0] >= 3:
        actual_volume = actual_volume.strip().decode('utf-8')
    else:
        actual_volume = actual_volume.strip()

    return int(actual_volume)

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
@buttonshim.on_press(buttonshim.BUTTON_C)
def button_c(button, pressed):
    global volume

    volume = get_volume()
    volume += 1

    print("Volume: {}%".format(volume))
    set("{}%".format(volume))

    scale = volume / 100.0

    buttonshim.set_pixel(int(0xff * (1.0 - scale)), int(0xff * scale), 0x00)

# Volume Down
@buttonshim.on_press(buttonshim.BUTTON_D)
def button_d(button, pressed):
    global volume

    volume = get_volume()
    volume -= 1

    print("Volume: {}%".format(volume))
    set("{}%".format(volume))

    scale = volume / 100.0

    buttonshim.set_pixel(int(0xff * (1.0 - scale)), int(0xff * scale), 0x00)

# Soft Power Off?
@buttonshim.on_press(buttonshim.BUTTON_E)
def button_e(button, pressed):
    pass

signal.pause()

