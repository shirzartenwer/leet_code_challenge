# https://neetcode.io/problems/minimum-window-with-characters

from collections import Counter
from math import inf

# time complexity O(n*k)


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        t_counter = {}
        t_ct_key = t_counter.keys()
        for ch in t:
            t_counter[ch] = 1 + t_counter.get(ch, 0)

        l = 0
        min_length = inf
        res = ""
        s_counter = {}
        for r in range(len(s)):
            s_counter[s[r]] = 1 + s_counter.get(s[r], 0)

            while s_counter.keys() >= t_ct_key and all(s_counter[key] >= t_counter[key] for key in t_ct_key):
                if r-l + 1 < min_length:
                    min_length = r-l+1
                    res = s[l:r+1]
                # the folllowing is preparing for moving the left pointer and remove the frequency count
                if s_counter[s[l]] > 1:
                    s_counter[s[l]] -= 1
                else:
                    del s_counter[s[l]]

                l += 1

            r += 1

        return res


# print(Solution().minWindow("ADOBECODEBANC", "ABC"))
print(Solution().minWindow("abc", "cba"))


#  answer that runs O(n) time and O(m) space


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        dict_t = Counter(t)         # O(m) time & space
        required = len(dict_t)        # how many distinct chars we need

        l = 0
        formed = 0                    # how many distinct chars are currently at target freq
        window_counts = {}
        ans = (inf, None, None)       # (window length, left, right)

        # expand the right pointer
        for r, ch in enumerate(s):
            window_counts[ch] = window_counts.get(ch, 0) + 1

            # if this char is one we care about and we've hit its needed count, bump formed
            if ch in dict_t and window_counts[ch] == dict_t[ch]:
                formed += 1

            # if we've got all required chars satisfied, try shrinking from the left
            while formed == required and l <= r:
                # update answer
                if (r - l + 1) < ans[0]:
                    ans = (r - l + 1, l, r)

                # remove the left char and update formed if needed
                left_ch = s[l]
                window_counts[left_ch] -= 1
                if left_ch in dict_t and window_counts[left_ch] < dict_t[left_ch]:
                    formed -= 1
                l += 1

        return "" if ans[0] == inf else s[ans[1]: ans[2] + 1]
