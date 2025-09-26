class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        def check(a,b,c):
            return a+b>c and a+c>b and b+c>a

        if len(nums)<3:
            return 0
        nums.sort()
        count=0

        for k in range(2,len(nums)):
            i,j=0,k-1
            while(i<j):
                if(nums[i]+nums[j]>nums[k]):
                    count+=j-i
                    j-=1
                else:
                    i+=1

        return count
