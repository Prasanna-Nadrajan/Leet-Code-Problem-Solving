  class Solution:
    def convert(self, s: str, numRows: int) -> str:
        ll=[]
        ii=0
        if numRows<=1:
            return s
        for i in range(numRows):
            ll.append([])

        for i in range(len(s)):
            if(ii==0):
                e=1
            elif(ii==numRows-1):
                e=-1
            ll[ii].append(s[i])
            ii+=e
        # print(ll)
        return "".join(["".join(i)for i in ll])
