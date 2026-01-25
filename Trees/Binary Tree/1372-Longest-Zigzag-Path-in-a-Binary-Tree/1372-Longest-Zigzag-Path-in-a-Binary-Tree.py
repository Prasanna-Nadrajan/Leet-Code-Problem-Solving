# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.m=0
        def dfs(root):
            if not root:
                return -1,-1
            left=dfs(root.left)
            right=dfs(root.right)
            lp=1+left[1]
            rp=1+right[0]
            self.m=max(self.m,lp,rp)
            return (lp,rp)
        dfs(root)
        return self.m
