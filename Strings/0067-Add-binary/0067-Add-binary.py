from itertools import zip_longest

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry=0
        res=[]

        for x,y in zip_longest(reversed(a),reversed(b),fillvalue='0'):
            tot=int(x)+int(y)+carry
            res.append(str(tot%2))
            carry=tot//2
        
        if carry:
            res.append(str(carry))
        
        return "".join(reversed(res))
