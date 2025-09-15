class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        tt=text.split()
        t=[1]*len(tt)
        for i in brokenLetters:
            for j in range(len(tt)):
                if i in tt[j]:
                    t[j]=0
        return sum(t)
