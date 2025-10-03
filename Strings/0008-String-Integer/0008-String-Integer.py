class Solution:
    def myAtoi(self, s: str) -> int:
        s=s.strip()
        num=""
        is_negative=False
        is_positive=False
        for i in s:
            if(not i.isdigit()):
                if(i=='-'):
                    if(is_positive or is_negative):
                        break
                    if(s.index(i)==0):
                        is_negative=True
                        continue
                elif(i=='+'):
                    if(is_negative or is_positive):
                        break
                    if(s.index(i)==0):
                        is_positive=True
                        continue
                break
            else:
                num+=i
        if num:
            num=int(num)
            if is_negative:
                num=-1*(num)
                if(num<(-2**31)):
                    return -2**31
            if(num>2**31-1):
                return 2**31-1
            return int(num)
        else:
            return 0
