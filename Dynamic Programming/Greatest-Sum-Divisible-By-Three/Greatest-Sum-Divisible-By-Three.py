class Solution:
    def maxSumDivThree(self ,nums):
        total = sum(nums)
        rem1, rem2 = [], []
        for num in nums:
            if num % 3 == 1:
                rem1.append(num)
            elif num % 3 == 2:
                rem2.append(num)
        rem1.sort()
        rem2.sort()
        if total % 3 == 0:
            return total
        elif total % 3 == 1:
            option1 = total - rem1[0] if rem1 else 0
            option2 = total - sum(rem2[:2]) if len(rem2) >= 2 else 0
            return max(option1, option2)
        else: 
            option1 = total - rem2[0] if rem2 else 0
            option2 = total - sum(rem1[:2]) if len(rem1) >= 2 else 0
            return max(option1, option2)
