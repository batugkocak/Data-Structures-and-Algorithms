# list

myList = [1, 2, 3, 4, 5]
print(type(myList))

# Arrays on Python are mutable just like lists, so you can append new items
# But the main difference is you can put just one type of item, like integer.
# If you want to put different types of items to the same collection, you have you use list
myList.append('Wow! String!')

print(myList)

# Normally, our computer could put our infos in our (R)AM randomly. 
# It holds their value block's id/adress, and it can access them whenever we want
# Arrays are contigous it makes arrays faster because computer always now
# that the next value is in the next block/byte of RAM


import array as arr

myArray = arr.array("i", [3, 6, 9, 12])

myArray.append(5)

myList = [1, 2, 3, 4, 5]

otherList = [6, 7, 8]

myList.extend(otherList)
print(myList)

result = [0] * 8  # All 8 pointers points one block that contais value of 0
# If we change on of the elements of the array, computer creates 2 value and change that values pointer to point 2 

import sys

n = 15
myDynamicArray = []

for i in range(n):
    myLength = len(myDynamicArray)
    myByte = sys.getsizeof(myDynamicArray)
    myDynamicArray.append(n)
    print(f" Length: {myLength} Byte: {myByte}")
