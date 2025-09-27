class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        i=0
        max_area=0
        area=0
        while(i<len(points)-2):
            j=i+1
            while(j<len(points)-1):
                k=j+1
                while(k<len(points)):
                    p1=points[i]
                    p2=points[j]
                    p3=points[k]
                    area=0.5*abs(p1[0]*(p2[1]-p3[1])+p2[0]*(p3[1]-p1[1])+p3[0]*(p1[1]-p2[1]))
                    max_area=max(max_area,area)  
                    k+=1 
                j+=1
            i+=1
        return(max_area)
