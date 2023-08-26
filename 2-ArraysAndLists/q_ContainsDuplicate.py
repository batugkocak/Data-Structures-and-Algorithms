'''
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

'''

nums = [1, 2, 3, 1]
nums2 = [1, 2, 3, 4, 5, 6, 7, 8]


# METHOD 1:
# Brute Force

# Time: O(n^2)
# Space: O(1)
def find_duplicate_bf(nums):
    isDuplicate = False
    for i in range(0, len(nums)):
        for j in range(i + 1, (len(nums))):
            if nums[i] == nums[j]:
                isDuplicate = True
                break
    print(isDuplicate)


# METHOD 2:
# First, sort the array. Then, check every two element that next o each other.
# For this, time complexity should be equal to sort algorithm's complexity.

# Time: O(n logN) # This is the most used and optimized sorting algorithm's time complexity
# Space: O(1)

def find_duplicate_sort(nums):
    isDuplicate = False
    nums.sort()
    for i in range(0, len(nums)):
        j = i + 1
        if (j == len(nums) - 1):
            break
        if nums[i] == nums[j]:
            isDuplicate = True
            break

        j += 1
    print(isDuplicate)


# METHOD 3:
# Using HashSet, HashSet holds every element unique.


# Time: O(n)
# Space: O(n)

def find_duplicate_hash2(nums):
    hashSet = set()  # HashSet could not contain duplicate variables
    for num in nums:
        if num in hashSet:
            return True
        hashSet.add(num)
    return False
# METHOD 4
# So duplicate elements would not count same much as the original array.
# Thanks to this, if array has a duplicated element, hashSet and original array
# lengths will be different.
def find_duplicate_hash(nums):
    return len(nums) != len(set(nums))
# if lenghts are not equal, return false


# find_duplicate_bf(nums2)
# find_duplicate_sort(nums)
print(find_duplicate_hash(nums2))
