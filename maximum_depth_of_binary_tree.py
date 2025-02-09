# https://leetcode.com/problems/maximum-depth-of-binary-tree/


class TreeNode:
    def __init__(
        self,
        val: int = 0,
        left: 'TreeNode | None' = None,
        right: 'TreeNode | None' = None,
    ) -> None:
        self.val = val
        self.left = left
        self.right = right


class RecursiveDfsSolution:
    def maxDepth(self, root: TreeNode | None) -> int:
        def _(node: TreeNode | None) -> int:
            if node is None:
                return 0

            return 1 + max(_(node.left), _(node.right))

        return _(root)


class IterativeBfsSolution:
    def maxDepth(self, root: TreeNode | None) -> int:
        if not root:
            return 0

        level = 0
        import collections
        q = collections.deque([root])
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                
            level += 1
        
        return level


class IterativeDfsSolution:
    def maxDepth(self, root: TreeNode | None) -> int:
        result = 0
        stack = [[root, 1]]
        while stack:
            node, depth = stack.pop()
            if node:
                result = max(result, depth)
                stack.append([node.left, depth + 1])
                stack.append([node.right, depth + 1])
        
        return result
