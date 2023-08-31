myString = ["h", "e", "l", "l", "o"]  # Output should be "olleh"


def reverseRecursive(string, start: int, end: int):
    if start > end:
        return True
    if start == end:
        print("Wow!")
    string[start], string[end] = string[end], string[start]
    reverseRecursive(string, start + 1, end - 1)


print(myString)
reverseRecursive(myString, 0, len(myString) - 1)  # start: 0, end: 4 -> start: 3, end: 1
myName = ["B", "A", "T", "U", "G"]
reverseRecursive(myName, 0, len(myName) -1)
print(myName)
print(myString)
