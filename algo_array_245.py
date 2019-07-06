# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 21:03:54 2019

@author: Marco
"""

def shortest(words, word1, word2):
    h = collections.defaultdict(list)
    for i in range(len(words)):
        h[words[i]].append(i)
    dis = len(words)
          
    if word1 == word2:
        for i1 in h[word1]:
            for i2 in h[word2]:
                if i2 != i1:
                    dis = min(dis, abs(i1-i2))                
    else:        
        for i1 in h[word1]:
            for i2 in h[word2]:
                dis = min(dis, abs(i1-i2))
                
    return dis                



