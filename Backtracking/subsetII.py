from typing import List


class Solution:
    def __init__(self):
        self.res = []
        self.track = []

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # 先排序，让相同的元素靠在一起
        nums.sort()
        self.backtrack(nums, 0)
        return self.res

    def backtrack(self, nums: List[int], start: int) -> None:
        # 前序位置，每个节点的值都是一个子集
        self.res.append(self.track[:])

        for i in range(start, len(nums)):
            # 剪枝逻辑，值相同的相邻树枝，只遍历第一条
            if i > start and nums[i] == nums[i - 1]:
                continue
            self.track.append(nums[i])
            self.backtrack(nums, i + 1)
            self.track.pop()
