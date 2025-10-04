class Solution:
    def maxArea(self, height: List[int]) -> int:
        c=0
        i=c
        max_area=0
        j=len(height)-1
    
        while(i<j):
            area=min(height[i],height[j])*(j-i)
            max_area=max(area,max_area)
            if(height[i]<height[j]):
                i+=1
            else:
                j-=1
        return(max_area)

