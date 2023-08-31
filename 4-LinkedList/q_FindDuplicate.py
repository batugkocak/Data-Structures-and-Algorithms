# You can't use HashSet or modify the array

myList = [5, 2, 1, 3, 4, 2]


def solution():
    for i in range(0, len(myList)):
        for j in range(0, len(myList)):
            if i == j:
                continue
            if myList[i] == myList[j]:
                return myList[i]


# TODO: Learn FloydAlgorithm !!!!
def solutionFloyd():  # Floyd Cycle Detection Algorithm
    slowPointer = 0
    fastPointer = 0

    while True:
        slowPointer = myList[slowPointer]
        fastPointer = myList[myList[fastPointer]]
        if slowPointer == fastPointer:
            break

    secondSlowPointer = 0
    while True:
        slowPointer = myList[slowPointer]
        secondSlowPointer = myList[secondSlowPointer]
        if slowPointer == secondSlowPointer:
            return slowPointer


print(solution())
print(solutionFloyd())
