# -*- coding: utf-8 -*-
"""
Created on Sat Sep  3 14:10:16 2022

@author: HP
"""

def numberOfSteps(self, num):

        n = 0
        while num != 0:
            if num % 2 == 0: 
                num = num / 2 
            else: 
                num = num - 1
            n = n + 1
        return n