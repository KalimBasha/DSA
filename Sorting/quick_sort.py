'''
Approach:
1. This will be done using recursion and by using divide and conquer method.
2. will take a pivot element either first or last element(common).
3. keep the lesser elements to the pivot in the left and greater in right.
'''

from typing import List

def quick_sort(nums:List) -> List:
    if len(nums) <= 1:
        return nums

    pivot = nums[-1]
    left = [val for val in nums[:-1] if val < pivot]
    right = [val for val in nums[:-1] if val > pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)


print(quick_sort([4,6,2,5,7,9,1,3]))