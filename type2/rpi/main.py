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
mulsens1, mulsens2 = [], []

def main():
    a = input("choose sensor in order (ex. \"1,3\"): ")
    if len(a)==1:
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

    elif len(a)>1:
        a = a.split(",")
        pico1.write(a[0].encode('utf-8'))
        pico2.write(a[1].encode('utf-8'))
        t = input("declare time in ordr (ex. \"10,15\"): ")
        t = t.split(",")
        pico1.write(t[0].encode('utf-8'))
        pico2.write(t[1].encode('utf-8'))

        devlen = [1,1]
        for i in range(2):
            if int(a[i])%2==0:
                devlen[i] = 2

        while True:
            time.sleep(0.1)
            d1,d2 = pico1.read(devlen[0]), pico2.read(devlen[1])
            msg1, msg2 = d1.decode('utf-8'), d2.decode('utf-8')
            if (msg1 == "DN" or msg1=="D") and (msg2 == "DN" or msg2=="D"):
                print("result1 :", sensor4, "\n", "result2 :", sensor4,)
                print("program exit")
                break
            mulsens1.append(msg1)
            mulsens2.append(msg2)
        
main()

# t = input("declare time in ordr (ex. \"10,15\"): ")
# t = t.split(",")
# print(type(t[0]))