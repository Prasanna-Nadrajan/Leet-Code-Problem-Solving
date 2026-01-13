class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        j=k
        vowels='AEIOUaeiou'
        print(s[:k])
        c=sum(1 if c in vowels else 0 for c in s[:k])
        cc=c
        for i in range(1,len(s)-k+1):
            if s[i-1] in vowels:
                cc-=1
            if s[i+k-1] in vowels:
                cc+=1
            c=max(cc,c)
        return c
