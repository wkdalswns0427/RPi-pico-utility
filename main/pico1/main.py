import time
import os
import machine
from random import *
uart = machine.UART(0, 115200)

def function1(endtime):
    init = time.time()
    while True:
        if (time.time()-init) > endtime:
            break
        for i in range(3):
            if (time.time()-init) > endtime:
                break
            uart.write('1'.encode('utf-8'))
            time.sleep(1)
        if (time.time()-init) > endtime:
            break
        uart.write('0'.encode('utf-8'))
        time.sleep(1)

def function2(endtime):
    num = 50
    init = time.time()
    while num<=100:
        if (time.time()-init) > endtime:
            break
        uart.write(str(num).encode('utf-8'))
        time.sleep(2)
        num += 2
        
def main():
    sens, secs = None, None
    while True:
        if sens == None and uart.any():
            sens = uart.readline().decode('utf-8')
            time.sleep(3)
            secs = int(uart.readline().decode('utf-8'))          
        if sens == "1":
            function1(secs)
            break
        elif sens == "2":
            function2(secs)
            break
            
main()

