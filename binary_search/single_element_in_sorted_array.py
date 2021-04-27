# https://leetcode.com/problems/single-element-in-a-sorted-array/
'''This question is hinted to use binary search. But before implementing a binary search, a simple counter can solve the problem.'''
from collections import Counter
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        b = Counter(nums)
        return b.most_common()[-1][0]
    
    
# TODO: check why this solution doesn't work. GET a correct binary search implementation
class NotWorkingSolution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        low = 0
        high = len(nums)-1
        return self.find_single(nums, low, high)
    

    def find_single(self, L, i, j):
        if j < i:
            return L[j]
        middle_index = (i+j)//2
        if L[middle_index] != L [middle_index +1]:
            if L[middle_index] != L [middle_index -1]:
                return L[middle_index]
            else:
                return self.find_single(L, middle_index+1, j)
        else:
            return self.find_single(L, i, middle_index-1)
        
            
        
        
# Double pointers 

from collections import Counter
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        low = 0
        high = len(nums)-1
        while low < high:
            middle_index = (low+high)//2
            if (middle_index % 2 ==0 and nums[middle_index] == nums [middle_index +1]) or (middle_index % 2 ==1 and nums[middle_index] == nums [middle_index -1]):
                low = middle_index + 1
            else:
                high = middle_index
        return nums[low]  #TODO: understand why we return the lower one
    
