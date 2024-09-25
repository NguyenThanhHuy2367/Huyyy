# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 21:04:03 2024

@author: NGUYEN THANH HUY
"""

n=int(input("Nhập số nguyên dương = " ))
while n<=0 or n %2 ==0:
    n=int(input("Nhập lại = "))
if n > 0 :
    S=1
    for i in range(1,n+1): # từ 1 đến bước nhảy n ( nhảy 2 )
        S *= i
    print(f"Tổng 1*2*3*....*{n} = {S}")