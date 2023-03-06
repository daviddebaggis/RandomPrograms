# -*- coding: utf-8 -*-
"""
Created on Thu Feb  9 11:15:45 2023

@author: ddebaggis
"""

s = "azcbobobegghakl"
sv2 = ''
sv3 = ''
for i in range(len(s)-1):
    if s[i] <= s[i+1]:
        sv2 = s[i] + s[i+1]
        print(sv2)
        