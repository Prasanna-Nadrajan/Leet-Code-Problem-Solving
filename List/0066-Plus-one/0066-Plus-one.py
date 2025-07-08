class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num=int("".join(list(map(str,digits))))
        num+=1
        num=str(num)
        return list(map(int,num))
