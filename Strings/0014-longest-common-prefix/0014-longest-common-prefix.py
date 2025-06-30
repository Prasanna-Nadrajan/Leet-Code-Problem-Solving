class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res=''
        al=list(zip(*strs))
        if not al:
            return ''
        al=list(map(list,map(set,al)))
        i=0
        while( i<len(al) and len(al[i])==1):
            res+=al[i][0]
            i+=1
        return(res)
