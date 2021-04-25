from typing import *
# https://leetcode.com/problems/maximum-ice-cream-bars/discuss/1174585/Python-sort
class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        
        count = 0
        for cost in costs:
            if cost <= coins:
                count += 1
                coins -= cost
            else:
                break
            
        return count
    
    
    
#TODO: check out why this solution didn't work
class MySolution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        for k in range(len(costs)):
            if costs[0] > coins:
                return 0
            elif sum(costs[:k]) >= coins:
                return k 
            elif sum(costs) <= coins:
                return len(costs)