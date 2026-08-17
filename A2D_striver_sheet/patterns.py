# 1. 5*5 star pattern
# n = int(input("Enter a number:"))
# for i in range(n):
#     for j in range(n):
#         print("*", end='')
#     print()


# 2. as per star pattern
# n = int(input("Enter a number:"))
# for i in range(1, n+1):
#     print("*"*i)


# 3. number pattern
# n = int(input("Enter a number:"))
# for i in range(1, n+1):
#     for j in range(1, i+1):
#         print(j, end='')
#     print()


# 4. number pattern printing each number in each line
# n = int(input("Enter a number:"))
# for i in range(1, n+1):
#     for j in range(1, i+1):
#         print(i, end='')
#     print()


# 5. inverted star pattern
# n = int(input("Enter a number:"))
# for i in range(n,0,-1):
#     print("*"*i)


# 6. inverted number pattern
# n = int(input("Enter a number:"))
# for i in range(n,0,-1):
#     for j in range(1,i+1):
#         print(j, end='')
#     print()


# 7. triangle pattern
# n = int(input("Enter a number:"))
# spaces = n-1
# for i in range(1,(n*2)+1,2):
#     for sp in range(spaces):
#         print(" ",end=' ')
#     for st in range(i):
#         print("*",end=' ')
#     print()
#     spaces -= 1


# 8. inverted triangle pattern
# n = int(input("Enter a number:"))
# spaces = 0
# for i in range((n*2)+1,0,-2):
#     for sp in range(spaces):
#         print(" ",end=' ')
#     for st in range(i):
#         print("*",end=' ')
#     print()
#     spaces += 1


# 9. diamond pattern
# n = int(input("Enter a number:"))
# spaces = n-1
# stars = 1
# for i in range(1,(n*2)+1):
#     for sp in range(spaces):
#         print(" ",end=' ')
#     for st in range(stars):
#         print("*",end=' ')
#     print()
#     if i < ((n*2)+1)//2:
#         spaces -= 1
#         stars += 2
#     else:
#         spaces += 1
#         stars -= 2


# 10. half diamond pattern
# n = int(input("Enter a number:"))
# stars = 1
# for i in range(1,(n*2)+1):
#     for st in range(stars):
#         print("*",end=' ')
#     print()
#     if i < ((n*2)+1)//2:
#         stars += 1
#     else:
#         stars -= 1


# 11. 0s and 1s pattern
# n = int(input("Enter a number:"))
# for i in range(n):
#     if i%2 == 0:
#         stars = 1
#     else:
#         stars = 0
#     for j in range(i+1):
#         print(stars,end='')
#         stars = 1 - stars
#     print()
    

# 12. number with space pattern
# n = int(input("Enter a number:"))
# spaces = 2*(n-1)
# for i in range(1,n+1):
#     for num1 in range(1,i+1):
#         print(num1,end='')
#     for j in range(spaces):
#         print(' ',end='')
#     for num2 in range(i,0,-1):
#         print(num2,end='')
#     spaces -= 2
#     print()


# 13. increment number pattern
# n = int(input("Enter a number:"))
# k = 1
# for i in range(n):
#     for j in range(i+1):
#         print(k, end=' ')
#         k+=1
#     print()


# 14. Alphabet series
# n = int(input("Enter a number:"))
# for i in range(n):
#     alpha = ord('A')
#     for j in range(i+1):
#         print(chr(alpha),end=' ')
#         alpha += 1
#     print()


# 15. Inverted alphabet series
# n = int(input("Enter a number:"))
# for i in range(n,0,-1):
#     alpha = ord('A')
#     for j in range(i):
#         print(chr(alpha),end=' ')
#         alpha += 1
#     print()


# 16. Same row alphabet series
# n = int(input("Enter a number:"))
# alpha = ord('A')
# for i in range(n):
#     for j in range(i+1):
#         print(chr(alpha),end=' ')
#     alpha += 1
#     print()


# 17. Alphabet series with space
n = int(input("Enter a number:"))
spaces = (n*2)-2
for i in range(1,n*2,2):
    alpha = ord('A')
    for sp in range(spaces):
        print(' ',end='')
    for j in range(i):
        print(chr(alpha),end=' ')
        if j < i//2:
            alpha += 1
        else:
            alpha -= 1
    spaces -= 2
    print()


# 18.  inverted alphabet series
n = int(input("Enter a number:"))
for i in range(1,n+1):
    alpha = ord('A')
    for j in range(i,0,-1):
        print(chr(alpha+n-j),end=' ')
    print()


# 19. hollow centre diamond
n = int(input("Enter a number:"))
