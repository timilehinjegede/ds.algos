from typing import List


# Complexity Analysis:
# -------------------------------------------------------
# |   Case    | Time Complexity   |   Space Complexity  |
# -------------------------------------------------------
# |   Best    | O(n^2)            |        O(1)         |
# |   Worst   | O(n^2)            |        O(1)         |
# |  Average  | O(n^2)            |        O(1)         |
# -------------------------------------------------------

class SelectionSort:
    @staticmethod
    def sort(nums: List[int]) -> None:

        n = len(nums)

        for i in range(n):
            min_index = i

            for j in range(i + 1, n):
                if nums[j] < nums[min_index]:
                    min_index = j

            nums[i], nums[min_index] = nums[min_index], nums[i]


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
        SelectionSort.sort(array)
        print(f'{name} -> Original: {original}, Sorted: {array}')
