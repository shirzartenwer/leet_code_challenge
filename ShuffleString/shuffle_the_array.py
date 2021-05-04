# https://leetcode.com/problems/shuffle-the-array/
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        x = nums[:n]
        y = nums[n:]
        z = []

        if type(x) == int:
            x = [x]
        if type(y) == int:
            y = [y]

        for i, e in enumerate(x):
            z.append(e)
            z.append(y[i])

        return z
        