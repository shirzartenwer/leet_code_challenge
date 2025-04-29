from math import inf
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        left_bar = 0
        right_bar = 0
        total_water = 0

        i = 0
        j = 0
        while i <= j and i < len(height) and j < len(height):
            if height[i] == 0 or (i+1 < len(height) and height[i+1] >= height[i]):
                i += 1
                j += 1
                continue
            left_bar = height[i]
            rolling_sum = 0
            j += 1
            while j > i and j < len(height):
                if j < len(height)-1 and height[j+1] <= height[j] and height[j] != 0 and height[j] > height[j-1]:
                    right_bar = height[j]
                    total_water += min(left_bar, right_bar) * \
                        (j - i - 1) - rolling_sum
                    left_bar = right_bar
                    right_bar = 0
                    rolling_sum = 0
                    i = j
                else:
                    rolling_sum += height[j]
                    j += 1

        return total_water


print(Solution().trap([4, 2, 0, 3, 2, 5]))  # This case fails the above algo
print(Solution().trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))


class PrefixSuffixSolution:
    def trap(self, height: List[int]) -> int:
        current_max = -inf
        max_left = []
        max_right = []

        for i, ele in enumerate(height):
            current_max = max(current_max, ele)
            max_left.append(current_max)

        current_max = -inf
        for i in range(len(height)-1, -1, -1):
            current_max = max(current_max, height[i])
            max_right.append(current_max)

        trapped_water = 0
        for i in range(len(height)):
            # The key insight is to calculate water trapped at each index
            trapped_water += min(max_left[i], max_right[i]) - height[i]

        return trapped_water


class TwoPointerSolution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        current_max = 0
        max_left = [0] * len(height)
        max_right = [0] * len(height)

        for i, ele in enumerate(height):
            current_max = max(current_max, ele)
            max_left[i] = current_max

        current_max = 0
        for i in range(len(height)-1, -1, -1):
            current_max = max(current_max, height[i])
            max_right[i] = current_max

        trapped_water = 0
        for i in range(len(height)):
            trapped_water += min(max_left[i], max_right[i]) - height[i]

        return trapped_water
