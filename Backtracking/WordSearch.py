from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n_row, n_col = len(board), len(board[0])
        self.found = False

        def dfs_search(board, i, j, start, word):

            if not board[i][j] == word[start]:
                return

            if start == len(word)-1:
                self.found = True
                return

            self.visited[i][j] = True

            if i+1 < n_row and not self.visited[i+1][j]:
                dfs_search(board, i+1, j, start+1, word)


            if i-1 >= 0 and not self.visited[i-1][j]:
                dfs_search(board, i-1, j, start+1, word)

            if j+1 < n_col and not self.visited[i][j+1]:
                dfs_search(board, i, j+1, start+1, word)


            if j-1 >= 0 and not self.visited[i][j-1]:
                dfs_search(board, i, j-1, start+1, word)

            self.visited[i][j] = False

        for i in range(n_row):
            for j in range(n_col):
                if not self.found:
                    self.visited = [
                        [False for _ in range(n_col)] for _ in range(n_row)]
                    dfs_search(board, i, j, 0, word)
                else:
                    break

        return self.found


# print(Solution().exist([["A", "B", "C", "D"], [
#       "S", "A", "A", "T"], ["A", "C", "A", "E"]], "CAT"))

print(Solution().exist([["A", "B", "C", "E"], [
      "S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCCED"))
