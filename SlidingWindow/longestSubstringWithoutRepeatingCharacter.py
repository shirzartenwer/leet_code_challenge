#  https://leetcode.com/problems/longest-substring-without-repeating-characters/description/?envType=study-plan-v2&envId=top-interview-150
import heapq


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0

        char_list = list(s)
        cur_char = s[0]
        collection = []

        for index, element in enumerate(char_list[1:]):
            if element not in cur_char:
                cur_char = cur_char + element
            else:
                heapq.heappush(collection, (len(cur_char), cur_char))
                i = 0
                while cur_char[i] != element:
                    i += 1

                cur_char = cur_char[i+1:] + element

        heapq.heappush(collection, (len(cur_char), cur_char))

        return heapq.nlargest(1, collection)[0][0]


# actually an easier way is to do sliding windows


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0

        char_set = set()
        l = 0

        for r in range(len(s)):
            while s[r] in char_set:
                # they key trick is to start shrinking the string from left,
                # becaues you want to maximize the chance of reusing other strings
                # that are not repeated to have a longer substring in the end
                char_set.remove(s[l])
                l += 1
            char_set.add(s[r])
            res = max(res, r-l+1)
        return res
