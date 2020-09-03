# -*- coding: utf-8 -*-
"""
Given an array A and a number x, find a pair(a, b) in A st a+b = x
"""
def find_pair(lst, x):
    dict_elem = {}
    for a in lst:
        b = x - a
        if dict_elem.get(b) != None:
            print('One such pair is ({}, {})'.format(a,b))
        dict_elem[a] = 0
        
find_pair([0, 1, 2, 10, 6, 9, 11, 5, 3], 9)
