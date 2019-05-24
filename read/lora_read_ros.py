import ifroglab
import RPi.GPIO as GPIO
import time
from std_msgs.msg  import Int64
import rospy
import os

LoRa = ifroglab.LoRa()

rospy.init_node('ap-Lib-5-lora-LoopRead.py') # 初始化 hello_python_node
rospy.loginfo('Hello World')         # 印出 Hello World

GPIO.setmode(GPIO.BCM)
GPIO.setup(23,GPIO.OUT)
GPIO.setup(24,GPIO.OUT)

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
while True:
  #讀取資料
  print("\n[8]:FunLora_6_read")
  data=LoRa.FunLora_6_readPureData()
  #print chr(data[0])
  print data[0]
  GPIO.output(23,0)
  GPIO.output(24,0)

  if data[0] == 97:
    #os.system('rostopic pub -1 /qq std_msgs/Int64 66')
    pub = rospy.Publisher('qq', Int64, queue_size = 10)
    rate = rospy.Rate(10)
    num = 666
    pub.publish(num)
    rate.sleep()

  if data[0] == 98:
   # os.system('rostopic pub -1 /qqq std_msgs/Int64 77')
    pub = rospy.Publisher('qq', Int64, queue_size = 10)
    rate = rospy.Rate(10)
    num = 777
    pub.publish(num)
    rate.sleep()

  if data[0] == 51:
    GPIO.output(23,1)

  if data[0] == 52:
    GPIO.output(24,1)

  #print ("len of data = ",len(data))
  if len(data) > 1:
    #print data[0:len(data)]
    for i in range (1,len(data)):
      print chr(data[i])

  time.sleep(1)


# 關閉
LoRa.FunLora_close()

