# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 18:17:13 2019

@author: Marco
"""

Input: "the sky is blue"
Output: "blue is sky the"

Input: "  hello world!  "
Output: "world! hello"

Input: "a good example"
Output: "example good a"


def reverseWords(s):
    #list(reversed(s.split()))
    return ' '.join(list(reversed(s.split())))
    
    
    



s = "the sky is blue"  
s = "a good example" 
reverseWords(s)