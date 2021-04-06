'''Given an array of integers arr, write a function
that returns true if and only if the number of occurrences of each value in the array is unique.'''

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        a = collections.Counter(arr)
        return len(a.values()) == len(set(a.values()))