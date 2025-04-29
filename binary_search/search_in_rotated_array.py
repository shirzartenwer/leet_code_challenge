from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:

        l = 0
        r = len(nums)-1
        while l <= r:
            mid = (l + r) // 2
            if target == nums[mid]:
                return mid

            if target < nums[mid]:
                if target < nums[l]:
                    if nums[l] <= nums[r]:
                        return -1
                    else:
                        l = mid
                else:
                    r = mid

            else:
                if target > nums[r]:
                    if nums[l] <= nums[r]:
                        return -1
                    else:
                        r = mid - 1
                else:
                    l = mid+1


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            # checking if middle value belongs to the left or right
            # The first one means middle value belongs to the left, and there is not pivot in between
            if nums[l] <= nums[mid]:
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1

            # middle value belongs to the right
            else:
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1
        return -1


# print(Solution().search([3, 4, 5, 6, 1, 2], 1))
print(Solution().search([3, 5, 6, 0, 1, 2], 4))
