import os
import machine
from time import sleep
uart = machine.UART(0, 115200)
print(uart)
b = None
msg = ""
while True:
    sleep(1)
    if uart.any():
        b = uart.readline()
        try:
            msg = b.decode('utf-8')
            print(type(msg))
            print(">> " + msg)
        except:
            pass
    uart.write('receviced'.encode('utf-8'))
    sleep(1)
