from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for element_1 in nums:
            for index_element_2 in range(nums.index(element_1)+1, len(nums)):
                if nums[index_element_2] + element_1 == target:
                    return [nums.index(element_1), index_element_2]
                else:
                    continue
                
            
# trying list comprehension:

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for element_1 in nums:
            element_2_list = [x for x in range(nums.index(element_1)+1, len(nums)) if nums[x] + element_1 == target]
            if len(element_2_list) > 0:
                return [nums.index(element_1), element_2_list[0]]
            else:
                continue


# TODO: Check hash_table and construct one https://www.tutorialspoint.com/python_data_structure/python_hash_table.htm
