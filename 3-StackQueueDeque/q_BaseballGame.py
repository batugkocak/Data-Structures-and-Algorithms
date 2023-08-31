# ops = [5, 2 , C , D , +]  # Output = 30
# + records a new score that is sum of last 2 scores.
# D records a new score that is double the previous score
# C invalidates the last score.


ops = ["5", "2", "C", "D", "+"]


def getScore(ops):
    stack = []  # I will use this list as Stack with append and pop
    for op in ops:
        if op == "C":
            stack.pop()
        elif op == "+":
            x = stack.pop()
            y = stack.pop()
            stack.append(y)
            stack.append(x)
            stack.append(x + y)
            # Atil Samancioglu : stack.append(myStack[-1] + myStack[-2])
        elif op == "D":
            x = stack.pop()
            stack.append(x)
            stack.append(x * 2)
        else:
            stack.append(int(op))
    return sum(stack)


print(getScore(ops))