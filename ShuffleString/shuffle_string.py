# https://leetcode.com/problems/shuffle-string/submissions/

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        zipped = list(zip(indices, s))
        zipped.sort()        
        l= [char for idx, char in zipped]
        return "".join(l)
        