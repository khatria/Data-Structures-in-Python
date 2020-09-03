# -*- coding: utf-8 -*-
"""
Find the maximum distance between 2 elements in an array st larger element 
appears after the smaller number
"""
def max_diff(lst):
    '''
    This function maintains track of min element and max diff, using which
    it finds the distance between 2 elements in the arrat
    Time - O(n)
    Space - O(1)
    '''
    min_so_far = lst[0]
    max_diff = 0
    for i in range(1, len(lst)):
        if lst[i] < min_so_far:
            min_so_far = lst[i]
        else:
            if (lst[i] - min_so_far) > max_diff:
                max_diff = lst[i] - min_so_far
    return max_diff

print('The max difference is {}'.format(max_diff([4, 3, 10, 2, 9, 1, 6])))


