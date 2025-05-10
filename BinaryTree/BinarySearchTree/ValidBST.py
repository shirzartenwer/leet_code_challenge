# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(node, left, right):
            if not node:
                return True
            if not (left < node.val < right):
                return False

            return valid(node.left, left, node.val) and valid(
                node.right, node.val, right
            )

        return valid(root, float("-inf"), float("inf"))


root = TreeNode(5, TreeNode(3, TreeNode(1, None, TreeNode(2, None, None)), TreeNode(
    4, None, None)), TreeNode(8, TreeNode(7, None, None), TreeNode(9, None, None)))

print(Solution().isValidBST(root))

#  NOTE: when checking if tree is binary, to think about boundary condition of each node:
# when thinking about how to deduct left boundary condition, think about node that's on the right
# when thinking about the right boundary condition, think about the node that's on the left.
#  It's not sufficient to guarantee left childiren is smaller than node, and right children is bigger than node.
# Because in the follwoing sub trees, EVERY NODE on the left needs to be smaller than the root tree,
# but they could be bigger than their parent node, if they are on the right side of their parent node
