# https://leetcode.com/problems/contains-duplicate-ii/?envType=study-plan-v2&envId=top-interview-150

from math import inf


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        num_map = {}
        min_length = inf

        for index, element in enumerate(nums):
            if element in num_map.keys():
                min_length = min(min_length, index - num_map[element])

            num_map[element] = index

        return min_length <= k
