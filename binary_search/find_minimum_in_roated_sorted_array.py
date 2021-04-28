# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

class Solution:
    def findMin(self, nums: List[int]) -> int:
        i = 0
        j = len(nums)-1
        
        if nums[j] > nums[0]:
            return nums[0]
        
        while i < j:
            middle = int(i + (j-i)/2)
            
            if nums[middle]> nums[middle+1]:
                return nums[middle+1]
            elif nums[middle] > nums[i]:
                i = middle + 1
            else:
                j = middle
                
        return nums[i]
    
    
class Solution2:
    def findMin(self, nums: List[int]) -> int:
        return min(nums)