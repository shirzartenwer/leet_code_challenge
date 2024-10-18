from typing import List
#  https://leetcode.com/problems/jump-game/


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        hash_m = {}

        if n == 1:
            return True

        def recursive_calls(index, nums, hash_m):
            if index in hash_m.keys():
                return hash_m[index]

            if nums[index] == 0:
                hash_m[index] = 0
                return 0

            if nums[index] >= len(nums) - index - 1:
                hash_m[index] = 1
                return 1
            else:
                for i in range(nums[index]):
                    result = recursive_calls(index + i+1, nums, hash_m)
                    if result >= 1:
                        return 1
                    hash_m[index] = result

                return hash_m[index]

        return recursive_calls(0, nums, hash_m) > 0


#  In the end we found aslo a better solution using Greedy actually

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        gas = 0
        for n in nums:
            if gas < 0:
                return False
            elif n > gas:
                gas = n
            gas -= 1

        return True
