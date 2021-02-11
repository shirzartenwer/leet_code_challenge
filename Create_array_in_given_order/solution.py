class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        target_array = []
        for i in range(len(index)):
            target_array.insert(index[i],nums[i])
        return target_array
                
        