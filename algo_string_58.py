# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 23:43:30 2019

@author: Marco
"""

def lengthOfLastWord(s):
    if len(s.split()) == 0:
        return 0
    else:
        return len(s.split()[-1])