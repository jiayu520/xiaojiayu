# -*- coding: utf-8 -*-
tmp = input("请输入一个年份")
tmp = int(tmp)
if (tmp % 4 == 0) and (tmp % 100 != 0):
    print("%d 是一个闰年" % tmp)
elif tmp % 400 == 0:
    print("%d 这是一闰年" % tmp)
else:
    print("%d 这是一个平年" % tmp)
