# Linear Runtime Complexity, Constant Extra Space
# O(n), O(1)


nums = [2, 2, 1]

nums1 = [4, 1, 2, 1, 2]

nums2 = [1]  # This is an Edge Case, one additional "if" could solve Edge Cases

nums3 = [4, 1, 2, 1, 2, 4, 5, 5, 9]


# Method 1
# Brute Force

# Time: O(N^2)
# Space: O(1)

# TODO: NOT DONE!
def findSingle(nums):
    if len(nums) == 1:
        return nums[0]
    for i in range(0, len(nums)):
        for j in range(0, (len(nums))):
            if i == j:
                continue  # skip inner loop's this step
            if nums[i] == nums[j]:
                print(f"Duplicate found!: {nums[i]} and {nums[j]}")
                i += 1
                break  # breaks both loops, skips outer loop's step
            else:
                print(f"No duplicate found!: {nums[i]}")
    print("Function is not done!")

# Method 2
# Sorting

# Time: O(N log N)
# Space: O(1)


# Method 3
# Another Array

# Add item to the list, go to the next item
# If item is on the list, pop it, go to the next item
# Last one stays on the list, is our one single item

# Time: O(N) ??
# Space: O(N) ??

# Method 4
# Hash Map


# Method 5
# Bit Manipulation
# Using binaries and XOR gate

# TODO: LOOK AT THIS AGAIN!
def findSingle_bit(nums):
    result = 0
    for number in nums:
        result = number ^ result  # xor with number

    return result


# findSingle(nums1)
print(findSingle_bit(nums))
