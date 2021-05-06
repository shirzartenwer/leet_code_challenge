
# https://leetcode.com/problems/running-sum-of-1d-array/
# TODO: why recursion doesn't work here?
class MySolution:
    def populate_list(self, nums: List[int], n: int):
        if n==0:
            return nums[n]
        else:
            return (self.populate_list(nums, n) + 
        self.populate_list(nums, n-1))
        
    def runningSum(self, nums: List[int]) -> List[int]:
        return self.populate_list(nums, len(nums))
        
        
        
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        if not nums or len(nums) <= 1:
            return nums
        res = [nums[0]]
        
        for num in nums[1:]:
            res.append(res[-1] + num)
            
        return res