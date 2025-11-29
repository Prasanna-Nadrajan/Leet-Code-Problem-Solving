class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        s=sum(nums)
        c=0
        while(s%k!=0):
            c+=1
            s-=1
        return c
