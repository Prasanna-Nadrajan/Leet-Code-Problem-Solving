import math
class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        if(len(nums)==1):
            return nums
        stack=[]

        for num in nums:
            while stack:
                top=stack[-1]
                if(math.gcd(top,num)>1):
                    num=math.lcm(top,num)
                    stack.pop()
                else:
                    break
            stack.append(num)    
        return stack
