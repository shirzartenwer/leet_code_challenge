#  https://leetcode.com/problems/kth-largest-element-in-an-array/description/
import heapq
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        heap = []
        for i in range(n):
            heapq.heappush(heap, nums[i])
            if len(heap) > k:
                heapq.heappop(heap)
        return heapq.heappop(heap)


# of course, it wasn't allowed to use sort when doing this problem, because
# the purpose is to practice heap
class QuickSolution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        return (nums[-k])


print(Solution().findKthLargest([3, 2, 1, 5, 6, 4], 2))
print(QuickSolution().findKthLargest([3, 2, 1, 5, 6, 4], 2))
