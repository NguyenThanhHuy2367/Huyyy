# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 17:19:09 2024

@author: NGUYEN THANH HUY
"""

s=0 
n=int(input("Nhập n = "))
while n <=0:
    n=int(input("Nhập lại "))
for i in range(1,n+1):  
    s += (2*i+1)/(2*i+2)
print(round(s,2)) 