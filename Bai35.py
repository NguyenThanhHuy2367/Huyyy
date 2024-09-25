# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 14:32:11 2024

@author: NGUYEN THANH HUY
"""
 

n = int(input("Nhập số nguyên dương n: "))
S = 0
if n>0:
    for i in range(1, n+1):
        S += i
    print(f"Tổng S = 1 + 2 + ... + {n} là : {S}")
