# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/?envType=study-plan-v2&envId=top-interview-150

from typing import List
import collections


class Solution:
    def majorityElementSort(self, nums):
        nums.sort()
        #  Always good to think about if there is a possiblity to sort the array
        return nums[len(nums) // 2]

    def majorityElementDict(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        nums_map = {}

        for i in nums:
            if i in nums_map.keys():
                nums_map[i] += 1
            else:
                nums_map[i] = 1

        max_element = 0
        max_value = 0
        for key, value in nums_map.items():
            if value > max_value:
                max_element = key
                max_value = value
        return max_element

    def Hashmap(self, nums):
        counts = collections.Counter(nums)
        return max(counts.keys(), key=counts.get)
