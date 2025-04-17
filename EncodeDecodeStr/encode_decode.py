# https://neetcode.io/problems/string-encode-and-decode
from typing import List


class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for string in strs:
            encoded_str = encoded_str + str(len(string)) + "#" + string
        return encoded_str

    def decode(self, s: str) -> List[str]:
        result_list, i = [], 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            result_list.append(s[j+1:j+1+length])
            i = j+1+length
        return result_list
