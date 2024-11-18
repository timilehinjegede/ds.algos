# Given a fixed-length integer array arr,
# duplicate each occurrence of zero, shifting the remaining elements to the right.
#
# Note that elements beyond the length of the original array are not written.
# Do the above modifications to the input array in place and do not return anything.
from typing import List


# Constraints:
# 1 <= arr.length <= 104
# 0 <= arr[i] <= 9

class Solution:
    @staticmethod
    def duplicateZeros(arr: List[int]) -> None:
        n = len(arr)
        zeros_count = 0

        for element in arr:
            if element == 0:
                zeros_count += 1

        for i in range(n - 1, -1, -1):
            if i + zeros_count < n:
                arr[i + zeros_count] = arr[i]

            if arr[i] == 0:
                zeros_count -= 1
                if i + zeros_count < n:
                    arr[i + zeros_count] = 0


if __name__ == '__main__':
    array = [1, 0, 2, 3, 0, 4, 5, 0]
    Solution.duplicateZeros(array)
    print(f'Test result is {array}')
