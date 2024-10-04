from typing import List
from collections import deque

# TODO: I didn't exlucde the "O"s that are vertically or horizontally connected to the "O"s on the boundary.


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        searched = set()
        region = set()

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "O" and 0 < i < len(board)-1 and 0 < j < len(board[0]) - 1 and (i, j) not in searched:
                    search_queue = deque([(i, j)])
                    region.add((i, j))
                    searched.add((i, j))

                    while search_queue:
                        x, y = search_queue.popleft()

                        if 0 < x+1 < len(board)-1 and board[x+1][y] == "O" and (x+1, y) not in region:
                            region.add((x+1, y))
                            search_queue.append((x+1, y))

                        if 0 < x-1 < len(board)-1 and board[x-1][y] == "O" and (x-1, y) not in region:
                            region.add((x-1, y))
                            search_queue.append((x-1, y))

                        if 0 < y+1 < len(board[0])-1 and board[x][y+1] == "O" and (x, y+1) not in region:
                            region.add((x, y+1))
                            search_queue.append((x, y+1))

                        if 0 < y-1 < len(board[0])-1 and board[x][y+1] == "O" and (x, y-1) not in region:
                            region.add((x, y-1))
                            search_queue.append((x, y-1))

        for element in region:
            print(element)
            x, y = element
            board[x][y] = "X"


class RevisedChatGPTSolution:
    def solve(self, board: List[List[str]]) -> None:
        if not board:
            return

        rows, cols = len(board), len(board[0])
        queue = deque()

        # Add all 'O's on the boundary to the queue
        for i in range(rows):
            if board[i][0] == "O":
                queue.append((i, 0))
            if board[i][cols - 1] == "O":
                queue.append((i, cols - 1))
        for j in range(cols):
            if board[0][j] == "O":
                queue.append((0, j))
            if board[rows - 1][j] == "O":
                queue.append((rows - 1, j))

        # Perform BFS to mark all 'O's connected to the boundary
        while queue:
            x, y = queue.popleft()
            if 0 <= x < rows and 0 <= y < cols and board[x][y] == "O":
                board[x][y] = "B"  # Mark the boundary-connected regions as 'B'
                # Add adjacent cells to the queue
                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    queue.append((x + dx, y + dy))

        # Flip all remaining 'O's to 'X' and 'B' back to 'O'
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "B":
                    board[i][j] = "O"


# case 1
# print(RevisedChatGPTSolution().solve([["X", "X", "X", "X"],
#                                       ["X", "O", "O", "X"],
#                                       ["X", "X", "O", "X"],
#                                       ["X", "O", "X", "X"]]))

# case2
print(RevisedChatGPTSolution().solve(
    [["O", "O", "O"],
     ["O", "O", "O"],
     ["O", "O", "O"]]))
