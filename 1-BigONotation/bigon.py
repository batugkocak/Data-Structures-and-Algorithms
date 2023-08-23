def bigon(n):
    complex= 0
    for i in range(0,n):
        complex = complex + 1
    print(complex)

print()
print('Big O Notation O(N)')
print('-------------------')
bigon(16)
print()


print('Big O Notation O(N^2)')
print('---------------------')

def bigon2(n):
    complex = 0
    for i in range(0,n):
        for j in range(0,n):
            complex = complex + 1
    print(complex)
    

bigon2(16)

#Big O Notation O(N^3) has 3 loops 


print()
print('Big O Notation O(log N)')
print('-----------------------')

import math

math.floor(5/2) 

def logn(n):
    complex= 0
    while n> 1:
        n= math.floor(n/2)
        complex = complex +1
    print(complex)

logn(16)

print()
print('Big O Notation O(N log N)')
print('-----------------------')

def nlogn(n):
    lim = n
    complex = 0
    while n> 1:
        n = math.floor(n/2)
        for i in range (1, lim):
            complex = complex +1
    print(complex)

nlogn(16)

print()
print('Big O Notation O(N!)')
print('-----------------------')

def nfactorial(n):
    if n == 0:
        print("1")
        return
    else:
        for i in range(0,n):
            print(i)
            nfactorial(n - 1)

nfactorial(4)

print()
print('Actual Factorial')
print('-----------------------')

#Do not confuse actual factorial and O(n!). Actual factorials time complexity is actually O(N)

def actualfactorial(n): # O(N)
    if (n == 1 or n ==0):
        return 1
    else:
        return(n * actualfactorial(n-1))
    
print(actualfactorial(4))
print()