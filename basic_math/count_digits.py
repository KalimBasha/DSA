# 1. Count digits

'''
Example 1:
Input:N = 12345
Output:5
Explanation:  The number 12345 has 5 digits.
'''

n = int(input("Enter a number:"))
def count_digits(num:int) -> int:
    # method 1
    # return len(str(num))

    # method 2
    count = 0
    while num != 0:
        count+=1
        num //= 10
    return count

print(count_digits(n))