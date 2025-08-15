from collections import defaultdict
class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        l=0
        max_len=0
        c=defaultdict(int)
        for r in range(len(fruits)):
            c[fruits[r]]+=1
            while(len(c)>2):
                c[fruits[l]]-=1
                if c[fruits[l]]==0:
                    del c[fruits[l]]
                l+=1

            max_len=max(max_len,r-l+1)
        return max_len
