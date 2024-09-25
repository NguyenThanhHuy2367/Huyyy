# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 16:46:31 2024

@author: NGUYEN THANH HUY
"""

a=[]
for x in range(1, 490):
    for y in range(1,140):
        for z in range(1,109):
            if 2*x + 7*y + 9*z == 979:
                a +=[(x,y,z)]
print(a)