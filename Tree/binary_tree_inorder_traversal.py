# https://leetcode.com/problems/binary-tree-inorder-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.traversal = []
        
    def dfs(self,node):
        if node.left:
            self.dfs(node.left)
        self.traversal.append(node.val)
        if node.right:
            self.dfs(node.right)
    
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if root:
            self.dfs(root)
        return self.traversal