# RPi4-PICO-Communication

RaspberryPi4 and PICO virtual sensor communication

## SETUP

### HW config

- Raspberry Pi 4B 8Gb [raspberrypiOS 64bit]
- Raspberry Pi PICO [sensor1 sensor2, micropython]
- Raspberry Pi PICO [sensor3 sensor4, micropython]

---

### Communication

- Interface : UART
- Protocol : Custom 8N1

will use uart ports on ttyAMA1 to ttyAMA4 of raspberry pi4

---

## CODES

### 1 Sensor

This program chooses **one sensor**, and receives data via uart

- connect Pi4 and PICO using usb interface
- connect RPi(GPIO27,GPIO28) and PICO1(GPIO5, GPIO4) for sensor device1
- connect RPi(GPIO32,GPIO33) and PICO2(GPIO5, GPIO4) for sensor device2
- turn on "Thonny" on raspberry pi
- open 'main.py' and run
- type in sensor no(1,2 for dev1 / 3,4 for dev2) & time on terminal

single sensor

![Screenshot from 2022-09-22 10-39-37](https://user-images.githubusercontent.com/68832065/191639566-d77f5115-006d-4b3c-ae2e-30aca63defcb.png)

---

### 2 Sensors

This program chooses **two sensors**, and receives data via uart

input : "no_of_sens,sensorno1,time1,sensorno2,time2" seperated by comma

connect (need usb connection, automatic init not resolved)

- RPi(GPIO27,GPIO28) and PICO1(GPIO5, GPIO4)
- RPi(GPIO32,GPIO33) and PICO2(GPIO5, GPIO4)

turn on "Thonny" on raspberry pi

- open 'main.py' from pico and run (repeat for another pico)
- type in sensor no & time according to protocol on terminal

double sensor

![Screenshot from 2022-09-22 10-25-52](https://user-images.githubusercontent.com/68832065/191638172-ce735787-d74b-48cd-a46a-a5e49ad87b93.png)

---

### 4 Sensors

This program chooses **four sensors**, and receives data via uart

input : "no_of_sens,sensor1,time1,sensor2,time2,sensor3,time3,sensor4,time4" seperated by comma

connect (may need usb connection, automatic init not resolved)

PICO1

- RPi(GPIO27,GPIO28) and PICO1(GPIO5, GPIO4) : AMA1 sensor1
- RPi(GPIO07,GPIO29) and PICO1(GPIO2, GPIO1) : AMA2 sensor2

PICO2

- RPi(GPIO32,GPIO33) and PICO2(GPIO5, GPIO4) : AMA4 sensor3
- RPi(GPIO24,GPIO21) and PICO1(GPIO2, GPIO1) : AMA3 sensor4

turn on "Thonny" on raspberry pi

- open 'main.py' and run
- type in sensor no & time on terminal according to protocol

quadro sensors

![t4](https://user-images.githubusercontent.com/68832065/192141114-57d37158-2800-4339-bfdd-6ae57ce0799f.JPG)

---
Connection Image

![뒤](https://user-images.githubusercontent.com/68832065/192139064-2021ef3a-270e-41a7-8ceb-30a1c882b999.jpg)
