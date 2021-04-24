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