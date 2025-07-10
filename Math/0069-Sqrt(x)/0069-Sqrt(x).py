import math
class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        n = x
        while (n**2) > x:
            n = (n + x // n)//2
        return n

