import time
import os
import machine
from random import *
import _thread
uart = machine.UART(1, baudrate=9600)
led = machine.Pin(25, machine.Pin.OUT)

def second_thread():
    while True:
        uart.write('core1'.encode('utf-8'))
        time.sleep(1)

_thread.start_new_thread(second_thread, ())

while True:
    uart.write('core0'.encode('utf-8'))
    time.sleep(2)
