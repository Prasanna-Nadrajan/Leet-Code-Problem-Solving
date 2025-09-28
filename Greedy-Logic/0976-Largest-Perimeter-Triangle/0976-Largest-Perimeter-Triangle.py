class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        for k in range(2,len(nums)):
            i,j=k-2,k-1
            if(nums[k]+nums[j]>nums[i]):
                return nums[i]+nums[j]+nums[k]
        return 0
