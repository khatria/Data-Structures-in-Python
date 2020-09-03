"""
Given a sorted array of size n, find an element that occurs more than n/2 times
"""
def getMajorityElement(lst):
    majority_index = 0
    vote = 1
    for index in range(1, len(lst)):
        if lst[majority_index] == lst[index]:
            vote += 1
        else:
            vote -= 1
        if vote == 0:
            majority_index = index
            vote = 1
    return lst[majority_index]

def isMajority_element(lst):
    element = getMajorityElement(lst)
    count = 0
    for index in range(len(lst)):
        if lst[index] == element:
            count += 1
    if count > len(lst)/2:
        return '{} is the majority element'.format(element)
    else:
        return 'No majority element'

print(isMajority_element([2, 2, 5, 6, 2, 2]))
print(isMajority_element([1, 2, 3, 4, 5, 5]))
