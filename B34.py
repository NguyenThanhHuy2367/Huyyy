# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 14:52:46 2024

@author: NGUYEN THANH HUY
"""

n = int(input("Nh n: "))
while n<=0:
    n = int(input("Nhập lại n "))
if n<2:
    print("Không phải là số nguyên tố")
else:
    for i in range(2,n+1):
        if n%i==0:
            print("Không phải là số nguyên tố")
            break
        else:
            print("Là số nguyên tố") 
            break