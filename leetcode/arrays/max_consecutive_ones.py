from typing import List


# Given a binary array nums, return the maximum number of consecutive 1's in the array.
# Constraints:
# 1 <= nums.length <= 105
# nums[i] is either 0 or 1.
class Solution:
    @staticmethod
    def findMaxConsecutiveOnes(nums: List[int]) -> int:
        max_count = 0
        count = 0

        for num in nums:
            if num == 1:
                count += 1
                max_count = max(max_count, count)
            else:
                count = 0

        return max_count


if __name__ == '__main__':
    test_result_1 = Solution.findMaxConsecutiveOnes([1, 1, 0, 1, 1, 1])
    test_result_2 = Solution.findMaxConsecutiveOnes([1, 0, 1, 1, 0, 1])
    print(f'Test result 1 => {test_result_1}')
    print(f'Test result 2 => {test_result_2}')
