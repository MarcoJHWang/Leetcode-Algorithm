# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 20:57:37 2019

@author: Marco
"""

""" 244. Shortest Word Distance II """
class WordDistance:

    def __init__(self, words: List[str]):
        self.h = collections.defaultdict(list)
        for i in range(len(words)):
            self.h[words[i]].append(i)
    
    def shortest(self, word1: str, word2: str) -> int:        
        dis = 100000
        for i1 in self.h[word1]:
            for i2 in self.h[word2]:
                dis = min(dis, abs(i1-i2))
    
        return dis 