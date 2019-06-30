# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 13:25:39 2019

@author: Marco
"""
""" 302 """

def minArea(image):
    rows, columns = len(image), len(image[0])
    length, Left, Right = [], columns, 0
    
    for i in range(rows):                                  
        if image[i].count('1'):
            length.append(i)
            Left = min(Left, image[i].index('1'))
            Right = max(Right, columns - image[i][::-1].index('1') - 1)
                      
