from typing import List
#  https://leetcode.com/problems/combinations/?envType=study-plan-v2&envId=top-interview-150


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []

        def backtracking(cur: List[int]):
            if len(cur) == k:
                ans.append(cur[:])
                return

            start = cur[-1]+1 if cur else 1
            for i in range(start, n+1):
                cur.append(i)
                # For loop for the rest of the element while in the for loop is backtracking
                backtracking(cur)
                cur.pop()

        backtracking([])
        return ans


print(Solution().combine(5, 3))
