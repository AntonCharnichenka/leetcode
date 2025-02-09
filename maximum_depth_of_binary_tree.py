# https://leetcode.com/problems/maximum-depth-of-binary-tree/


class TreeNode:
    def __init__(
        self,
        val: int = 0,
        left: "TreeNode" | None = None,
        right: "TreeNode" | None = None,
    ) -> None:
        self.val = val
        self.left = left
        self.right = right


class RecursiveSolution:
    def maxDepth(self, root: TreeNode | None) -> int:
        def f(node: TreeNode | None) -> int:
            if node is None:
                return 0

            return 1 + max(f(node.left), f(node.right))

        return f(root)
