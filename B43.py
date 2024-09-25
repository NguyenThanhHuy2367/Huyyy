# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 14:51:08 2024

@author: NGUYEN THANH HUY
"""

n = int(input("Nhập n ="))  
s = 0

for i in range(1, n+1):
  s += i / (i+1)

print("Tổng của dãy số là:", s)