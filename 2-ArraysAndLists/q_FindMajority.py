myList = [2, 3, 4, 1, 1, 1, 1, 1, 5, 5, 5]
mySecondList = [2, 2, 1, 1, 1, 2, 2]


# METHOD 1

# Time: O(n)
# Space: (On)

def findMajority(myList):
    numbers = {}  # Dictionary, HashMap, Map - (Key-Value)
    result = 0
    maxNumber = 0

    for num in myList:
        numbers[num] = 1 + numbers.get(num, 0)  # This will get the numbers value and add 1 to it
        # If the element is not on the map, add it as 1
        if numbers[num] > maxNumber:
            result = num
        maxNumber = max(maxNumber, numbers[num])
    return result


# numbers will be { 2: 1, 3: 1, 4: 1, 1: 4, 5: 1}

# METHOD 2
# Boyer Moore - A Very Good Algorithm for Finding Majorities ( if majority exits ofc)

# Time: O(n) ??
# Space: O(1)

def boyerMoore(myList):

    result = 0
    count = 0

    for num in myList:
        if count == 0:
            result = num
        count += 1 if num == result else -1  # If num is equal to the result, add one. Else, minus one.

    return result


print(findMajority(myList))

print(boyerMoore(mySecondList))
