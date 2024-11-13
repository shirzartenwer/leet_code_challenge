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
