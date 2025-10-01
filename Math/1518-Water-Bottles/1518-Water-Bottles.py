class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        count=int(numBottles+((numBottles-1)/(numExchange-1)))
        return(count)
