import time
import os
import machine
from machine import Pin
from random import *
uart = machine.UART(1, 115200)
print(uart)
led=Pin(25, Pin.OUT)


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
        num = str(randint(0,100))
        if len(num)==1:
            num = "0"+num
        uart.write(num.encode('utf-8'))
        time.sleep(0.1)
    uart.write("DN".encode('utf-8'))

def main():
    led.toggle()
    sens, secs = None, None
    uart.write("I".encode('utf-8'))
    while True:
        if sens == None and uart.any():
            sens = uart.readline().decode('utf-8')
            time.sleep(3)
            secs = int(uart.readline().decode('utf-8'))  
        if sens == "3":
            function3(secs)
            break
        elif sens == "4":
            function4(secs)
            break
    uart.write("D".encode('utf-8'))
    led.toggle()
            
main()

