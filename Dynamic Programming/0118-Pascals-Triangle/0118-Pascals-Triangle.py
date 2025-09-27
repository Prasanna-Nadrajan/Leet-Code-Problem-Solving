class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows==0:
            return [[]]
        elif numRows==1:
            return [[1]]
        elif numRows==2:
            return [[1],[1,1]]
        else:
            numRows-=2
            ll=[[1],[1,1]]
            for i in range(numRows):
                n=[]
                n.append(1)
                for j in range(len(ll[i+1])-1):
                    n.append(ll[i+1][j]+ll[i+1][j+1])
                n.append(1)
                ll.append(n)
                # print(ll)
            return ll 
            
