"""
Separate 0s and 1s in an array
"""
def separate0and1(lst):
    start = 0
    end = len(lst) - 1
    
    #We will run this till start index is less than end index, 
    #stop when they cross
    while( start < end):
        #next 2 while loop are used to increment index, if the current
        #pointer is at 0 or 1, increment and decrement accordingly
        while((lst[start] == 0) & (start < end)):
            start += 1
        while((lst[end] == 1) & (end > start)):
            end -= 1
            
        #This condition assigns a value of 0 to a start index pointing at 1 and vice versa
        if (start < end):
            lst[start] = 0
            lst[end] = 1
            start += 1
            end -+ 1
    return lst

print(separate0and1([1,0,0,1,0,1,1,1,0,1]))