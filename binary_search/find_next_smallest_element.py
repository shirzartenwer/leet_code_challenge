# https://leetcode.com/problems/find-smallest-letter-greater-than-target/submissions/
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        for i in letters:
            if i >target:
                return i
        return letters[0]
    
    
# I was being dogmatic and thinking about binary search. But the soluttion is way easier.    
class MySolution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        if target > letters[:-1]:
            return letters[0]
        elif target < letters[0]:
            return letters[0]
        else:
            return self.find(0, len(letters)-1, target)
        
    def find(self, L, i, j, target):
        if L[j] < L[i]:
            return L[j]
        m = (L[i]+L[j])//2
        if L[m] == target:
            return L[m]
        elif L[m] > target:
            return self.find(L[i], L[m-1], target)
        else:
            return self.find(L[m+1], L[j], target)