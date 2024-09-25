# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 15:55:41 2024

@author: NGUYEN THANH HUY
"""

N = int(input("Nhap so nguyen duong N: "))
while N <= 0:
    print("Số N phải là số nguyên dương.")
    N = int(input("Nhập lại : "))

print("Cac uoc so cua", N, "la:")
for i in range(1, N+1):
    if N % i == 0:
        print(i, end=" ")