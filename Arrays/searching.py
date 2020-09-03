"""
This file contains implementation of linear and binary search
"""
#Linear Search - O(n)
def linear_search(lst, element):
    if len(lst) == 0:
        return 'Empty List'
    else:
        for i in lst:
            if i == element:
                return 'Element Found!!!'
        return 'Not Found!!!'
print(linear_search([1, 3, 5, 2, 6, 8], 2))

#Binary Search/half-interval search/lograthmic search- array/list needs to be sorted- O(logn)
def binary_search(lst, element):
    start = 0
    end = len(lst) - 1
    
    while start <= end:
        mid = (start + end) // 2
        if lst[mid] == element:
            return mid
        if lst[mid] < element:
            start = mid + 1
        else:
            end = mid -1 
    return -1
print(binary_search([1,2,3,5,6,8], 5))
