# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = len(nums) -1
        list_index = []
        while left <= right:
 
            mid = left + (right - left) // 2

            # Check if key is present at mid
            if nums[mid] == target:
                list_index.append(mid)
                if nums[mid-1] == target:
                    list_index.append(mid-1)
                if nums[mid+1] == target:
                    list_index.append(mid+1)
                return sorted(list_index)

            # If key is greater, ignore left half
            elif nums[mid] < target:
                left = mid + 1

            # If key is smaller, ignore right half
            else:
                right = mid - 1

        return [-1, 1]


Solution().searchRange([5,7,7,8,8,10], 8)