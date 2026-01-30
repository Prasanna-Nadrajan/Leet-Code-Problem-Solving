from collections import Counter
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        ans=0
        rows=Counter(tuple(row) for row in grid)
        columns=Counter(tuple([grid[i][j] for i in range(len(grid))]) for j in range(len(grid)))
        for key1 in rows:
            for key2 in columns:
                if(key1==key2):
                    ans+=(rows[key1]*columns[key2])
        return ans
