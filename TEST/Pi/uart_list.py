import time
import serial

pico1 = serial.Serial(
  port='/dev/ttyAMA1',
  baudrate = 115200,
  parity=serial.PARITY_NONE,
  stopbits=serial.STOPBITS_ONE,
  bytesize=serial.EIGHTBITS
)

def main():
    data = [0x01,0x0A,0x02,0x05]
    while True:
        time.sleep(1)
        rd = pico1.read()
        if rd:
            print(rd)
            for d in data:
                pico1.write(str(d).encode('utf-8'))
            print("sent : ", data)
    
main()
    