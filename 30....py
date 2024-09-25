# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 13:16:36 2024

@author: NGUYEN THANH HUY
"""

a = float(input("Nhập tháng: "))
b = float(input("Nhập năm: "))
# Kiểm tra tháng
if 1<=a<=12:
    print("Đây là một tháng trong năm.")
    if a in [1, 3, 5, 7, 8, 10, 12]:
        print("Tháng có 31 ngày.")
    elif a == 2 and b % 4 == 0 and (b % 100 != 0 or b % 400 == 0):
        print("Tháng có 29 ngày.")
    elif a == 2:
        print("Tháng có 28 ngày.")
    else:
        print("Tháng có 30 ngày.")
else:
    print("Tháng không hợp lệ. Vui lòng nhập từ 1 đến 12.")   
# Kiểm tra năm nhuận 
if b % 4 == 0 and (b % 100 != 0 or b % 400 == 0):
    print("Năm nhuận.")
else:
    print("Không phải năm nhận.")