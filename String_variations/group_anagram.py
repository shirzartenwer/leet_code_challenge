# https://leetcode.com/problems/group-anagrams/submissions/1401675676/?envType=study-plan-v2&envId=top-interview-150
from typing import List
from collections import Counter, defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = {}
        for ele in strs:
            if map.get(''.join(sorted(ele))) is not None:
                map[''.join(sorted(ele))].append(ele)
            else:
                map[''.join(sorted(ele))] = [ele]
        return list(map.values())


class Solution1:
    def groupAnagrams(self, strs):
        anagram_map = defaultdict(list)

        for word in strs:
            sorted_word = ''.join(sorted(word))
            anagram_map[sorted_word].append(word)

        return list(anagram_map.values())


Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
