class Solution:
    def hasSameDigits(self, s: str) -> bool:
        while(len(s)>2):
            st=""
            for i in range(len(s)-1):
                st+=str((int(s[i])+int(s[i+1]))%10)
            s=st
        return(s[0]==s[1])

