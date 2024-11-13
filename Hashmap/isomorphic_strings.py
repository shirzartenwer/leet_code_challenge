# https://leetcode.com/problems/isomorphic-strings/

# TODO: Need to debug

from collections import Counter


class Solution:
    # This solution turns out to be too slow
    def find(self, string, character):
        return [i for i, ltr in enumerate(string) if ltr == character]

    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        if len(set(s)) != len(set(t)):
            return False

        for index in range(len(s)):
            if self.find(s, s[index]) != self.find(t, t[index]):
                return False

        return True


class AnotherSolution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        return len(set(s)) == len(set(zip(s, t))) == len(set(t))


class DefaultSolution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        mapping_s_t = {}
        mapping_t_s = {}

        for c1, c2 in zip(s, t):

            # Case 1: No mapping exists in either of the dictionaries
            if (c1 not in mapping_s_t) and (c2 not in mapping_t_s):
                mapping_s_t[c1] = c2
                mapping_t_s[c2] = c1

            # Case 2: Ether mapping doesn't exist in one of the dictionaries or Mapping exists and
            # it doesn't match in either of the dictionaries or both
            elif mapping_s_t.get(c1) != c2 or mapping_t_s.get(c2) != c1:
                return False

        return True


AnotherSolution().isIsomorphic("add", "egg")
