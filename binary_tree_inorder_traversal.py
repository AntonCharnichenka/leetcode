# https://leetcode.com/problems/binary-tree-inorder-traversal/


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: TreeNode | None) -> list[int]:
        result: list[int] = []

        def rec_inorder_traversal(node: TreeNode | None) -> None:
            if node is None:
                return

            rec_inorder_traversal(node.left)
            result.append(node.val)
            rec_inorder_traversal(node.right)

        rec_inorder_traversal(root)

        return result


TREE = TreeNode(
    val=1,
    left=None,
    right=TreeNode(val=2, left=TreeNode(val=3, left=None, right=None), right=None),
)

assert Solution().inorderTraversal(TREE) == [1, 3, 2]
