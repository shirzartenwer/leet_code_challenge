# https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/?envType=problem-list-v2&envId=sliding-window
from collections import Counter

# Brute Force Solution


class Solution:

    def check_valid(self, s: str, k: int):
        counter = Counter(s)
        if all(value >= k for value in counter.values()):
            return True
        else:
            return False

    def longestSubstring(self, s: str, k: int) -> int:

        result = []
        for i in range(len(s)):
            for j in range(i+1, len(s)+1):
                candidate = s[i:j]
                if self.check_valid(candidate, k):
                    result.append(len(candidate))

        if result:
            return max(result)
        else:
            return 0


# Divide and conquer class Solution:
class DNDSolution:

    def longestSubstring(self, s, k):
        if len(s) < k:
            return 0

        # Count frequency of each character
        freq = Counter(s)

        # Identify splitting character
        for c in freq:
            if freq[c] < k:
                # Split and recurse on each part
                # this is the most tricky part to understand
                return max(self.longestSubstring(t, k) for t in s.split(c))

        # If every character appears at least k times
        return len(s)
