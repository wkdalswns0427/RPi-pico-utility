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
    print("type in according to protocol \"no_of_sens,sensorno1,time1,sensorno2,time2\"")
    a = input("input : ")
    data = a.split(",")
    no_of_sensors = int(data[0])
    
    # <---------- use one sensor ----------> 
    if no_of_sensors==1:
        devlen = 1
        if int(data[1])%2==0:
            devlen = 2
        print("dev : {dev}, devlen : {devlen}".format(dev = data[1], devlen=devlen))
        if data[1]=="1" or data[1]=="2":
            senddata = data[1]+","+data[2]
            pico1.write(senddata.encode('utf-8'))
            while True:
                time.sleep(0.1)
                b = pico1.read(devlen)
                msg = b.decode('utf-8')
                if msg == "D" or msg == "DN":
                    break
                sensor1.append(msg)
                print(msg)
            sensor1.append("data of sensor"+data[1]+","+data[2]+"secs")
            print("result :", sensor1)
            print("program exit")
                
        elif data[1]=="3" or data[1]=="4":
            senddata = data[1]+","+data[2]
            pico2.write(senddata.encode('utf-8'))
            while True:
                time.sleep(0.1)
                b = pico2.read(devlen)
                msg = b.decode('utf-8')
                if msg == "D" or msg == "DN":
                    break
                sensor1.append(msg)
                print(msg)
            sensor1.append("data of sensor"+data[1]+","+data[2]+"secs")
            print("result :", sensor1)
            print("program exit")

    # <---------- use two sensors ----------> 
    elif no_of_sensors==2:
        print("mode two sensors : {sensor1}, {sensor2}".format(sensor1=data[1], sensor2=data[3]))
        devlen = [1,1]
        for i in range(2):
            if int(data[i*2+1])%2==0:
                devlen[i] = 2

        senddata1 = data[1]+","+data[2]
        senddata2 = data[3]+","+data[4]
        pico1.write(senddata1.encode('utf-8'))
        pico2.write(senddata2.encode('utf-8'))
        while True:
            time.sleep(0.1)
            d1,d2 = pico1.read(devlen[0]), pico2.read(devlen[1])
            msg1, msg2 = d1.decode('utf-8'), d2.decode('utf-8')
            if (msg1 == "DN" or msg1=="D") and (msg2 == "DN" or msg2=="D"):
                break
            sensor1.append(msg1)
            sensor2.append(msg2)
            print(msg1, " , ", msg2)
        sensor1.append("data of sensor"+data[1]+","+data[2]+"secs")
        sensor2.append("data of sensor"+data[3]+","+data[4]+"secs")
        print("result1 :", sensor1, "\n", "result2 :", sensor2)
        print("program exit")
        
main()
