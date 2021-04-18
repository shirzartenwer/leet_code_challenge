'''You are given an array points where points[i] = [xi, yi] is the coordinates of the ith point on a 2D plane. Multiple points can have the same coordinates.

You are also given an array queries where queries[j] = [xj, yj, rj] describes a circle centered at (xj, yj) with a radius of rj.

For each query queries[j], compute the number of points inside the jth circle. Points on the border of the circle are considered inside.

Return an array answer, where answer[j] is the answer to the jth query.

'''
from typing import *


# Brute force
class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        result_list = []
        for j in queries:
            count = 0
            for n in points:
                if (n[0]-j[0])**2 + (n[1]-j[1])**2 <= j[2]**2:
                    count +=1
                
            result_list.append(count)
            
        return result_list
                