def hashFunction(key):
    myHash = 0
    for letter in key:
        myHash = (myHash + ord(letter) * 19)
    return myHash  


#https://realpython.com/python-hash-table/
def hash_function(key):
        return sum(
            index * ord(character)
            for index, character in enumerate(repr(key).lstrip("'"), 1)
        )

class HashTable:

    def __init__(self, size = 13) -> None:
         self.dataMap = [None] * size

    def hash(self, key):
        myHash = 0
        for letter in key:
            myHash = (myHash + ord(letter) * 19) % len(self.dataMap)
        return myHash  

    def setItem(self,key,value):
        index = self.hash(key)
        if self.dataMap[index] == None:
            self.dataMap[index] = []
        self.dataMap[index].append([key, value])

    def getItem(self, key):
        index = self.hash(key)
        if self.dataMap is not None:
            for i in range(len(self.dataMap[index])):
                if self.dataMap[index][i][0] == key:
                    return self.dataMap[index][i][1]
        return None
        
    def getKeys(self):
        keys = []
        for i in range(len(self.dataMap)):
            if self.dataMap[i] is not None:
                for j in range(len(self.dataMap[i])):
                    keys.append(self.dataMap[i][j][0])

    def printTable(self):
        for index, value in enumerate(self.dataMap):
            print(index, "->", value)

myHashTable = HashTable()

myHashTable.setItem('Apple', 100)
myHashTable.setItem('Banana', 150)
myHashTable.setItem('Melon', 250)
myHashTable.setItem('Watermelon', 300)
myHashTable.setItem('Strawberry', 100)
myHashTable.setItem('Lemon', 150)


myHashTable.printTable()
            