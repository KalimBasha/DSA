'''
Example 1:
Input:N = 153
Output:True
Explanation: 1^3+5^3+3^3 = 1 + 125 + 27 = 153
'''

def is_armstrong(n:int)->bool:
    res = 0
    dummy = n
    while n != 0:
        rem = n % 10
        res += rem**(len(str(dummy)))
        n //= 10 

    return dummy == res

print(is_armstrong(153))
print(is_armstrong(12))