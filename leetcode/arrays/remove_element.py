from typing import List


# Given an integer array nums and an integer val, remove all occurrences of val in nums in-place.
# The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

# Consider the number of elements in nums which are not equal to val be k, to get accepted,
# you need to do the following things:
# 1. Change the array nums such that the first k elements of nums contain the elements which are not equal to val.
# The remaining elements of nums are not important as well as the size of nums.
# 2. Return k.

class Solution:
    @staticmethod
    def removeElement(nums: List[int], val: int) -> int:
        i = 0
        for j in range(len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1

        return i


if __name__ == '__main__':
    result_1 = Solution.removeElement([3, 2, 2, 3], 3)
    print(f'Test result 1 is {result_1}')
    result_2 = Solution.removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2)
    print(f'Test result 2 is {result_2}')
