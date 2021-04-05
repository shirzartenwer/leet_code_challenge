# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

# Follow up: Could you implement a solution with a linear runtime complexity and without using extra memory?

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        numDict = set()
        for num in nums:
          if num in numDict:
            numDict.remove(num)
          else:
            numDict.add(num)
            
        ## After the above, only one item will be left in the set.
        return numDict.pop()