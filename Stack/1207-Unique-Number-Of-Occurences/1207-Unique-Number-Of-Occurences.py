from collections import Counter
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        c=dict(Counter(arr))
        a=list(c.values())
        for i in a:
            if(a.count(i)!=1):
                return False
        return True
