# Definition for a binary tree node.

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res_list = []

        def dfs(node):
            nonlocal res_list
            if not node:
                return

            if len(res_list) == k:
                return

            dfs(node.left)
            res_list.append(node.val)
            if len(res_list) < k:
                dfs(node.right)
        dfs(root)
        return res_list[k-1]

#  NOTE: use a counter and a variable to repalce List


class LessSpaceSolution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.k = k
        self.ans = None

        def inorder(node):
            if not node or self.k == 0:
                return
            inorder(node.left)
            self.k -= 1
            if self.k == 0:
                self.ans = node.val
                return
            inorder(node.right)

        inorder(root)
        return self.ans
