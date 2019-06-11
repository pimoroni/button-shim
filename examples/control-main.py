#!/usr/bin/env python
import time
import signal
import buttonshim

print("""
Button SHIM: control-main.py

Light up the LED a different color of the rainbow with each button pressed.
""")

@buttonshim.on_press(buttonshim.BUTTON_A)
def button_a(button, pressed):
    global button_flag
    button_flag = "button_1"
    
@buttonshim.on_press(buttonshim.BUTTON_B)
def button_b(button, pressed):
    global button_flag
    button_flag = "button_2"
    
@buttonshim.on_press(buttonshim.BUTTON_C)
def button_c(button, pressed):
    global button_flag
    button_flag = "button_3"

@buttonshim.on_press(buttonshim.BUTTON_D)
def button_d(button, pressed):
    global button_flag
    button_flag = "button_4"

@buttonshim.on_press(buttonshim.BUTTON_E)
def button_e(button, pressed):    
    global button_flag
    button_flag = "button_5"
    
button_flag = "null"  

while True:
   time.sleep(.1)
   if button_flag == "button_1":
       buttonshim.set_pixel(0x94, 0x00, 0xd3)
       button_flag = "null"
   elif button_flag == "button_2":
       buttonshim.set_pixel(0x00, 0x00, 0xff)
       button_flag = "null"
   elif button_flag == "button_3":    
       buttonshim.set_pixel(0x00, 0xff, 0x00)
       button_flag = "null"
   elif button_flag == "button_4":       
       buttonshim.set_pixel(0xff, 0xff, 0x00)
       button_flag = "null"
   elif button_flag == "button_5":   
       buttonshim.set_pixel(0xff, 0x00, 0x00)
       button_flag = "null"