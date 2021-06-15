from collections import Counter
from typing import List

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
    # if the len of list is not equals to the combinatorial of n-1, then there is no town judge
        if len(trust) != n * (n-1) / 2 -1:
            return -1
        flat_trust_list = [sublist[1] for sublist in trust]
        counter = Counter(flat_trust_list)
        if n-1 in counter.values():
            pass
        else:
            return -1