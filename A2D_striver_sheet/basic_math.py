# 1. Count digits

'''
Example 1:
Input:N = 12345
Output:5
Explanation:  The number 12345 has 5 digits.
'''

n = int(input("Enter a number:"))
def return_length(num:int) -> int:
    # method 1
    # return len(str(num))

    # method 2
    count = 0
    while num != 0:
        count+=1
        num //= 10
    return count


# 2. reverse a number
def reverse_number(n:int)->int:
    power = len(str(n))-1
    res = 0
    while n != 0:
        rem = n%10
        res = res + rem*(10**power)
        power-=1
        n//=10
    return res


# 3.

print(return_length(n))
print(reverse_number(n))