# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 20:19:34 2024

@author: NGUYEN THANH HUY
"""

a=float(input("Nhập quãng đường đã đi (km) = "))
if a<1 :
    print("Số tiền là : ",1*15000)
if  1< a <= 5 :
    print("Số tiền phải trả là : ", 15000 + (a-1)*13500)
elif a >5 : 
    print("Số tiền phải trả là : ", 15000+(4*13500)+(a-5)*11000)
t=15000+(4*13500)+(a-5)*11000
if a > 120:
  print("Số tiền sau giảm 8% = ", t*0.9)
else :
    print("Không hợp lệ")