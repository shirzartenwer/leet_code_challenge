from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        return [max(nums[i:i+k]) for i in range(len(nums)-k + 1)]


print(Solution().maxSlidingWindow([1, 2, 1, 0, 4, 2, 6], 3))
