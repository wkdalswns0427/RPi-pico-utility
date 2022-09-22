# RPi4-PICO-Communication

RaspberryPi4 and PICO virtual sensor communication

## SETUP

### HW config

- Raspberry Pi 4B 8Gb [raspbeeypiOS 64bit]
- Raspberry Pi PICO [sensor1 sensor2, micropython]
- Raspberry Pi PICO [sensor3 sensor4, micropython]

---

### Communication

- Interface : UART
- Protocol : Custom 8N1

will use uart ports on ttyAMA1(Rx 28, Tx 27) and ttyAMA4(Rx 33, Tx 32)

---

## CODES

### Type 1

using files in /type1

This program chooses **one sensor**, and receives data via uart

- connect Pi4 and PICO using usb interface
- connect RPi(GPIO27,GPIO28) and PICO1(GPIO5, GPIO4) for sensor device1
- connect RPi(GPIO32,GPIO33) and PICO2(GPIO5, GPIO4) for sensor device2
- turn on "Thonny" on raspberry pi
- open 'main.py' and run
- type in sensor no(1,2 for dev1 / 3,4 for dev2) & time on terminal

---

### Type 2

using files in /type2

This program chooses **two sensors**, and receives data via uart

input : "no_of_sens,sensorno1,time1,sensorno2,time2" seperated by comma

connect (may need usb connection, automatic init nor resolved)

- RPi(GPIO27,GPIO28) and PICO1(GPIO5, GPIO4)
- RPi(GPIO32,GPIO33) and PICO2(GPIO5, GPIO4)

turn on "Thonny" on raspberry pi

- open 'main.py' and run
- type in sensor no & time on terminal

single sensor

![Screenshot from 2022-09-22 10-39-37](https://user-images.githubusercontent.com/68832065/191639566-d77f5115-006d-4b3c-ae2e-30aca63defcb.png)

double sensor

![Screenshot from 2022-09-22 10-25-52](https://user-images.githubusercontent.com/68832065/191638172-ce735787-d74b-48cd-a46a-a5e49ad87b93.png)

---

### Type 4

using files in /type2

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
- type in sensor no & time on terminal

---
Connection Image

![20220920_175545](https://user-images.githubusercontent.com/68832065/191214689-bde92233-fc61-4595-91fc-a26a63eef96a.jpg)

UART PINMAP

![Screenshot from 2022-09-16 10-28-28](https://user-images.githubusercontent.com/68832065/190536895-26a9b863-89ed-415a-84b4-b041fe700060.png)
