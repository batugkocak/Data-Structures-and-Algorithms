import timeit

# F(0) = 0, F(1) = 1
# F(N) = F(N- 1) + F(N -2), for n > 1

# F(2) = F(1) + F(0) = 1 + 0 = 1

# F(4) = F(3) + F(2) = 2 + 1 = 3


# Solution 1 - Recursive


def recursiveFibonacci(num: int):
    if num == 0:
        return 0
    if num == 1:
        return 1
    else:
        return recursiveFibonacci(num - 1) + recursiveFibonacci(num - 2)


# Solution 2 - Iteration

def iterativeFibonacci(num: int):
    x, y = 0, 1
    result = 0
    for i in range(num):
        #x, y = y, x + y # OR: 
        x = y
        y= result
        result = x +y
        

    return result
print(recursiveFibonacci(10))

print(iterativeFibonacci(10))