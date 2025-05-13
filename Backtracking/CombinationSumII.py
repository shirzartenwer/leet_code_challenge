from typing import List

# NOTE: always think about back tracking as going through levels of decision tree
# each DFS is going down to a subtree by choosing one branch
# each for loop is options at the same level of trees


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def dfs(start: int, cur: List[int], total: int):
            # 1) did we hit the target?
            if total == target:
                res.append(cur.copy())
                return

            prev = None         # for skipping duplicates at this level
            for j in range(start, len(candidates)):
                # a) prune if sum too large
                if total + candidates[j] > target:
                    break

                # b) skip same value as previous at this tree-level
                if prev is not None and candidates[j] == prev:
                    continue

                # c) choose index j
                cur.append(candidates[j])

                # d) recurse, next start is j+1 so we never reuse j
                dfs(j+1, cur, total + candidates[j])

                # e) backtrack both the value and the index
                cur.pop()

                # f) remember this value so any further equal ones get skipped
                prev = candidates[j]

        # kick off with nothing chosen
        dfs(0, [], 0)
        return res


print(Solution().combinationSum2([1, 1, 2], 2))
