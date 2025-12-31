class Solution:
    def reverseVowels(self, s: str) -> str:
        left=0
        right=len(s)-1
        vowels='AEIOUaeiou'
        s=list(s)
        while(left<=right):
            if(s[left] in vowels):
                if(s[right] in vowels):
                    s[left],s[right]=s[right],s[left]
                    left+=1
                right-=1
            else:
                left+=1
        return "".join(s)
