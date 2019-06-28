# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 11:49:06 2019

@author: Marco
"""

""" 243. Shortest Word Distance """
""" 78% """
#words = ["practice", "makes", "perfect", "coding", "makes"]
#word1 = 'coding'
#word2 = 'practice'
#shortestDistance(words, word1, word2) 

def shortestDistance(words, word1, word2):
    w1_idx, w2_idx = [], []

    for (idx, word) in enumerate(words):
        if word == word1: 
            w1_idx.append(idx)
        elif word == word2:
            w2_idx.append(idx)
            
    m = len(words)
    for i in range(len(w1_idx)):
        for j in range(len(w2_idx)):
            m = min(m, abs(w1_idx[i] - w2_idx[j]))

    return m            

   
