from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        s1=set(ransomNote)
        s2=set(magazine)
        if(s1.issubset(s2)):
            d1=dict(Counter(ransomNote))
            d2=dict(Counter(magazine))
            for i in d2:
                if i in d1 and d1[i]>d2[i]:
                    return False
            return True
        return False
