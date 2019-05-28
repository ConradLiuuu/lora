import os

while True:
    print("RX mode")
    os.system('python receive.py')
    print("Tx mode")
    os.system('python send.py')
