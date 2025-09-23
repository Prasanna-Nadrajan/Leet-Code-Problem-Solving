class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        def correct(s):
            if s[0]=="0":
                while s[0]=="0":
                    s=s[1::]
                    if not s:
                        return "0"
            return s
        
        i=0
        j=0
        v1=version1.split(".")
        v2=version2.split(".")
        l1=len(v1)
        l2=len(v2)
        while(i<l1 or j<l2):
            le=int(correct(v1[i])) if i<l1 else 0
            re=int(correct(v2[j])) if j<l2 else 0
            if(le>re):
                return 1
            elif le<re:
                return -1
            i+=1
            j+=1
        return 0
