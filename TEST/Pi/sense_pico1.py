# sender.py
import time
import serial
pico1 = serial.Serial(
  port='/dev/ttyAMA1',
  baudrate = 115200,
  parity=serial.PARITY_NONE,
  stopbits=serial.STOPBITS_ONE,
  bytesize=serial.EIGHTBITS,
  timeout=0.1
)
pico2 = serial.Serial(
  port='/dev/ttyAMA4', # Change this according to connection methods, e.g. /dev/ttyUSB0
  baudrate = 115200,
  parity=serial.PARITY_NONE,
  stopbits=serial.STOPBITS_ONE,
  bytesize=serial.EIGHTBITS
)
msg = ""

a = input("choose sensor : ")
pico1.write(a.encode('utf-8'))
t = input("declare time : ")
pico1.write(t.encode('utf-8'))
inta = int(a)
sensor1, sensor2 = [], []

while True:
  time.sleep(1)
  b = pico1.readline()
  try:
    msg = b.decode('utf-8')
    if inta == 1:
      sensor1.append(int(msg))
      print(">> ", sensor1)
    elif inta == 2:
      sensor2.append(int(msg))
      print(">> ", sensor2)
  except:
    pass

