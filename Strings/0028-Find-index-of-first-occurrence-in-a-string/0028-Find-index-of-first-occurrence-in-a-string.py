class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        try:
            val=haystack.find(needle)
        except ValueError:
            return -1
        else:
            return val
