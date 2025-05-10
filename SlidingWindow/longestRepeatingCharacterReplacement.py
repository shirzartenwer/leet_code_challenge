# https://neetcode.io/problems/longest-repeating-substring-with-replacement
#  Brufte Force

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        for i in range(len(s)):
            count, maxf = {}, 0
            for j in range(i, len(s)):
                count[s[j]] = 1 + count.get(s[j], 0)
                maxf = max(maxf, count[s[j]])
                #  The key is this condition, we want to find the
                # longest string that require least character to be replaced
                if (j - i + 1) - maxf <= k:
                    res = max(res, j - i + 1)
        return res


class SlidingWindowSolution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0

        l = 0
        maxf = 0
        for r in range(len(s)):
            # constucting the frequency of every character that ever encountered
            count[s[r]] = 1 + count.get(s[r], 0)
            maxf = max(maxf, count[s[r]])

            while (r - l + 1) - maxf > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)

        return res
