# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 23:39:15 2019

@author: Marco
"""

def longestCommonPrefix(strs):
    length = 1000
    for word in strs:
        if len(word) < length:
            length = len(word)
    
    idx = -1
    for pos in range(length):
        counter = 0
        for j in range(1, len(strs)):        
            if strs[j-1][pos] == strs[j][pos]:
                counter += 1
                
        if counter == len(strs)-1:
            idx = pos      
        elif counter != len(strs)-1:
            break
    
    if idx >= 0:
        return strs[0][0:idx+1]
    else:
        return ''