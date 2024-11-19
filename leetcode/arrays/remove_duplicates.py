# Given an integer array nums sorted in non-decreasing order,
# remove the duplicates in-place such that each unique element appears only once.
# The relative order of the elements should be kept the same. Then return the number of unique elements in nums.
from typing import List


# Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:
# 1. Change the array nums such that the first k elements of nums contain the unique elements in the order they were
# present in nums initially. The remaining elements of nums are not important as well as the size of nums.
# 2. Return k.

# The judge will test your solution with the following code:
# int[] nums = [...]; // Input array
# int[] expectedNums = [...]; // The expected answer with correct length
#
# int k = removeDuplicates(nums); // Calls your implementation
#
# assert k == expectedNums.length;
# for (int i = 0; i < k; i++) {
#     assert nums[i] == expectedNums[i];
# }
# If all assertions pass, then your solution will be accepted.

class Solution:
    @staticmethod
    def removeDuplicates(nums: List[int]) -> int:
        unique_index = 0
        n = len(nums)

        for i in range(1, n):
            if nums[unique_index] != nums[i]:
                unique_index += 1
                nums[unique_index] = nums[i]

        return unique_index + 1


if __name__ == '__main__':
    result_1 = Solution.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4])
    print(f'Test result 1 is {result_1}')
    result_2 = Solution.removeDuplicates([1, 1, 2])
    print(f'Test result 2 is {result_2}')
