# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 21:15:31 2024

@author: NGUYEN THANH HUY
"""

n=int(input("Nhập N = "))
S=0
if n>0 :
    for i in range(1,n+1):
        S += 1/(2*i)
else:
    print("Nhập số nguyên dương ")
print("tổng = ", S)        

