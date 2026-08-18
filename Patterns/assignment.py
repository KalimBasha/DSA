'''
1.
1 * 2 * 3 
* 4 * 5 * 
6 * 7 * 8 
* 9 * 1 * 
2 * 3 * 4

2.
11111
*****
22222
*****
33333
'''


# solutions
n = 5
k = 1

# for i in range(n):
#     for j in range(1,n+1):
#         if i %2 == 0:
#             if j % 2 != 0:
#                 print(k, end=' ')
#                 if k < 9:
#                     k += 1
#                 else:
#                     k = 1
#             else:
#                 print("*", end=' ')
#         else:
#             if j % 2 != 0:
#                 print("*", end=' ')
#             else:
#                 print(k, end=' ')
#                 if k < 9:
#                     k += 1
#                 else:
#                     k = 1
#     print()



# for i in range(n):
#     for j in range(n):
#         if i%2 != 0:
#             print("*", end=' ')
#             if j == n-1:
#                 k += 1
#         else:
#             print(k, end=' ')
#     print()


# optimized solutions

# problem 1

for i in range(n):
    for j in range(n):
        if (i % 2 == 0 and j % 2 == 0) or (j % 2 != 0 and i % 2 != 0):
                print(k, end=' ')
                if k < 9:
                    k += 1
                else:
                    k = 1
        else:
            print("*", end=' ')
    print()


# problem 2
# for i in range(n):
#     for j in range(n):
#         if i%2 != 0:
#             print("*", end=' ')
#         else:
#             print((i//2)+1, end=' ')
#     print()