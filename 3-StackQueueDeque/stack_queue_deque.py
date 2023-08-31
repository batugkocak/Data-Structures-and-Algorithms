# Stack


# There is no need to use a special type to use stacks, actually. Lists can do everything that stacks do.

myList = []

myList.append(4)
myList.append(3)  # [4, 3]
myList.pop()  # [4]
myList.append(5)  # [4, 5]
myList.pop()  # [4]

print(myList)

# And this is, that special Stack type

from queue import LifoQueue  # LIFO means Stack

# put means push, get means pop

lifoQueue = LifoQueue()

lifoQueue.put(1)
lifoQueue.put(10)
lifoQueue.put(20)

print(lifoQueue.get())
print(lifoQueue.get())
print(lifoQueue.get())
print(lifoQueue.empty())

# Queue

from queue import Queue  #FIFO

myQueue = Queue()

myQueue.put(1)
myQueue.put(10)
myQueue.put(20)

print(myQueue.get())
print(myQueue.get())
print(myQueue.get())
print(myQueue.empty())


# Deque

from collections import deque  # Double sided queue

myDeque = deque()

myDeque.append(10)
myDeque.append(20)
myDeque.append(30)
myDeque.appendleft(40)
print(myDeque)
print(myDeque.pop())
print(myDeque.popleft())
