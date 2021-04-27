# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        low = 1
        high = n
        while low<high:
            middle = int(low + (high-low)/2)
            if isBadVersion(middle) is True:
                high = middle # Here: high is not middle+1, because when the middle one is bad, you can't make sure if it's the first one that is bad
            else:
                low = middle+1
        return low
            
        