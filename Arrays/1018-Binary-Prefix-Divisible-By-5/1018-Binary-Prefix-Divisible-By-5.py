class Solution:
    
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        res=[]
        p_mod=0
        for i in nums:
            p_mod=(2*p_mod+i)%5
            res.append(p_mod==0)
        return res
