from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        n = len(height)
        r = n-1
        area = (r - l) * min(height[r], height[l])
        while l < r:
            area = max(area, (r - l) * min(height[r], height[l]))

            # The key of this problem is the following condition:
            # optimizing for the height of minimum bar
            # Trying for other condition such as moving left or right pointer based on the size of area of next pointer position is not correct,
            # like using the following line is not correct
            # if (r - (l+ 1)) * min(height[r], height[l+1]) > (r-1 - l) * min(height[r-1], height[l])

            # however, there is no general take away from this, just the perks of this problem
            if height[l] <= height[r]:
                l = l+1
            else:
                r = r-1

        return area
