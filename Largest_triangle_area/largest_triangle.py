'''You have a list of points in the plane. Return the area 
of the largest triangle that can be formed by any 3 of the points.'''

# https://leetcode.com/problems/largest-triangle-area/

# This is my soluation, but apparently my formula for calculating area is 
# not general enough. Check the solution below
# class Solution:
#     def largestTriangleArea(self, points: List[List[int]]) -> float:
#         min_x = points[0][0]
#         min_y = points[0][1]
#         max_x = points[0][0]
#         max_y = points[0][1]
#         for element in points:
#             if element[0] < min_x:
#                 min_x = element[0]
#             if element[0] > max_x:
#                 max_x = element[0]
#             if element[1] < min_y:
#                 min_y = element[1]
#             if element[1] > max_y:
#                 max_y = element[1]
                
#         return (max_x - min_x) * (max_y - min_y)/2

class Solution:
    def find_area(self, L: List[List[int]]):
	   # checkout the formula for finding area of a polygon in cartesian co-ordinates
        L = L + [L[0]]
        area = 0
        for i in range(3):
            area += L[i][0] * L[i + 1][1]
        for j in range(3):
            area -= L[j][1] * L[j + 1][0]
        return abs(area) * 0.5

    def largestTriangleArea(self, points: List[List[int]]) -> float:
        area = -1
        length = len(points)
        for i in range(0, length):
            for j in range(i+1, length):
                for k in range(j+1, length):
                    area = max(area, self.find_area([points[i],
                                                     points[j],
                                                     points[k]]))
        return area