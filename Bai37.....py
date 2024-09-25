# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 16:03:58 2024

@author: NGUYEN THANH HUY
"""

n=int(input("Nhập n = "))
while n<0 or n %2 != 0:
    n=int(input("Nhập n = "))
if n>0:
    s=0
    for i in range(2,n+1,2):
        s += i 
print(f" 2 + 4  +... + {n} = {s} ")
