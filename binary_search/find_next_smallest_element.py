# https://leetcode.com/problems/find-smallest-letter-greater-than-target/submissions/
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        for i in letters:
            if i >target:
                return i
        return letters[0]
    
    
# I was being dogmatic and thinking about binary search. But the soluttion is way easier.    
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        if target >= letters[-1]:
            return letters[0]
        if target < letters[0]:
            return letters[0]
        low = 0
        high = len(letters)-1
        while low < high:
            m = int(low+ (high-low)/2)
            if letters[m] <= target:
                low = m+1
            else:
                high = m
        return letters[low]