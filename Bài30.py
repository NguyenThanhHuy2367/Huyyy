# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 19:45:42 2024

@author: NGUYEN THANH HUY
"""
thang = int(input("Nhập tháng : "))
        
nam = int(input("Nhập năm : "))
if thang < 1 or thang > 12:

    print("Tháng không hợp lệ. Vui lòng nhập lại.")
nam_nhuan = False
if nam % 4 == 0 and (nam % 100 != 0 or nam % 400 == 0):
    nam_nhuan = True


if thang in [1, 3, 5, 7, 8, 10, 12]:
            so_ngay = 31
elif thang == 2:
            if nam_nhuan:
                so_ngay = 29
else:
            so_ngay = 28
if thang in [4,6,9,11]:
            so_ngay = 30
print(f"Tháng {thang} năm {nam} có {so_ngay} ngày.")
print("năm nhuận",nam_nhuan)
