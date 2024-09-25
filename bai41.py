# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 14:40:06 2024

@author: NGUYEN THANH HUY
"""
n=int(input("Nhập n = "))
s = 0
for i in range(1,n+1):
  s += 1 / (2*i + 1)

print("Tổng của dãy số là:", s)