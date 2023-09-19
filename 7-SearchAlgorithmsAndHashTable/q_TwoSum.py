class Solution:
    def twoSum(self, nums, target: int):
        myHashMap = {}
        
        for ix, num in enumerate(nums):
            difference = target - num
            if difference in myHashMap:
                return [myHashMap[difference], ix]
            myHashMap[num] = ix