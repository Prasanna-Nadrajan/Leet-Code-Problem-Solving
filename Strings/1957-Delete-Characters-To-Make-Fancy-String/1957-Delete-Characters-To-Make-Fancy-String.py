class Solution:
    def makeFancyString(self, s: str) -> str:
        temp=''
        if(len(s)!=1):
            temp=s[0]
        for i in range(1,len(s)-1):
            if(s[i-1]==s[i] and s[i]==s[i+1]):
                continue
            else:
                temp+=s[i]
        temp+=s[-1]
        return(temp)
