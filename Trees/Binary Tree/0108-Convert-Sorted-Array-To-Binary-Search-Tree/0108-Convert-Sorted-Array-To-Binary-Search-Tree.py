# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def join(self,start,end,nums:List[int]):
        if(start<=end):
            mid=(start+end)//2
            root=TreeNode(nums[mid])
            root.left=self.join(start,mid-1,nums)
            root.right=self.join(mid+1,end,nums)
            return root
        return None

    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        root=self.join(0,len(nums)-1,nums)
        return root


