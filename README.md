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

This program chooses one sensor, and receives data via uart
- connect Pi4 and PICO using usb interface
- connect RPi(GPIO27,GPIO28) and PICO(GPIO5, GPIO4)
- turn on "Thonny" on raspberry pi
- open 'main.py' and run
- type in sensor no & time on terminal

---
UART PINMAP

![Screenshot from 2022-09-16 10-28-28](https://user-images.githubusercontent.com/68832065/190536895-26a9b863-89ed-415a-84b4-b041fe700060.png)
