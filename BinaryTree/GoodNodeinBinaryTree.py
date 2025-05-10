# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class OneSolution:
    def goodNodes(self, root: TreeNode) -> int:
        max_val = root.val
        num_good = 0

        def dfs(node, max_val):
            if not node:
                return 0

            num_good = 1 if node.val >= max_val else 0
            max_val = max(node.val, max_val)

            num_good += dfs(node.left, max_val)
            num_good += dfs(node.right, max_val)
            return num_good

        return dfs(root, max_val)


root = TreeNode(2, TreeNode(1, TreeNode(3, None, None), None), TreeNode(
    1, TreeNode(1, None, None), TreeNode(5, None, None)))

OneSolution.goodNodes(root)


class SecSolution:
    def goodNodes(self, root: TreeNode) -> int:
        max_val = root.val
        num_good = 0

        def dfs(node, max_val):
            # NOTE: declare non local variables to keep giving access to num_good globally to the sub funcitons.
            nonlocal num_good
            if not node:
                return 0

            if node.val >= max_val:
                max_val = node.val
                num_good += 1

            dfs(node.left, max_val)
            dfs(node.right, max_val)

        dfs(root, max_val)

        return num_good
