# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def findMin(root):
            while root.left:
                root=root.left
            return root.val

        if root is None:
            return None
        else:
            if root.val>key:
                root.left = self.deleteNode(root.left,key)
            elif root.val<key:
                root.right = self.deleteNode(root.right,key)
            else:
                if root.left==None:
                    root=root.right
                elif root.right==None:
                    root=root.left
                else:
                    minval=findMin(root.right)
                    root.val=minval
                    root.right = self.deleteNode(root.right,minval)
            return root
