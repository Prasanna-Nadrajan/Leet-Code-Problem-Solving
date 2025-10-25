class Solution:
    def totalMoney(self, n: int) -> int:
        tn=n//7
        cost=0
        i=1
        j=7
        for k in range(tn):
            cost+=(3.5)*(i+j)
            i+=1
            j+=1
        rem=n%7
        for k in range(rem):
            cost+=i
            i+=1
        return(int(cost))
