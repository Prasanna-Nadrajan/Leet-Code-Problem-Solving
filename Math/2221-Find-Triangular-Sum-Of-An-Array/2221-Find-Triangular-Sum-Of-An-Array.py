import numpy as np

class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        def getMod10(n, k):            
            fast5 = [
                [1, 0, 0, 0, 0],
                [1, 1, 0, 0, 0],
                [1, 2, 1, 0, 0],
                [1, 3, 3, 1, 0],
                [1, 4, 1, 4, 1]
            ]
            
            sunzi = [
                [0, 6, 2, 8, 4],
                [5, 1, 7, 3, 9]
            ]
            
            nBit = bin(n)[2:]
            kBit = bin(k)[2:].zfill(len(nBit))
            
            n5 = np.base_repr(n, 5)
            k5 = np.base_repr(k, 5).zfill(len(n5))
            
            mod2 = 1
            for i in range(len(nBit) - 1, -1, -1):
                if kBit[i] == '1' and nBit[i] == '0':
                    mod2 = 0
                    break
            
            mod5 = 1
            for i in range(len(n5)):
                mod5 *= fast5[int(n5[i])][int(k5[i])]
                mod5 %= 5
            
            return sunzi[mod2][mod5]
        
        n = len(nums) - 1
        total = 0
        
        for k in range(n + 1):
            coeff = getMod10(n, k)
            total += coeff * nums[k]
            total %= 10
        
        return total
