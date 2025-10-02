class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        fulls=numBottles
        emp=0
        c=0
        while(fulls!=0):
            c+=fulls
            emp+=fulls
            fulls=0
            while(emp>=numExchange):
                fulls+=1
                emp-=numExchange
                numExchange+=1
        return(c)
