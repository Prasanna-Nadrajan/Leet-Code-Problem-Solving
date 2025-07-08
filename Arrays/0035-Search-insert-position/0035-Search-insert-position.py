class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        try:
            pos=nums.index(target)
        except ValueError:
            tail=len(nums)-1
            while(tail>=0 and nums[tail]>target):
                tail-=1
            return tail+1
        else:
            return pos
