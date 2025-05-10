# Definition for a binary tree node.
from typing import Optional

# NOTE: the key in this question is to find the splitting point where these two nodes belongs to different subtree.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if root.val == p.val or root.val == q.val:
            return root

        if p.val < root.val:
            if q.val < root.val:
                return self.lowestCommonAncestor(root.left, p, q)
            else:
                return root
        else:
            if q.val > root.val:
                return self.lowestCommonAncestor(root.right, p, q)
            else:
                return root
