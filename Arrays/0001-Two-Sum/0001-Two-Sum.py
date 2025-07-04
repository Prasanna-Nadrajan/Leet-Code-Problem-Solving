class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l=[]
        for i,num in enumerate(nums):
            comp=target-nums[i]
            if comp in nums and nums.index(comp)!=i:
                return [i,nums.index(comp)]
        return[]
        
