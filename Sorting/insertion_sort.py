'''
Approach:
1. run a for loop for iterating from 1 to number of values in list or array.
2. Take a key and initilaise an element to compare.
3. take an index to check the index value is greater than key or not, if then assign the next index with current value.
4. Iterate till it gets inserted at correct position.
5. Then assign the next element with key value.
6. Iterate until the list or array gets sorted.
'''

from typing import List

def insertion_sort(l: List) -> List:
    for i in range(1, len(l)):

        key = l[i]
        j = i-1

        while j >=0 and l[j] > key:
            l[j+1] = l[j]
            print(l,"1st step")
            j -= 1
        print(j+1,"j value")
        l[j+1] = key
        print(l,"2nd step")

    return l


print(insertion_sort([5,4,3,2,1]))