# sender.py
import time
import serial
pico1 = serial.Serial(
  port='/dev/ttyAMA1',
  baudrate = 115200,
  parity=serial.PARITY_NONE,
  stopbits=serial.STOPBITS_ONE,
  bytesize=serial.EIGHTBITS,
  timeout=1
)
pico2 = serial.Serial(
  port='/dev/ttyAMA4', # Change this according to connection methods, e.g. /dev/ttyUSB0
  baudrate = 115200,
  parity=serial.PARITY_NONE,
  stopbits=serial.STOPBITS_ONE,
  bytesize=serial.EIGHTBITS,
  timeout=1
)
msg = ""
i = 0
while True:
    i+=1
    print("Counter {} - Hello from Raspberry Pi".format(i))
    pico1.write('hello'.encode('utf-8'))
    time.sleep(1)
    pico1.readline()
    b = pico1.readline()
    try:
        msg = b.decode('utf-8')
        print(type(msg))
        print(">> " + msg)
    except:
        pass
    time.sleep(1)
