# https://leetcode.com/problems/isomorphic-strings/

#TODO: Need to debug

from collections import Counter

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_counter = Counter(s)
        t_counter = Counter(t)
        if len(s_counter.keys()) == len(t_counter.keys()) and s_counter.values() == t_counter.values():
            return True
        else:
            return False