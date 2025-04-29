# https://neetcode.io/problems/permutation-string
# NOTE: this quesiton is a bit ill-defined, its not clear what counts as permutation and what doesn't.
from collections import Counter

#  Time complexity of this is O (n*k),
# because when every time when the counter is constructed,
# it needs to scan through k elements


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        need = Counter(s1)
        k = len(s1)
        for i in range(len(s2) - k + 1):
            if Counter(s2[i:i+k]) == need:   # direct equality
                return True
        return False


# An eaasier sliding window is to use counter minimally.
# This results in O(n), because Window counter is constructed at the beginning, and
# iteratively expanded
class MinCounterWindow:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m, n = len(s1), len(s2)
        if m > n:                     # early exit
            return False

        need = Counter(s1)
        window = Counter()

        left = 0
        for right, ch in enumerate(s2):
            window[ch] += 1

            # keep window length == m
            if right - left + 1 > m:
                window[s2[left]] -= 1
                if window[s2[left]] == 0:
                    del window[s2[left]]
                left += 1

            # check permutation
            if window == need:
                return True

        return False


#  The idea in this solution is having
class SlidingWindowSolution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1Count, s2Count = [0]*26, [0]*26
        for i in range(len(s1)):
            # ord(s1[i]) - ord('a') is determininig the index of the current character s1[i]
            # because ord computes the ASCII value of single character. And character starts with A
            # so you minus ord('a') to get relative position
            s1Count[ord(s1[i]) - ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] += 1

        matches = 0
        # comparing if the counter hashmap of each character is the same
        for i in range(26):
            matches += (1 if s1Count[i] == s2Count[i] else 0)

        l = 0
        # only iterate the part of S2 that's longer than S1
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True

            index = ord(s2[r]) - ord('a')
            s2Count[index] += 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] + 1 == s2Count[index]:
                matches -= 1

            # because we are moving the left point,
            # we update the match for after removing this character at position l
            index = ord(s2[l]) - ord('a')
            s2Count[index] -= 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] + 1 == s2Count[index]:
                matches -= 1
            l += 1
        return matches == 26
