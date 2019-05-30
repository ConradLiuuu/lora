# www.ifroglab.com
# -*- coding: utf8 -*-
# coding=UTF-8
# * iFrogLab IL-LORA1272  www.ifroglab.com
# *
# * 功能,             USB to TTL , IFROGLAB LORA
# * 電源VDD,          3.3V       ,Pin 3
# * 接地GND,          GND        ,Pin 1
# * 接收反應Host_IRQ,  null       , Pin 2
# * UART,             RX         ,UART_RX  Pin 7
# * UART,             TX         ,UART_TX  Pin 8


import ifroglab
import time
import serial





#######
LoRa2 = ifroglab.LoRa()





# 打開Port
print("Open Port, FunLora_init()")
ser=LoRa2.FunLora_initByName("/dev/ttyACM0")


#讀取F/W版本及Chip ID
print("Get Firmware Version, FunLora_0_GetChipID()")
LoRa2.FunLora_0_GetChipID()



# 重置 & 初始化
print("Init, FunLora_1_Init()")
LoRa2.FunLora_1_Init()

# 讀取設定狀態
print("\n[4]:FunLora_2_ReadSetup");
LoRa2.FunLora_2_ReadSetup();

cmd=input("Send cmd is :")

LoRa2.FunLora_3_TX();
LoRa2.FunLora_5_write16bytesArrayString(str(cmd));
print(cmd)

# 關閉
LoRa2.FunLora_close()




