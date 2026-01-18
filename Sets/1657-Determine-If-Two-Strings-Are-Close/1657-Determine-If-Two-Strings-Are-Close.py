from collections import Counter
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1)==len(word2):
            c1=dict(Counter(word1))
            c2=dict(Counter(word2))
            s1=c1.keys()
            s2=c2.keys()
            v1=sorted(c1.values())
            v2=sorted(c2.values())
            if(s1==s2 and v1==v2):
                return True
        return False
