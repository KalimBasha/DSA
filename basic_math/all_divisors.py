'''
Input: N = 36
Output: [1, 2, 3, 4, 6, 9, 12, 18, 36]  
Explanation: The divisors of 36 are 1, 2, 3, 4, 6, 9, 12, 18, 36.

Input: N = 12
Output: [1, 2, 3, 4, 6, 12]
Explanation: The divisors of 12 are 1, 2, 3, 4, 6, 12.
'''

def return_all_divisors(n:int)->list[int]:
    return [i for i in range(1,n+1) if n % i == 0]

def return_all_divisors_2(n: int)->list[int]:
    l = []
    for i in range(1, (n//2)+1):
        if n % i == 0:
            l.append(i)
    l.append(n)
    return l

print(return_all_divisors(36))
print(return_all_divisors(12))