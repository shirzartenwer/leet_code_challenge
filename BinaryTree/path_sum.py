# https://leetcode.com/problems/path-sum/description/
from typing import Optional
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Recursion


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False

        if root.left is None and root.right is None:
            return root.val == targetSum

        return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum - root.val)

# DFS


class SolutionDFS:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False

        search_queue = [(root, 0)]
        while search_queue:
            node, node_sum = search_queue.pop()
            node_sum += node.val

            if node.left is not None:
                search_queue.append((node.left, node_sum))

            if node.right is not None:
                search_queue.append((node.right, node_sum))

            if node.left is None and node.right is None and node_sum == targetSum:
                return True

        return False


# case 1
#  [5,4,8,11,null,13,4,7,2,null,null,null,1]
root = TreeNode(5, TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2)), None),
                TreeNode(8, TreeNode(13), TreeNode(4, None, TreeNode(1))))
targetSum = 22

print(SolutionDFS().hasPathSum(root, targetSum))
