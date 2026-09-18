'''
Example 1:
Input:N = 2    
Output:True                
Explanation: 2 is a prime number because it has two divisors: 1 and 2 (the number itself).
             
Example 2:
Input:N =10                   
Output: False
Explanation: 10 is not prime, it is a composite number because it has 4 divisors: 1, 2, 5 and 10. 
'''

def is_prime(n:int)->bool:
    if n == 2:
       return True
    for i in range(2, (n//2)+1):
        if n % i == 0:
            return False
    return True

print(is_prime(2))
print(is_prime(14))