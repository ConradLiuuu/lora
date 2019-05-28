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
 

LoRa = ifroglab.LoRa()


# 打開Port
print("Open Port, FunLora_init()")
ser=LoRa.FunLora_initByName("/dev/ttyACM0")

#讀取F/W版本及Chip ID
print("Get Firmware Version, FunLora_0_GetChipID()")
LoRa.FunLora_0_GetChipID()
# 重置 & 初始化
print("Init, FunLora_1_Init()")
LoRa.FunLora_1_Init()
# 讀取設定狀態
print("\n[4]:FunLora_2_ReadSetup");
LoRa.FunLora_2_ReadSetup();

# 設定讀取和頻段
# print("\n[7]:FunLora_3_RX")
LoRa.FunLora_3_RX();

LoRa.debug=False
counter=0
lastData=[]
tic = time.clock()
for i in range(200):
  #tic = time.clock()
  #讀取資料
  print("\n[8]:FunLora_6_read")
  data=LoRa.FunLora_6_readPureData()
  
  #print(data)
  str_data = []
  if len(data) != 0:
    #print(chr(data[0]))
    
    #print((data))
    for i in data:
      if i >= 45 and i <= 57:
        str_data.append(chr(i))
    #print(str_data)
    str_data2 = "".join(str_data) ## list -> str

    print(float(str_data2))
    #print "-------"
    
toc = time.clock()
print("processing time =",toc-tic)    
  

# 關閉
LoRa.FunLora_close() 


