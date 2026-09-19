'''
Input: N = 3
Output: Ashish Ashish Ashish 
Explanation: Name is printed 3 times.

Input: N = 1
Output: Ashish 
Explanation: Name is printed once.
'''

def print_name(val:str,n:int)->str:
    if n == 1:
        return val
    return val + ' ' + print_name(val, n-1)

# print(print_name("kalim", 4))


'''
Input: N = 4
Output: 1, 2, 3, 4
Explanation: All the numbers from 1 to 4 are printed.

Input: N = 1
Output: 1 
Explanation: This is the base case.
'''

def print_numbers(n:int,i:int)->int:
    if i == n:
        return i
    print(i, end=',')
    return print_numbers(n,i+1)

# print(print_numbers(10,1))


'''
Input: N = 4
Output: 4, 3, 2, 1
Explanation: All the numbers from 4 to 1 are printed.

Input: N = 1
Output: 1 
Explanation: This is the base case.
'''

def print_rev_numbers(n:int, i:int)->int:
    if i == n+1:
        return i
    print(i, end=',')
    return print_rev_numbers(n, i-1)

print(print_rev_numbers(0,10))


'''
Input: N=5
Output: 15
Explanation: 1+2+3+4+5=15.

Input: N=6
Output: 21
Explanation: 1+2+3+4+5+6=15.
'''

def print_sum(n:int)->int:
    if n == 0:
        return n
    return n + print_sum(n-1)

print(print_sum(6))


'''
Input:
 X = 5
Output:
 120
Explanation:
 5! = 5*4*3*2*1
'''

def factorial(n:int)->int:
    if n == 0:
        return 1
    return n * factorial(n-1)

print(factorial(3))


'''
Input: N = 5, arr[] = {5,4,3,2,1}
Output: {1,2,3,4,5}
Explanation: Since the order of elements gets reversed the first element will occupy the fifth position, the second element occupies the fourth position and so on.

Input: N=6 arr[] = {10,20,30,40}
Output: {40,30,20,10}
Explanation: Since the order of elements gets reversed the first element will occupy the fifth position, the second element occupies the fourth position and so on.
'''

def rev_array(l:list)->list:
    if l == []:
        return []
    return [l.pop()] + rev_array(l)

print(rev_array([5,4,3,2,1]))
print(rev_array([10,20,30,40]))


'''
Example 1:
Input: Str =  “ABCDCBA”
Output: Palindrome
Explanation: String when reversed is the same as string.

Example 2:
Input: Str = “TAKE U FORWARD”
Output: Not Palindrome
Explanation: String when reversed is not the same as string.
'''

def is_palindrome(s:str, i:int)->bool:
    if i >= len(s)//2:
        return True
    if s[i] != s[len(s)-i-1]:
        return False
    return is_palindrome(s, i+1)

print(is_palindrome('ABCDCBA', 0))
print(is_palindrome("kalim", 0))


'''
Example 1:
Input: N = 5
Output: 0 1 1 2 3 5
Explanation: 0 1 1 2 3 5 is the fibonacci series up to 5th term.(0 based indexing)

Example 2:
Input: 6
Output: 0 1 1 2 3 5 8
Explanation: 0 1 1 2 3 5 8 is the fibonacci series upto 6th term.(o based indexing)
'''

def fibonacci(n:int)->int:
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

for i in range(10):
    print(fibonacci(i), end=' ')