import sys

def getkey():
    key = sys.stdin.read(1)
    #key = input()
    return key

cnt = 0
while True:
    print("one")
    key2 = getkey()
    #print key2
    if key2 == 'w':
        cnt = cnt + 1
    print("cnt = ")
    print(cnt)
