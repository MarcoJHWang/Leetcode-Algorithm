# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 12:15:41 2019

@author: Marco
"""

""" 274 H-index """
""" 81% """

def hIndex(citations):
    # O(N*logN)
    if len(citations) == 0:
        return 0
    
    citations.sort(reverse=True)
    N = len(citations)        
    h = 0
    for i in range(N):
        if citations[i] <= i:
            h = i-1
            break
        h = i
    
    return h+1

