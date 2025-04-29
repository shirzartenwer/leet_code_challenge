# https://neetcode.io/problems/search-2d-matrix

# NOTE: this asks for a solution that's O(log(m*n)), m is row number, n is column number

from typing import List

# my solution that's O(m*log(n))


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        column = len(matrix[0])

        k = 0
        while k < row:
            l = 0
            r = column - 1
            if target > matrix[k][r]:
                k = k+1
                continue
            else:
                while l <= r:
                    middle = (l+r) // 2

                    if target == matrix[k][middle]:
                        return True
                    elif target > matrix[k][middle]:
                        l = middle + 1
                    else:
                        r = middle - 1
                k += 1
        return False

# actually O(log(m+n)) means O(log(m) + log(n)), which means two binary search


class TBSSolution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])

        top, bot = 0, ROWS - 1
        while top <= bot:
            row = (top + bot) // 2
            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bot = row - 1
            else:
                break

        if not (top <= bot):
            return False
        row = (top + bot) // 2
        l, r = 0, COLS - 1
        while l <= r:
            m = (l + r) // 2
            if target > matrix[row][m]:
                l = m + 1
            elif target < matrix[row][m]:
                r = m - 1
            else:
                return True
        return False
