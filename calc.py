# -*- coding: utf-8 -*-
# tmp = int(input("请输入1-100之间的数字:"))
# if 1<tmp or tmp>100:
#     print("你大爷好丑")
# else:
#     print("你妹好漂亮")

tmp = input("请输入1-100之间的数字")
num = int(tmp)
try:

    if 1 <=num<=100:
        print('你好漂亮')
    else:
        print('你好丑')
except ValueError as e:
    print('你错了')