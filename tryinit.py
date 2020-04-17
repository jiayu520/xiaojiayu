# -*- coding: utf-8 -*-
class Try_int(int):
    def __add__(self, other):
        return self + other
a = Try_int(3)
b = Try_int(5)
a+b