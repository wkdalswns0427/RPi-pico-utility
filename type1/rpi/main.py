# rpi4 code
import time
import serial

pico1 = serial.Serial(
  port='/dev/ttyAMA1',
  baudrate = 9600,
  parity=serial.PARITY_NONE,
  stopbits=serial.STOPBITS_ONE,
  bytesize=serial.EIGHTBITS
)
pico2 = serial.Serial(
  port='/dev/ttyAMA4', # Change this according to connection methods, e.g. /dev/ttyUSB0
  baudrate = 9600,
  parity=serial.PARITY_NONE,
  stopbits=serial.STOPBITS_ONE,
  bytesize=serial.EIGHTBITS
)
msg = ""
sensor1, sensor2, sensor3, sensor4 = [], [], [], []

def main():
    a = input("choose sensor : ")
    if a=="1":
        pico1.write(a.encode('utf-8'))
        t = input("declare time : ")
        pico1.write(t.encode('utf-8'))
        while True:
            time.sleep(0.1)
            b = pico1.read(1)
            msg = b.decode('utf-8')
            if msg == "D":
                print("result :", sensor1)
                print("program exit")
                break
            sensor1.append(msg)
            print(msg)
            
    if a=="2":
        pico1.write(a.encode('utf-8'))
        t = input("declare time : ")
        pico1.write(t.encode('utf-8'))
        while True:
            time.sleep(0.1)
            b = pico1.read(2)
            msg = b.decode('utf-8')
            if msg == "DN":
                print("result :", sensor2)
                print("program exit")
                break
            sensor2.append(msg)
            print(msg)
            
    elif a=="3":
        pico2.write(a.encode('utf-8'))
        t = input("declare time : ")
        pico2.write(t.encode('utf-8'))
        while True:
            time.sleep(0.1)
            b = pico2.read(1)
            msg = b.decode('utf-8')
            if msg == "D":
                print("result :", sensor3)
                print("program exit")
                break
            sensor3.append(msg)
            print(msg)

    elif a=="4":
        pico2.write(a.encode('utf-8'))
        t = input("declare time : ")
        pico2.write(t.encode('utf-8'))
        while True:
            time.sleep(0.1)
            b = pico2.read(2)
            msg = b.decode('utf-8')
            if msg == "DN":
                print("result :", sensor4)
                print("program exit")
                break
            sensor4.append(msg)
            print(msg)
    #elif len(a)>1:
        
        
main()