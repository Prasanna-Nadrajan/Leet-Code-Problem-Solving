class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex==0:
            return [1]
        elif rowIndex==1:
            return [1,1]
        else:
            arr=[[1],[1,1]]
            rowIndex-=1
            while(rowIndex!=0):
                temp=[1,1]
                last=arr[-1]
                i=1
                while(i<len(last)):
                    temp.insert(i,(last[i-1]+last[i]))
                    i+=1
                arr.append(temp)
                rowIndex-=1
            return arr[-1]
                
