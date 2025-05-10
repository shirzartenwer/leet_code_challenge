# Same binary tree
# Definition for a binary tree node.
from typing import Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Commmon operaiont to see if the tree is the same
# https://neetcode.io/problems/same-binary-tree
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if p and q and p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        else:
            return False


# Subtree of antother tree
#  https://neetcode.io/problems/subtree-of-a-binary-tree
class Solution:
    def check_subtree(self, node_1: TreeNode, node_2: TreeNode):
        if not node_1 and not node_2:
            return True
        if node_1 and node_2 and node_1.val == node_2.val:
            return self.check_subtree(node_1.left, node_2.left) and self.check_subtree(node_1.right, node_2.right)

        else:
            return False

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        q = deque()
        q.append(root)
        result = []
        while q:
            len_q = len(q)
            for i in range(len_q):
                cur = q.popleft()
                if cur.val == subRoot.val:
                    result.append(self.check_subtree(cur, subRoot))

                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)

        if result:
            return any(result)
        else:
            return False


#  Balanced Tree
#  https://neetcode.io/problems/balanced-binary-tree
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def dfs(node: Optional[TreeNode]):
            if not node:
                return [True, 0]

            left, right = dfs(node.left), dfs(node.right)
            all_balanced = left[0] and right[0] and abs(
                left[1] - right[1]) <= 1

            return [all_balanced, 1+max(left[1], right[1])]

        return dfs(root)[0]


# Maximum depth of binary tree: most basic BFS
#  https://neetcode.io/problems/depth-of-binary-tree
class Solution:
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
            depth += 1

        return depth


# Diameter of Binary Tree
# https://neetcode.io/problems/binary-tree-diameter
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0

        def dfs(node):
            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            # Update the diameter at this node
            self.diameter = max(self.diameter, left + right)
            # Return the depth
            return 1 + max(left, right)

        dfs(root)
        return self.diameter
