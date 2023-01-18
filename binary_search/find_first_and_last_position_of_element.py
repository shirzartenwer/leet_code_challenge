# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1,-1]
        l = 0
        r = len(nums) - 1
        # The first part is to find the left bounding index of the number
        while l<r:
            mid = (l+r) // 2
            if nums[mid] < target:
                l = mid +1
            elif nums[mid] == target:
                r = mid 
            else:
                r = mid - 1
        
        if nums[l] != target:
            return [-1,-1]
        else:
            # The second part is looking for the right index of the number
            end = start = l
            r = len(nums) - 1
            while l<=r:
                
                mid = (l+r) // 2
                if nums[mid] == target:
                    l = mid + 1
                else:
                    r = mid - 1
            end = r        
            return [start,end]



Solution().searchRange([5,7,7,8,8,10], 8)