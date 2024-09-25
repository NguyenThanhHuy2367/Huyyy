# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 15:34:17 2024

@author: NGUYEN THANH HUY
"""

n=int(input("Nhập n = " ))

while n<0:
    n=int(input("Nhập lại : "))
if n>0:
    s=0
for i in range(1,n+1):
    s += i**2
print(f"S = 1**2 + 2**2 + 3**2 + .... + { n**2 } = {s}")    