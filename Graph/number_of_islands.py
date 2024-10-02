from typing import List
from collections import deque


# TODO: try to recap and understand that MySolution turned out to be better than the RevisedChatGPTSolution,
# because using one more Island set actually made it faster

class MySolution:
    def numIslands(self, grid: List[List[str]]) -> int:
        island_count = 0
        searched = set()
        island = set()
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] != "0" and (i, j) not in searched:
                    search_queue = [(i, j)]

                    while search_queue:
                        cell = search_queue.pop(0)
                        searched.add(cell)
                        x, y = cell
                        if cell not in island:
                            island_count += 1
                            island.add(cell)
                        if x+1 <= len(grid)-1 and grid[x+1][y] == "1" and (x+1, y) not in island:
                            island.add((x+1, y))
                            search_queue.append((x+1, y))
                        if y+1 <= len(grid[0])-1 and grid[x][y+1] == "1" and (x, y+1) not in island:
                            island.add((x, y+1))
                            search_queue.append((x, y+1))
                        if x-1 >= 0 and grid[x-1][y] == "1" and (x-1, y) not in island:
                            island.add((x-1, y))
                            search_queue.append((x-1, y))
                        if y-1 >= 0 and grid[x][y-1] == "1" and (x, y-1) not in island:
                            island.add((x, y-1))
                            search_queue.append((x, y-1))

                    else:
                        continue
        print("The sum of i and j is", i+j)
        return island_count


class RevisedChatGPTSolution:
    def numIslands(self, grid: List[List[str]]) -> int:
        island_count = 0
        searched = set()

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1' and (i, j) not in searched:
                    # Initialize search queue for this new island
                    search_queue = [(i, j)]
                    island_count += 1  # Increment the island count at the start of a new island search

                    while search_queue:
                        cell = search_queue.pop(0)
                        searched.add(cell)
                        x, y = cell

                        # Check neighbors with boundary checks
                        if x + 1 < len(grid) and grid[x + 1][y] == "1" and (x + 1, y) not in searched:
                            search_queue.append((x + 1, y))
                        if y + 1 < len(grid[0]) and grid[x][y + 1] == "1" and (x, y + 1) not in searched:
                            search_queue.append((x, y + 1))
                        if x - 1 >= 0 and grid[x - 1][y] == "1" and (x - 1, y) not in searched:
                            search_queue.append((x - 1, y))
                        if y - 1 >= 0 and grid[x][y - 1] == "1" and (x, y - 1) not in searched:
                            search_queue.append((x, y - 1))

        return island_count


class ChatGPTSolution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        island_count = 0
        rows, cols = len(grid), len(grid[0])

        def bfs(i, j):
            queue = deque([(i, j)])
            # Mark the starting cell as visited by setting it to "0"
            grid[i][j] = "0"

            while queue:
                x, y = queue.popleft()

                # Check all four possible directions (down, right, up, left)
                for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                    nx, ny = x + dx, y + dy

                    if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == "1":
                        queue.append((nx, ny))
                        grid[nx][ny] = "0"  # Mark as visited

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    island_count += 1
                    bfs(i, j)

        return island_count


# case 1
# print(Solution().numIslands([["1", "1", "1", "1", "0"],
#                              ["1", "1", "0", "1", "0"],
#                              ["1", "1", "0", "0", "0"],
#                              ["0", "0", "0", "0", "0"]]))

#  case 2
# print(ChatGPTSolution().numIslands([["1", "1", "0", "0", "0"],
#                                     ["1", "1", "0", "0", "0"],
#                                     ["0", "0", "1", "0", "0"],
#                                     ["0", "0", "0", "1", "1"]]))
#  case 3
# print(MySolution().numIslands([["1", "1", "1"],
#                                ["0", "1", "0"],
#                                ["1", "1", "1"]]))
# case 4
print(MySolution().numIslands([["0", "0", "0", "0", "0", "0", "1"]]))
