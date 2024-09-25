# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 20:06:56 2024

@author: NGUYEN THANH HUY
"""

a=int(input("Độ dài cạnh a = "))
b=int(input("Độ dài canh b = "))
c=int(input("Độ dài cạnh c = "))
if a+b>c or a+c>b or b+c>a and (a>0 and b>0 and c>0) :
    print("Là tam giác")
    if a == b == c and (a>0 and b>0 and c>0) :
        print("Tâm giác đều ")
    elif a**2 + b**2 == c**2 or b**2 + c**2 == a**2 or a**2 + c**2 == b**2 :
        print("Tam giác vuông ")
    elif a == b or b==c or c==a:
        print("Tam giác cân")
else: 
    print("Không phải là tam giác")
        