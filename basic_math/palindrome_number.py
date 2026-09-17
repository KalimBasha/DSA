'''
Example 1:
Input:N = 4554
Output:Palindrome Number
Explanation: The reverse of 4554 is 4554 and therefore it is palindrome number
'''

def is_palindrome(n: int) -> bool:
    dummy = n
    power = len(str(n)) - 1
    res = 0
    while n != 0:
        rem = n % 10
        res = res + rem * (10 ** power)
        n //= 10
        power -= 1
    return res == dummy

def is_palindrome_2(n: int):
    rev_num = 0  # Initialize a variable to store the reverse of the number
    dup = n  # Create a duplicate variable to store the original number

    # Iterate through each digit of the number until it becomes 0
    while n > 0:
        ld = n % 10  # Extract the last digit of the number
        rev_num = (rev_num * 10) + ld  # Build the reverse number by appending the last digit
        n //= 10  # Remove the last digit from the original number

    # Check if the original number is equal to its reverse
    return dup == rev_num

print(is_palindrome(1331))
print(is_palindrome_2(123))