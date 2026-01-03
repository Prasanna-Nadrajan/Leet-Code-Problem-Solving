class Solution:
    def numOfWays(self, n: int) -> int:
        MOD = 10**9 + 7
        A, B = 6, 6  
        for _ in range(2, n + 1):
            nextA = (3 * A + 2 * B) % MOD
            nextB = (2 * A + 2 * B) % MOD
            A, B = nextA, nextB
        
        return (A + B) % MOD
