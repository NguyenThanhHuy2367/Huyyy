# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 21:12:31 2024

@author: NGUYEN THANH HUY
"""

n=int(input("Nhập N = "))
while n<0:
    n=int(input("Nhập N = "))
if n >0 :
    S=0
    for i in range(1,n+1):
        S += 1/i
print(f"1 + 1/2 + 1/3 + .... + 1/{n} = {S} ")       