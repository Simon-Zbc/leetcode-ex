from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

## Runtime 33.3%
## Memory 82.5%
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        res = 0

        def dfs(root, direction):
            nonlocal res
            if not root:
                return 0
            left = dfs(root.left, 'l')
            right = dfs(root.right, 'r')
            res = max(res, left, right)
            return right + 1 if direction == 'l' else left + 1
        
        if not root:
            return 0
        dfs(root, 'l')
        dfs(root, 'r')
        return res