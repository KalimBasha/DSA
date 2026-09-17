'''
Example 1:
Input: N1 = 9, N2 = 12

Output: 3
Explanation:
Factors of 9: 1, 3, 9
Factors of 12: 1, 2, 3, 4, 6, 12
Common Factors: 1, 3
Greatest common factor: 3 (GCD)
'''

def gcd(n1: int, n2: int) -> int:
    gcd_val = 1
    for i in range(1, (min(n1,n2)//2)+1):
        if n1 % i == 0 and n2 % i == 0:
            gcd_val = i
        
    return gcd_val

def gcd_2(n1: int, n2: int) -> int:
    for i in range((min(n1,n2)//2), 0, -1):
        if n1 % i == 0 and n2 % i == 0:
            return i

print(gcd(9, 12))
print(gcd(20, 15))
print(gcd_2(15,20))