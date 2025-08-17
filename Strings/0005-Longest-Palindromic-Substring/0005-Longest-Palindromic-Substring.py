class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left+1:right]

        longest = ""
        for i in range(len(s)):
            p1 = expand(i, i)
            p2 = expand(i, i+1)
            longest = max(longest, p1, p2, key=len)
        return longest
