class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        i=0
        cond=False
        temp=[]
        remp=[]
        if(not nums):
            return nums
        while(i<len(nums)-1):
            temp.append(nums[i])
            if(nums[i+1]-nums[i]!=1):
                remp.append(temp)
                temp=[]
                
                cond=True
            else:
                cond=False
            i+=1
        if(cond):
            remp.append([nums[-1]])
        else:
            temp.append(nums[-1])
            remp.append(temp)
        res=[]
        for i in remp:
            if len(i)>1:
                res.append(f"{i[0]}->{i[-1]}")
            else:
                res.append(f"{i[0]}")
        return(res)
