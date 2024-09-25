# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 16:59:22 2024

@author: NGUYEN THANH HUY
"""
ts=1
ms=0
s=0
n=int(input("Nhập n = "))
while n<=0:
    n=int(input("Nhập n= "))
x=float(input("Nhập X : "))
    #x^n = x**n = ts = 1
    # 1+2+3+..+n = ms = 0
for i in range(1,n+1):

        ts=x**i
        ms= ms + i
        s += ts/ms
print(round(s,2))