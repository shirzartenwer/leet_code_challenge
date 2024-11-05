# https://leetcode.com/problems/sum-root-to-leaf-numbers/?envType=study-plan-v2&envId=top-interview-150


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        stack = [(root, 0)]
        ans = 0
        while stack:
            cur, path_sum = stack.pop()
            path_sum = path_sum*10+cur.val
            # leaf
            if not cur.left and not cur.right:
                ans += path_sum

            if cur.left:
                stack.append((cur.left, path_sum))
            if cur.right:
                stack.append((cur.right, path_sum))

        return ans


root_1 = TreeNode(1, TreeNode(2, None, None), TreeNode(3, None, None))
root_2 = TreeNode(4, TreeNode(9, 5, 1), TreeNode(0, None, None))


print(Solution().sumNumbers(root_1))
