from typing import *

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