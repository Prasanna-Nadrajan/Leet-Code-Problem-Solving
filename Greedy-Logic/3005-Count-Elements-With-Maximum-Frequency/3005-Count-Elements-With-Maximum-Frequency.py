from collections import Counter
class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        if(len(nums)<=1):
            return len(nums)
        d=dict(Counter(nums))
        # print(d)
        dl=list(d.values())
        res=dl.count(max(dl))*max(dl)
        return(res)
