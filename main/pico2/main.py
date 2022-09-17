import time
import os
import machine
from random import *
uart = machine.UART(0, 115200)

def function3(endtime):
    init = time.time()
    while True:
        looptime = time.time()
        while(time.time()-looptime)<5 and (time.time()-init)<endtime:
            uart.write('1'.encode('utf-8'))
            time.sleep(1)
        while(time.time()-looptime)>=5 and (time.time()-looptime)<=10 and (time.time()-init)<endtime:
            uart.write('0'.encode('utf-8'))
            time.sleep(1)
        if(time.time() - init)>endtime:
            break

def function4(endtime):
    init = time.time()
    while True:
        if(time.time() - init) > endtime:
            break
        num = randint(0,100)
        uart.write(str(num).encode('utf-8'))
        time.sleep(0.1)

def main():
    sens, secs = None, None
    while True:
        if sens == None and uart.any():
            sens = uart.readline().decode('utf-8')
            time.sleep(3)
            secs = int(uart.readline().decode('utf-8'))
            
        if sens == "3":
            print(sens, secs)
            function3(secs)
            break
        elif sens == "4":
            function4(secs)
            break
            
main()

