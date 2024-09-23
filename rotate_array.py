# https: // leetcode.com/problems/rotate-array /?envType = study-plan-v2 & envId = top-interview-150


class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 1 or k == len(nums) or k == 0:
            nums[:] = nums[:]
        elif k <= len(nums):
            right = nums[:-k]
            for i in range(0, k):
                nums[i] = nums[i-k]
            nums[k:] = right[:]
        else:
            self.rotate(nums, k-len(nums))


sol = Solution()
sol.rotate([1, 2, 3, 4, 5, 6, 7], 3)
