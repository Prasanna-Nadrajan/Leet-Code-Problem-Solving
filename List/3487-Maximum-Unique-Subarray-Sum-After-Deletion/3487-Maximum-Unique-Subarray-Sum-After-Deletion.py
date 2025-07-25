class Solution:
    def maxSum(self, nums: List[int]) -> int:
        nn=list(set(nums))
        print(nn)
        nl=[]
        f=True
        for i in nn:
            if i>0:
                f=False
        if(f):
            return max(nn)
        for i in nn:
            if i>0:
                nl.append(i)
        return(sum(nl))
