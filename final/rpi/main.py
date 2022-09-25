# rpi4 code
import time
import serial

#sensor1
pico1 = serial.Serial(
  port='/dev/ttyAMA1',
  baudrate = 9600,
  parity=serial.PARITY_NONE,
  stopbits=serial.STOPBITS_ONE,
  bytesize=serial.EIGHTBITS,
  timeout = 0.1
)

#sensor2
pico1_1 = serial.Serial(
  port='/dev/ttyAMA2',
  baudrate = 9600,
  parity=serial.PARITY_NONE,
  stopbits=serial.STOPBITS_ONE,
  bytesize=serial.EIGHTBITS,
  timeout = 0.1
)

#sensor4
pico2 = serial.Serial(
  port='/dev/ttyAMA4',
  baudrate = 9600,
  parity=serial.PARITY_NONE,
  stopbits=serial.STOPBITS_ONE,
  bytesize=serial.EIGHTBITS,
  timeout = 0.1
)

#sensor3
pico2_1 = serial.Serial(
  port='/dev/ttyAMA3',
  baudrate = 9600,
  parity=serial.PARITY_NONE,
  stopbits=serial.STOPBITS_ONE,
  bytesize=serial.EIGHTBITS,
  timeout = 0.1
)

msg = ""
# DATA buffer list
sensor1, sensor2, sensor3, sensor4 = [], [], [], []

# check message for termination
def confirm_end(msg):
    if msg == "D" or msg == "DN":
        return True
    else:
        return False

def main():
    print("type in according to protocol \"no_of_sens,sensorno1,time1,sensorno2,time2\"")
    a = input("input : ")
    data = a.split(",")
    no_of_sensors = int(data[0])
    sensor1, sensor2, sensor3, sensor4 = [], [], [], []
    
    # <---------- use one sensor ----------> 
    if no_of_sensors==1:
        # devlen decides bytes of read data
        devlen = 1
        if int(data[1])%2==0:
            devlen = 2
        print("dev : {dev}, devlen : {devlen}".format(dev = data[1], devlen=devlen))

        if data[1]=="1" or data[1]=="2":
            senddata = data[1]+","+data[2]
            pico1.write(senddata.encode('utf-8'))
            while True:
                time.sleep(0.1)
                if data[1]=="1":
                    b = pico1.read(devlen)
                    msg = b.decode('utf-8')
                elif data[1]=="2":
                    b = pico1_1.read(devlen)
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
                if data[1]=="3":
                    b = pico2_1.read(devlen)
                    msg = b.decode('utf-8')
                elif data[1]=="4":
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
        flag = 0
        print("mode two sensors : {sensor1}, {sensor2}".format(sensor1=data[1], sensor2=data[3]))
        # devlen decides bytes of read data
        # sensor 1,3 --> 1byte, 2,4 --> 2bytes
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
            if devlen[0]==1:
                d1 = pico1.read(devlen[0]) # sensor1
            else:
                d1 = pico1_1.read(devlen[0]) # sensor2

            if devlen[1]==1:
                d2 = pico2_1.read(devlen[1]) # sensor3
            else:
                d2 = pico2.read(devlen[1]) # sensor4
            msg1, msg2 = d1.decode('utf-8'), d2.decode('utf-8')

            # breaks loop when both sensors reach termination
            if confirm_end(msg1) or confirm_end(msg2):
                flag += 1
                if flag == 2:
                    break
            sensor1.append(msg1)
            sensor2.append(msg2)
            print(msg1, msg2)
        # append data info
        sensor1.append("data of sensor"+data[1]+","+data[2]+"secs")
        sensor2.append("data of sensor"+data[3]+","+data[4]+"secs")

        # remove dummy, useless data
        remove_set = {"","D","DN","00"}
        sensor1 = [i for i in sensor1 if i not in remove_set]
        sensor2 = [i for i in sensor2 if i not in remove_set]
        print("result1 :", sensor1, " ,", "result2 :", sensor2)
        print("program exit")

    # <---------- use four sensors ----------> 
    elif no_of_sensors==4:
        flag = 0
        print("mode all sensors")
        senddata1 = data[1]+","+data[2]+","+data[3]+","+data[4]
        senddata2 = data[5]+","+data[6]+","+data[7]+","+data[8]
        pico1.write(senddata1.encode('utf-8'))
        pico2.write(senddata2.encode('utf-8'))
        begin = time.time()
        while True:
            d1 = pico1.read(1)
            d2 = pico1_1.read(2)
            d3 = pico2_1.read(1)
            d4 = pico2.read(2)
            msg1, msg2, msg3, msg4  = d1.decode('utf-8'), d2.decode('utf-8'), d3.decode('utf-8'), d4.decode('utf-8')
            # breaks loop when all sensors reach termination
            if confirm_end(msg1) or confirm_end(msg2) or confirm_end(msg3) or confirm_end(msg4):
                flag += 1
                if flag == 4:
                    break
            sensor1.append(msg1)
            sensor2.append(msg2)
            sensor3.append(msg3)
            sensor4.append(msg4)
            print(msg1, msg2, msg3, msg4)
        # append data info
        sensor1.append("data of sensor"+data[1]+","+data[2]+"secs")
        sensor2.append("data of sensor"+data[3]+","+data[4]+"secs")
        sensor3.append("data of sensor"+data[5]+","+data[6]+"secs")
        sensor4.append("data of sensor"+data[7]+","+data[8]+"secs")

        # remove dummy, useless data
        remove_set = {"","D","DN","00"}
        sensor1 = [i for i in sensor1 if i not in remove_set]
        sensor2 = [i for i in sensor2 if i not in remove_set]
        sensor3 = [i for i in sensor3 if i not in remove_set]
        sensor4 = [i for i in sensor4 if i not in remove_set]
        print("result1 :", sensor1, " ,", "result2 :", sensor2)
        print("result3 :", sensor3, " ,", "result4 :", sensor4)
        print("program exit")
        
main()
