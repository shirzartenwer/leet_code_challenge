'''Problem description:

We have a collection of stones, each stone has a positive integer weight.

Each turn, we choose the two heaviest stones and smash them together.  Suppose the stones have weights x and y with x <= y.  The result of this smash is:

If x == y, both stones are totally destroyed;
If x != y, the stone of weight x is totally destroyed, and the stone of weight y has new weight y-x.
At the end, there is at most 1 stone left.  Return the weight of this stone (or 0 if there are no stones left.)
'''


from typing import Union, List
import copy

class Solution:
    
    def lastStoneWeight(self, stones: List[int]) -> int:
        def select_two_biggest_number(stone_list: List[int]) ->Union[int, int]:
            seperate_stone_list = copy.deepcopy(stones)
            biggest_element = max(seperate_stone_list)
            seperate_stone_list.remove(biggest_element)
            second_biggest_element = max(seperate_stone_list)
            return biggest_element, second_biggest_element
        
        while len(stones) >1:
                biggest, second_biggest = select_two_biggest_number(stones)
                if biggest==second_biggest:
                    stones.remove(biggest)
                    stones.remove(second_biggest)
                else:
                    stones.remove(biggest)
                    stones.remove(second_biggest)
                    stones.append(biggest-second_biggest)

        
            
        if len(stones) == 1:
            return stones[0]
        else:
            return 0
        
        
        
# def lastStoneWeight(self, stones: List[int]) -> int:
#         while len(stones)>1:
#             stones.sort()
#             y = stones.pop()
#             x = stones.pop()
#             stones.append(y-x)    # don't need to compare x & y...

#         return stones[0]
        
if __name__ == "__main__":
    solution = Solution()
    print(solution.lastStoneWeight(stones=[2,7,4,1,8,1]))
    
    
    
    