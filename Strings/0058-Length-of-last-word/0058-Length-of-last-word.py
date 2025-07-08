class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s=s.strip()
        s=s.split()
        l=s[-1]
        return len(l)
