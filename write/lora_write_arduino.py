import serial
import os
import ifroglab
from time import sleep, clock

os.system('sudo chmod a+rw /dev/ttyUSB0')##set lora
os.system('sudo chmod a+rw /dev/ttyACM0')## set arduino


LoRa2 = ifroglab.LoRa()

ser_arduino = serial.Serial("/dev/ttyACM0",9600,timeout = 0.5)

#Open port
print("Open port")
ser_lora = LoRa2.FunLora_initByName("/dev/ttyUSB0")

#Read firmware  version
print("Get firmware version")
LoRa2.FunLora_0_GetChipID()

#Reset and Init
print("Reset & Init")
LoRa2.FunLora_1_Init()

#Read setup
print("Read setup")
LoRa2.FunLora_2_ReadSetup()
LoRa2.FunLora_3_TX()
while True:
    #tic = clock()
    sensor = ser_arduino.readline()
    #print(sensor)
    #print(sensor.decode())
    #print(type(sensor))
    LoRa2.FunLora_5_write16bytesArrayString(str(sensor))
    #sleep(0.5)
    #toc = clock()
    #print("processing time =",toc-tic)

#close
LoRa2.FunLora_close()

