from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res=[]
        que=deque([root])
        while que:
            level=[]
            for _ in range(len(que)):
                node=que.popleft()
                level.append(node.val)
                if(node.left):
                    que.append(node.left)
                if(node.right):
                    que.append(node.right)
            res.append(level[-1])
        return res
