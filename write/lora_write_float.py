import serial
import os
import ifroglab
from time import sleep, clock

os.system('sudo chmod a+rw /dev/ttyUSB0')##set lora
#os.system('sudo chmod a+rw /dev/ttyACM0')## set arduino


LoRa2 = ifroglab.LoRa()

#ser_arduino = serial.Serial("/dev/ttyACM0",9600,timeout = 0.5)

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

    #sensor = [1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 10.5, 11.5, 12.5, 13.5, 14.5, 15.5, 16.5]
    sensor = [1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 10.5, 11.5, 12.5, 13.5, 14.5, 15.5, 16.5, 17.2, 18.6, 19.4, 20.0]

    if len(sensor) <= 16:
        for i in range(0,len(sensor)):
            LoRa2.FunLora_5_write16bytesArrayString(str(sensor[i]))
    if len(sensor) > 16:
        for i in range(0,16):
            LoRa2.FunLora_5_write16bytesArrayString(str(sensor[i]))

        for i in range(16,len(sensor)):
            LoRa2.FunLora_5_write16bytesArrayString(str(sensor[i]))
        
    #toc = clock()
    #print("processing time =",toc-tic)
#close
LoRa2.FunLora_close()

