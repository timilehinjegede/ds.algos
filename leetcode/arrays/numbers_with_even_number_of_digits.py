from typing import List


# Given an array nums of integers, return how many of them contain an even number of digits.
# Constraints:
# 1 <= nums.length <= 500
# 1 <= nums[i] <= 105

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        for num in nums:
            if self.countDigits(num) % 2 == 0:
                count += 1
        return count

    def countDigits(self, digit: int) -> int:
        if digit // 10 == 0:
            return 1
        else:
            return 1 + self.countDigits(digit // 10)


if __name__ == '__main__':
    solution = Solution()
    result = solution.findNumbers([555, 901, 482, 1771])
    print(f'Test result is => {result}')
