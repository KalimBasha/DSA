"""
*
**
***
****
*****
"""

n = int(input("Enter a number: "))

for i in range(1, n+1):
    print("*" * i)
    
for i in range(n,0,-1):
    print("*" * i)

for i in range(1,n+1):
    for j in range(i,n):
        print('', end=' ')
    print("*")

           