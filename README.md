# RPi4-PICO-Communication
RaspberryPi4 and PICO virtual sensor communication

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

connect (may need usb connection, automatic init nor resolved)
- RPi(GPIO27,GPIO28) and PICO1(GPIO5, GPIO4)
- RPi(GPIO32,GPIO33) and PICO2(GPIO5, GPIO4)

turn on "Thonny" on raspberry pi
- open 'main.py' and run
- type in sensor no & time on terminal

---
Connection Image

![20220920_175545](https://user-images.githubusercontent.com/68832065/191214689-bde92233-fc61-4595-91fc-a26a63eef96a.jpg)

UART PINMAP

![Screenshot from 2022-09-16 10-28-28](https://user-images.githubusercontent.com/68832065/190536895-26a9b863-89ed-415a-84b4-b041fe700060.png)
