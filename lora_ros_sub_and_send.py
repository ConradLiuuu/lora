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
from  time import sleep
import rospy
from std_msgs.msg import Int8
import os

LoRa =  ifroglab.LoRa()
os.system('sudo chmod a+rw /dev/ttyACM0')

rospy.init_node('lora_ros_sub')
value = 0

# LoRa setup
ser=LoRa.FunLora_initByName("/dev/ttyUSB0")
LoRa.FunLora_0_GetChipID()
LoRa.FunLora_1_Init()
LoRa.FunLora_2_ReadSetup()
LoRa.FunLora_3_TX()
print("LoRa Ready!!!")

def callback(data):
    value = data.data
    LoRa.FunLora_5_write16bytesArrayString(str(value))

def listener():
    rospy.init_node('lora_ros_sub')
    rospy.Subscriber("/SensorData", Int8, callback)
    rospy.spin()

while not rospy.is_shutdown():
    listener()
    rospy.spin()

