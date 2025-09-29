class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        from functools import lru_cache
        @lru_cache(None)
        
        def dp(i,j):
            if(j-i<2):
                return 0
            min_score=float('inf')
            for k in range(i+1,j):
                score=dp(i,k)+dp(k,j)+(values[i]*values[k]*values[j])
                min_score=min(min_score,score)
            return min_score
        
        return dp(0,len(values)-1)
