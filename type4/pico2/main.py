import time
import os
import machine
import _thread
from random import *
uart = machine.UART(1, 9600)
led=machine.Pin(25, machine.Pin.OUT)

# baton = _thread.allocate_lock()

def function3(endtime):
    init = time.time()
    while True:
        looptime = time.time()
        while(time.time()-looptime)<5 and (time.time()-init)<endtime:
            # baton.acquire()
            uart.write('1'.encode('utf-8'))
            time.sleep(1)
            # baton.release()
        while(time.time()-looptime)>=5 and (time.time()-looptime)<=10 and (time.time()-init)<endtime:
            # baton.acquire()
            uart.write('0'.encode('utf-8'))
            time.sleep(1)
            # baton.release()
        if(time.time() - init)>endtime:
            break
    uart.write("D".encode('utf-8'))

def function4(endtime):
    init = time.time()
    while True:
        if(time.time() - init) > endtime:
            break
        # baton.acquire()
        num = str(randint(0,100))
        if len(num)==1:
            num = "0"+num
        uart.write(num.encode('utf-8'))
        time.sleep(0.1)
        # baton.release()
    uart.write("DN".encode('utf-8'))

def main():
    led.high()
    state = False
    while True:
        if uart.any()>0 and not state:
            data = uart.read().decode('utf-8')
            data = data.split(",")
            state = True
            if len(data) > 2:
                _thread.start_new_thread(function3, (data[1]))
                function4(int(data[3]))
                if data[0] == "3":
                    function3(int(data[1]))
                    break
                elif data[0] == "4":
                    function4(int(data[1]))
                    break
    led.low()
            
main()
