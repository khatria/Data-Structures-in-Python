"""
find the number occuring odd number of times in an array, given that exactly
one number occurs odd number of times
"""

def getOddOccurence1(lst):
    '''
    Using hash table
    '''
    count_dict = {}
    for ele in lst:
        if count_dict.get(ele) == None:
            count_dict[ele] = 1
        else:
            count_dict[ele] += 1
    return max(count_dict, key=count_dict.get)

print('The element occuring odd number of times is {}'.format(getOddOccurence1([3, 2, 1, 2, 3, 1, 1])))

def getOddOccurence2(lst):
    '''
    Using xor: If a number occurs even number of times and we apply XOR on it, we get result as zero and
    odd number of times then we get the number itself
    '''
    result = 0
    for element in lst:
        result = result ^ element
    return result

print('The element occuring odd number of times is {}'.format(getOddOccurence2([3, 2, 1, 2, 3, 1, 1])))