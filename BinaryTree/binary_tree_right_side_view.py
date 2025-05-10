#  https://neetcode.io/problems/binary-tree-right-side-view


# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        q = deque([root])
        result = [root.val]
        while q:
            right_side = None
            length = len(q)
            for i in range(length):
                cur = q.popleft()

                # NOTE: the sequence of following two if is designed to preserve the right side value on each level
                # This is a smart way to automatically preserve the right side value, instead of needing to compare
                # existing all node on the same level to see which one is on the right side

                # Sequence of code is important!!!
                if cur.left:
                    right_side = cur.left
                    q.append(cur.left)

                if cur.right:
                    right_side = cur.right
                    q.append(cur.right)

            if right_side:
                result.append(right_side.val)

        return result
