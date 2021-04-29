# https://leetcode.com/problems/valid-anagram/submissions/

from collections import Counter
# NOTE: to compare if 2 strings are anagram, they just need to 
# be composed of the same letter with same frequency of each letter

class Solution1:
    def isAnagram(self, s: str, t: str) -> bool:
        count_s = Counter(list(s))
        count_t = Counter(list(t))
        
        if count_s == count_t:
            return True
        else:
            False 
            
            
# Second solution: following the logic of the first one: if two strings are anagram, 
# then after sort, these 2 sorted list should be equal

class Solution2:
    def isAnagram(self, s: str, t: str) -> bool:
        count_s =list(s)
        count_t = list(t)
        
        if count_s == count_t:
            return True
        else:
            False 
            
            
if __name__ == '__main__':
    solution = Solution2()
    print(solution.isAnagram("rat", "car"))