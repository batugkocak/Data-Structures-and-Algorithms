# 10 20 30 40 -> Stack -> Pop removes 40 -> Pop and Push is O(1)
# 10 20 30 40 -> Queue -> Pop removes 10
# The only difference between them is pop
from collections import deque


# Using Queue for implementing Stack is going to make our time complexity for pop O(n)


class Stack():
    def __init__(self):
        self.queue = deque()  # We are using deque to not complicate the top function, ü
        # we're still going to use deque like queue

    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int:
        for i in range(len(self.queue) - 1):
            self.queue.append(self.queue.popleft())  # popleft is same with normal queue
        return self.queue.popleft()
    # Add every element to last of the queue except the last one, and pop it like normal queue
    # 1 2 3 -> 2 3 1 -> 3 1 2 -> 1 2  # It's the same as Stack but only its slower
    def top(self) -> int:
        return self.queue[-1]

    def empty(self) -> bool:
        return len(self.queue) == 0
