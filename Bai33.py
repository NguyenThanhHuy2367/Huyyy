# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 14:25:44 2024

@author: NGUYEN THANH HUY
"""
import math
n=int(input("Nhập = "))
for i in range(1,n+1):
    can=math.sqrt(n)
if i == can**2:
        print("Chính Phương = ",can)
else:
        print("Không chính phương")