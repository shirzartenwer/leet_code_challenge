class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result = []
        for element in candies:
            if element + extraCandies >= max(candies):
                result.append(True)
            else:
                result.append(False)
        return result
        