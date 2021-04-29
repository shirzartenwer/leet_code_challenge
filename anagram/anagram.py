# https://leetcode.com/problems/valid-anagram/submissions/

from collections import Counter
# NOTE: to compare if 2 strings are anagram, they just need to 
# be composed of the same letter with same frequency of each letter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_s = Counter(list(s))
        count_t = Counter(list(t))
        
        if count_s == count_t:
            return True
        else:
            False 