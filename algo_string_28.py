# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 23:36:18 2019

@author: Marco
"""

def strStr(haystack, needle):
    if needle == '':
        return 0
    elif haystack == '' and needle != '':
        return -1
    elif needle not in haystack:
        return -1
    else:
        for i in range(len(haystack)):
            idx = 0
            while haystack[i] == needle[idx] and idx < len(needle):
                i += 1
                idx += 1                
                if idx == len(needle):
                    break
            if idx == len(needle):
                break            
        return i - idx