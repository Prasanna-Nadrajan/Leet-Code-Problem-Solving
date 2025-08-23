class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        g2=list(zip(*grid))
        t1=0
        t2=0
        t3=0
        t4=0
        for i in range(len(grid)):
            if sum(grid[i])>0:
                t1=i
                break

        for i in range(len(g2)):
            if(sum(g2[i])>0):
                t2=i
                break
   
        for i in range(len(grid)-1,-1,-1):
            if(sum(grid[i])>0):
                t3=i
                break
        
        for i in range(len(g2)-1,-1,-1):
            if(sum(g2[i])>0):
                t4=i
                break

        re=(t3-t1+1)*(t4-t2+1)
        
        return re
