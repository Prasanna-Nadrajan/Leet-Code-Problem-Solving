class Solution:
    def romanToInt(self, s: str) -> int:
        if not s:
            return 0
        val=0
        t2=0
        rev=s[::-1]
        for i in rev:
            match i:
                case 'I':
                    t=1
                case 'V':
                    t=5
                case 'X':
                    t=10
                case 'L':
                    t=50
                case 'C':
                    t=100
                case 'D':
                    t=500
                case 'M':
                    t=1000
            if t>=t2:
                val+=t
            else:
                val-=t
            t2=t
        return(val)
