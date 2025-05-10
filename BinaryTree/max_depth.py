# Definition for a binary tree node.
from typing import Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1


class BFSSolution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        q = deque()
        q.append(root)
        depth = 0
        while q:
            node_list = len(q)
            for i in range(node_list):
                cur = q.popleft()

                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
            # NOTE: the depth is incremented out side of the loop, because the loop is based on the lenght of ndoe at each level
            # This essentially goes through every element at each level
            depth += 1

        return depth


root = TreeNode(3, TreeNode(9, None, None),
                TreeNode(20, TreeNode(15), TreeNode(7)))

print(Solution().maxDepth(root))
