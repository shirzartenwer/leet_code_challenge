from typing import List
from collections import deque


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        island_count = 0
        i = 0
        j = 0
        search_queue = []
        search_queue.append((i, j))
        searched = set()
        island = set()
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if len(search_queue) != 0:
                    cell = search_queue.pop(0)
                    if not cell in searched:
                        searched.add(cell)
                        x, y = cell
                        if grid[x][y] == "0":
                            continue
                        else:
                            if cell not in island:
                                island_count += 1
                                island.add(cell)
                            if x+1 <= len(grid)-1 and grid[x+1][y] == "1":
                                island.add((cell[0]+1, cell[1]))
                                search_queue.append((cell[0]+1, cell[1]))
                            if y+1 <= len(grid[0]) and grid[x][y+1] == "1":
                                island.add((cell[0], cell[1]+1))
                                search_queue.append((cell[0], cell[1]+1))
                    else:
                        continue
                else:
                    continue
        return island_count


# case 1
print(Solution().numIslands([["1", "1", "1", "1", "0"],
                             ["1", "1", "0", "1", "0"],
                             ["1", "1", "0", "0", "0"],
                             ["0", "0", "0", "0", "0"]]))

#  case 2
print(Solution().numIslands([["1", "1", "0", "0", "0"],
                             ["1", "1", "0", "0", "0"],
                             ["0", "0", "1", "0", "0"],
                             ["0", "0", "0", "1", "1"]]))
