# https://leetcode.com/problems/longest-consecutive-sequence/description/?envType=study-plan-v2&envId=top-interview-150

def longestConsecutive(arr) -> int:
    num_set = set(arr)
    max_seq = 0
    for num in arr:
        if num - 1 not in num_set:
            seq_len = 0
            while num in num_set:
                seq_len += 1
                num += 1
            max_seq = max(max_seq, seq_len)

    return max_seq


class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        nums = set(nums)
        table = {}
        maxval = 0
        for num in nums:
            x = table.get(num - 1, 0)
            y = table.get(num + 1, 0)
            val = x + y + 1
            table[num - x] = val
            table[num + y] = val
            maxval = max(maxval, val)
        return maxval


print(longestConsecutive([100, 4, 200, 1, 3, 2]))
print(Solution().longestConsecutive([100, 4, 200, 1, 3, 2]))
