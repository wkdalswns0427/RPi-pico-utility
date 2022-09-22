import time
import os
import machine
from random import *
import _thread
uart = machine.UART(1, baudrate=9600)
led=machine.Pin(25, machine.Pin.OUT)

# uart data lock for anti-corruption
baton = _thread.allocate_lock()

def function1(endtime):
    init = time.time()
    while True:
        if (time.time()-init) > endtime:
            break
        for i in range(3):
            baton.acquire()
            if (time.time()-init) > endtime:
                break
            uart.write('1'.encode('utf-8'))
            time.sleep(1)
            baton.release()
        if (time.time()-init) > endtime:
            break
        baton.acquire()
        uart.write('0'.encode('utf-8'))
        time.sleep(1)
        baton.release()
    uart.write("D".encode('utf-8'))

def function2(endtime):
    num = 50
    init = time.time()
    while num<=100:
        if (time.time()-init) > endtime:
            break
        baton.acquire()
        uart.write(str(num).encode('utf-8'))
        time.sleep(1)
        uart.write("00".encode('utf-8'))
        time.sleep(1)
        baton.release()
        num += 2
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
                _thread.start_new_thread(function1, tuple(map(int,data[1])))
                function2(int(data[3]))
            else:
                if data[0] == "1":
                    function1(int(data[1]))
                    break
                elif data[0] == "2":
                    function2(int(data[1]))
                    break
    led.low()
            
main()
