class Solution:
    def convertToBase7(self, num: int) -> str:
        t=abs(num)
        v=''
        while(t>=7):
            v+=str(t%7)
            t//=7
        v+=str(t)
        l=list(v)
        l.reverse()
        v=('-' if num<0 else '') + "".join(l)
        return(v)
