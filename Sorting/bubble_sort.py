'''
Approach:

1. Use two loops one for iterating and one to compare ewith each other.
2. First sort the max in this bubble sort means the last index has to be sorted first.
3. so run the loops from last to first with len(list) to 0th index.
4. In the inner loop, compare the current element with next element if current element is greater than next swap the elements.
5. swap elements if condition satisfies also till the iteration is done.
6. atlast return the sorted list.
'''

from typing import List

def bubble_sort(l: List) -> List:
    for i in range(len(l)-1, -1, -1):
        for j in range(i):
            if l[j] > l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]
    return l

print(bubble_sort([123,9,45,3,0,27]))