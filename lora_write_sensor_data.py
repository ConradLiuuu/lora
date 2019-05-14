import serial
import os
import ifroglab
from time import sleep

os.system('sudo chmod a+rw /dev/ttyUSB0')##set lora
os.system('sudo chmod a+rw /dev/ttyACM1')## set arduino


LoRa2 = ifroglab.LoRa()

ser_arduino = serial.Serial("/dev/ttyACM1",9600,timeout = 0.5)

#Open port
print("Open port")
ser_lora = LoRa2.FunLora_initByName("/dev/ttyUSB0")

#Read firmware  version
print("Get firmware version")
LoRa2.FunLora_0_GetChipID()

#Reset and Init
print("Reset & Init")

#Read setup
print("Read setup")
LoRa2.FunLora_2_ReadSetup()

while True:
    #LoRa2.FunLora_3_TX();
    sensor = ser_arduino.readline()
    #print(type(sensor))
    print(sensor.decode())

    LoRa2.FunLora_5_write16bytesArrayString(str(sensor))
    #sleep(1)

#close
LoRa2.FunLora_close()

