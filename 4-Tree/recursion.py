def calculateFactorial(num):
    if num == 0:
        return 1
    else:
        return num * calculateFactorial(num - 1)


print(calculateFactorial(0))


def calculateContagiousSum(num):
    if num == 0:
        return 0
    else:
        return num + calculateContagiousSum(num - 1)


print(calculateContagiousSum(5))
