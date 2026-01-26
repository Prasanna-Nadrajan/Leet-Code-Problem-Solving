from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic=dict(Counter(nums))
        dic=sorted(dic,key=lambda x:dic[x])
        return dic[-1]
