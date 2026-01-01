class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        m=max(candies)
        results=[]
        for i in candies:
            if i+extraCandies>=m:
                results.append(True)
            else:
                results.append(False)
        return results
