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
"""
範例3:
確認，二個LoRa 可以連續大量的　送　和　收資料
ap-Lib-5-lora-LoopRead.py
ap-Lib-5-lora-LoopWrite.py
"""
import ifroglab
import RPi.GPIO as GPIO
import time
import os

LoRa = ifroglab.LoRa()

GPIO.setmode(GPIO.BCM)
GPIO.setup(23,GPIO.OUT)
GPIO.setup(24,GPIO.OUT)
GPIO.setup(18,GPIO.IN)

# 打開Port
print("Open Port, FunLora_init()")
ser=LoRa.FunLora_initByName("/dev/ttyUSB0")

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
print("\n[7]:FunLora_3_RX")
LoRa.FunLora_3_RX();

LoRa.debug=False

GPIO.output(23,0)
GPIO.output(24,0)

while True:
    ## Read data
    pin2 = GPIO.input(18)
    #print("pin2 = ",pin2)
    #print("\n[8]:FunLora_6_read")
  
    if pin2 == 1: ## Read new data
        #print("pin2 HIGH")
        data=LoRa.FunLora_6_readPureData()
        #time.sleep(0.2)
        print("Received data , ascii code =",data)

        if data[0] == 51: ## num3
          GPIO.output(23,1)
          GPIO.output(24,0)
        elif data[0] == 52:  ##num4
          GPIO.output(23,0)
          GPIO.output(24,1)
        else: ##others nums
          GPIO.output(23,0)
          GPIO.output(24,0)

# 關閉
LoRa.FunLora_close() 


