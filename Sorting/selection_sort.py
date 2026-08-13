'''
Approach:
1. Need two loops for iterating and comparing with each one.
2.When first loop iterates we can fix a min index.
3. In the second loop iterates from the i+1 elements.
4. compare the values of min index with inner loop values.
5. If min index is lesses keep as it is else fix the min index as lesser value's index.
6. Once inner loop completes, swap the values with the indices of i-th position with min index position.
7. Atlast return the sorted list.
'''

from typing import List

def selection_sort(l:List) -> List:
    for i in range(len(l)):
        minimum_index = i
        for j in range(i+1,len(l)):
            if l[j] < l[minimum_index]:
                minimum_index = j
        l[i],l[minimum_index] = l[minimum_index],l[i]
    return l

print(selection_sort([12,34,11,5,2]))