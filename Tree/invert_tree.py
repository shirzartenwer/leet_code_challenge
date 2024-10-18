# Definition for a binary tree node.
# https://leetcode.com/problems/invert-binary-tree/?envType=study-plan-v2&envId=top-interview-150

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def invert_tree(root: TreeNode):
    if root.left == None and root.right == None:
        return root
    else:
        holder = root.right
        root.right = root.left
        root.left = holder
        invert_tree(root.left)
        invert_tree(root.right)
    return root
