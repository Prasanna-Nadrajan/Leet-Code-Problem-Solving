# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:    
        t1=[]
        t2=[]
        def inorder(root,t):
            if(root!=None):
                if root.left==None and root.right==None:
                    t.append(root.val)
                inorder(root.left,t)
                inorder(root.right,t)
        inorder(root1,t1)
        inorder(root2,t2)
        return t1==t2
