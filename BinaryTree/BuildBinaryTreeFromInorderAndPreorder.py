# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class WrongSolution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        self.length = len(inorder)
        pivot_idx = 0
        for i in range(self.length):
            if inorder[i] == preorder[0]:
                pivot_idx = i

        def construct_node(inorder, index):
            if index < 0 or index > len(inorder) - 1:
                return None
            else:
                left = index // 2
                right = (len(inorder) - 1 - index) // 2
                return TreeNode(inorder[index], construct_node(inorder, left), construct_node(inorder, right))

        return construct_node(inorder, pivot_idx)

# O(n2)


class DFSSolution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1: mid + 1], inorder[:mid])
        root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])
        return root
