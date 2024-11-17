from typing import List
import copy


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
            element_2_list = [x for x in range(nums.index(
                element_1)+1, len(nums)) if nums[x] + element_1 == target]
            if len(element_2_list) > 0:
                return [nums.index(element_1), element_2_list[0]]
            else:
                continue


# Double pointers

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # The following line gets the index of the original list sorted (https://stackoverflow.com/questions/7851077/how-to-return-index-of-a-sorted-list)
        get_the_sorted_index = sorted(range(len(nums)), key=lambda k: nums[k])
        nums.sort()
        left_pointer = 0
        right_pointer = len(nums) - 1
        while left_pointer <= right_pointer:
            result = nums[left_pointer] + nums[right_pointer]
            if result < target:
                left_pointer += 1
                continue
            elif result > target:
                right_pointer -= 1
                continue
            else:
                return get_the_sorted_index[left_pointer], get_the_sorted_index[right_pointer]


# Some other solution:

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        complement_dict = {}
        nums_len = len(nums)
        for i in range(nums_len):
            complement = target - nums[i]
            if complement in complement_dict:
                return [complement_dict[complement], i]
            else:
                if nums[i] in complement_dict:
                    continue
                complement_dict[nums[i]] = i

# TODO: Check hash_table and construct one https://www.tutorialspoint.com/python_data_structure/python_hash_table.htm
