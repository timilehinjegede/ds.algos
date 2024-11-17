# Given an integer array nums sorted in non-decreasing order,
# return an array of the squares of each number sorted in non-decreasing order.
from typing import List


# Constraints:
# 1 <= nums.length <= 104
# -104 <= nums[i] <= 104
# nums is sorted in non-decreasing order.

class Solution:
    @staticmethod
    def sortedSquares(nums: List[int]) -> List[int]:
        squared_array = []
        for num in nums:
            squared_array.append(num * num)

        return sorted(squared_array)


if __name__ == '__main__':
    test_result_1 = Solution.sortedSquares([-4, -1, 0, 3, 10])
    print(f'Test result 2 is => {test_result_1}')
    test_result_2 = Solution.sortedSquares([-7, -3, 2, 3, 11])
    print(f'Test result 2 is => {test_result_2}')
