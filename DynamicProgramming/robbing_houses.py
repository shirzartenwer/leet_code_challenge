# https://leetcode.com/problems/house-robber/description/?envType=study-plan-v2&envId=top-interview-150


class BruteForceSolution:
    def rob(self, nums: int):
        odd_sum = sum(nums[i] for i in range(len(nums)) if i//2 != 0)
        eve_sum = sum(nums[i] for i in range(len(nums)) if i//2 == 0)

        return odd_sum if odd_sum >= eve_sum else eve_sum


print(BruteForceSolution().rob([1, 2, 3, 1]))

# The brute force solution doesn't work in the following scenario
print(BruteForceSolution().rob([2, 1, 1, 2]))

#  The key here is I don't need to return which indices composed of the max solution. Just what's the max solution


# def rob_h(i, memo) -> int:
#     if memo[i] != -1:
#         return memo[i]
#     if i == 0:
#         memo[i] = nums[0]
#         return memo[i]
#     if i == 1:
#         memo[i] = max(nums[0], nums[1])
#         return memo[i]
#     memo[i] = max(nums[i] + rob_h(i-2, memo), rob_h(i-1, memo))
#     return memo[i]

# n = len(nums)
# memo = [-1]*n
# return rob_h(n-1, memo)
