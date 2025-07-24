from collections import Counter

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        cc=dict(Counter(nums))
        cc=sorted(cc,key=lambda x:cc[x])
        return(cc[0])
