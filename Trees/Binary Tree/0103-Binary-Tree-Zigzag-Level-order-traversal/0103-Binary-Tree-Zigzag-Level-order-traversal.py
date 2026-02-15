from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res=[]
        queue=deque([root])
        while(queue):
            lvl=[]
            lvls=len(queue)
            for i in range(lvls):
                node=queue.popleft()
                lvl.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(lvl)
        for i in range(1,len(res),2):
            res[i]=res[i][::-1]
        return res
                    
