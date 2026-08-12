from typing import List


def conquer(l, left, right):
    lind, rind, mind = 0, 0, 0
    while lind < len(left) and rind < len(right):
        if left[lind] > right[rind]:
            l[mind] = right[rind]
            rind += 1
        else:
            l[mind] = left[lind]
            l += 1
        mind += 1
    while lind < len(left):
        l[mind] = left[lind]
        lind += 1
        mind += 1
    while rind < len(right):
        l[mind] = right[rind]
        mind += 1
        rind += 1


def divide(l):
    if len(l) > 1:
        mid = len(l)//2
        left = l[:mid]
        right = l[mid:]
        divide(left)
        divide(right)
        return conquer(l, left, right)

l = [5,4,3,2,1]
divide(l)
print(l)