from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]*len(nums)
        suffix = [1]*len(nums)

        for i in range(len(nums)):
            if i == 0:
                continue
            prefix[i] = nums[i-1] * prefix[i-1]

        for i in range(-1, -len(nums)-1, -1):
            if i == -1:
                continue
            suffix[i] = nums[i+1] * suffix[i+1]

        return [prefix[i]*suffix[i] for i in range(len(nums))]


class LessCodeSolution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1]*len(nums)

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]

        return res
