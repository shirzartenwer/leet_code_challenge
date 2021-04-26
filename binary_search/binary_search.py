# https://leetcode.com/problems/sqrtx/submissions/
class Solution:
    def mySqrt(self, x: int) -> int:
        l=0
        h=x
        #1 2 3 4 5 6 7 8 
        while(h>=l):
            mid=(l+(h))//2
            if mid*mid==x:
                return mid
            elif mid*mid>x:
                h=mid-1 
            elif mid*mid<x:
                l=mid+1
        return h



# class MySolution:    
#     def binary_search(self, low, high, target):
#         if low > high:
#             return False
#         elif low == high:
#             if low == target:
#                 return low
#             else:
#                 return low - 1
#         else:
#             mid = (low + high)//2
#             if mid*mid == target:
#                 return mid
#             elif mid*mid < target:
#                 low +=1
#                 return self.binary_search(low,high, target)
#             else:
#                 high -=1
#                 return self.binary_search(low,high, target)
                
#     def mySqrt(self, x: int) -> int:
#         low = 0
#         high = x
#         return self.binary_search(low, high, x)
            