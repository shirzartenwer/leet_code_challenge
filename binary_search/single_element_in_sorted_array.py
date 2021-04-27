# https://leetcode.com/problems/single-element-in-a-sorted-array/
'''This question is hinted to use binary search. But before implementing a binary search, a simple counter can solve the problem.'''
from collections import Counter
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        b = Counter(nums)
        return b.most_common()[-1][0]