# -*- coding: utf-8 -*-
import random

times = 3
secret = random.randint(1,10)
#tmp = int(input("请输入一个数字"))
tmp = 0
while (tmp != secret) and (times > 0):
    tmp = int(input("请输入一个数字"))
    times -=1
    if tmp == secret:
        print("卧槽，猜对了")
    else:
        if tmp > secret:
            print("大了")
        else:
            print("小了")
        if times > 0 :
            print("再试一次: ",end="")
        else:
            print("机会用光了")
print("游戏结束")