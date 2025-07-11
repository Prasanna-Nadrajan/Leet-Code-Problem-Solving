class Solution:
    def climbStairs(self, n: int) -> int:
        if n<=0:
            return 0
        elif n==1 or n==2 or n==3:
            return n
        else:
            c=3
            l1,l2,l3=1,2,3
            while(c!=n):
                temp=l2
                l2,l3=l3,l3+temp
                c+=1
            return l3
