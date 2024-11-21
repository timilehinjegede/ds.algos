from typing import List


# Complexity Analysis:
# -------------------------------------------------------
# |   Case    | Time Complexity   |   Space Complexity  |
# -------------------------------------------------------
# |   Best    | O(n)              |        O(1)         |
# |   Worst   | O(n^2)            |        O(1)         |
# |  Average  | O(n^2)            |        O(1)         |
# -------------------------------------------------------

class BubbleSort:
    @staticmethod
    def sort(nums: List[int]) -> None:

        n = len(nums)

        for i in range(n):
            swapped = False

            for j in range(n - 1 - i):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
                    swapped = True

            if not swapped:
                break


if __name__ == '__main__':
    test_arrays = {
        "Test Result 1": [1, 2, 3, 4, 5],
        "Test Result 2": [5, 4, 3, 2, 1],
        "Test Result 3": [4, 2, 2, 8, 3],
        "Test Result 4": [-3, 5, -2, 8, -1],
        "Test Result 5": [-2, 45, 0, 11, -9],
    }

    for name, array in test_arrays.items():
        original = array.copy()
        BubbleSort.sort(array)
        print(f'{name} -> Original: {original}, Sorted: {array}')
