import time
import os
import machine
from random import *
uart = machine.UART(1, baudrate=9600)
led = machine.Pin(25, machine.Pin.OUT)

def second_thread():
    while True:
        print("Hello, I'm here in the second thread writting every second")
        time.sleep(1)

_thread.start_new_thread(second_thread, ())

while True:
    led.toggle()
    time.sleep(2)