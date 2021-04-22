from typing import *
from collections import Counter
import heapq
#TODO: why this works, but not my sorting work

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict = {}
        for x in nums:
            if x not in dict:
                dict[x] = 1
            else:
                dict[x] += 1
                
        return list(sorted(dict, key=dict.get, reverse=True))[0:k]
    
 
# Solution from leetcode 


class Solution_2:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]: 
        # O(1) time 
        if k == len(nums):
            return nums
        
        # 1. build hash map : character and how often it appears
        # O(N) time
        count = Counter(nums)   
        # 2-3. build heap of top k frequent elements and
        # convert it into an output array
        # O(N log k) time
        return heapq.nlargest(k, count.keys(), key=count.get)     
    

# bucket sort idea from leetcode discussion
class BucketSort:
    def topKFrequent(self, nums, k):
        bucket = [[] for _ in range(len(nums) + 1)]
        Count = Counter(nums).items()  
        for num, freq in Count: bucket[freq].append(num) 
        flat_list = [item for sublist in bucket for item in sublist]
        return flat_list[::-1][:k]

# class MySolution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         counts = []
#         for element in nums:
#             counts.append(nums.count(element))
#         original_list = copy.deepcopy(counts)
#         counts.sort()
#         original_list.index(counts[-k])
            
if __name__ == "__main__":
    solution = Solution()
    print(solution.topKFrequent([1,1,1,2,2,3], 2))