class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l=0
        s=len(nums)-1
        k=len(nums)
        while(l<len(nums)):
            if(nums[l]==val):
                while(s>0 and nums[s]==val):
                    s-=1
                nums[l]=nums[s]
                s-=1
                k-=1
            l+=1
        return k
        
