# reverse a number
def reverse_number(n:int)->int:
    power = len(str(n))-1
    res = 0
    while n != 0:
        rem = n%10
        res = res + rem*(10**power)
        power-=1
        n//=10
    return res

print(reverse_number(1234))