# https://leetcode.com/problems/merge-sorted-array/?envType=study-plan-v2&envId=top-interview-150

#  They to this solution is to start sorting from the back of the nums1, since there are anyway spaces to fit every element.

class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Merges nums2 into nums1 in-place.
        """
        # Start filling nums1 from the end
        i = m - 1  # Pointer to the last element in the valid part of nums1
        j = n - 1  # Pointer to the last element in nums2
        k = m + n - 1  # Pointer to the last position in nums1

        # Merge in reverse order
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1

        # If there are remaining elements in nums2, copy them to nums1
        # No need to copy nums1 elements because they are already in place
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1


sol = Solution()
sol.merge([2, 0], 1, [1], 1)
