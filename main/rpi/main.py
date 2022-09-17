# rpi4 code
import time
import serial

pico1 = serial.Serial(
  port='/dev/ttyAMA1',
  baudrate = 115200,
  parity=serial.PARITY_NONE,
  stopbits=serial.STOPBITS_ONE,
  bytesize=serial.EIGHTBITS
)
pico2 = serial.Serial(
  port='/dev/ttyAMA4', # Change this according to connection methods, e.g. /dev/ttyUSB0
  baudrate = 115200,
  parity=serial.PARITY_NONE,
  stopbits=serial.STOPBITS_ONE,
  bytesize=serial.EIGHTBITS
)
msg = ""
sensor1, sensor2, sensor3, sensor4 = [], [], [], []

a = input("choose sensor : ")
if a=="1" or a=="2":
    pico1.write(a.encode('utf-8'))
    t = input("declare time : ")
    pico1.write(t.encode('utf-8'))
    while True:
        time.sleep(0.1)
        b = pico1.read(1)
        msg = b.decode('utf-8')
        print(msg)
        
    
elif a=="3":
    pico2.write(a.encode('utf-8'))
    t = input("declare time : ")
    pico2.write(t.encode('utf-8'))
    while True:
        time.sleep(0.1)
        b = pico2.read(1)
        msg = b.decode('utf-8')
        print(msg)

elif a=="4":
    pico2.write(a.encode('utf-8'))
    t = input("declare time : ")
    pico2.write(t.encode('utf-8'))
    while True:
        time.sleep(0.1)
        b = pico2.read(2)
        msg = b.decode('utf-8')
        print(msg)

'''
while True:
  time.sleep(0.1)
  if a=="4":
      b = pico2.read(2)
  elif a=="3":
      b = pico2.read(1)
  elif a=="1" or a=="2":
      b = pico1.read(1)
  msg = b.decode('utf-8')
  print(msg)
'''