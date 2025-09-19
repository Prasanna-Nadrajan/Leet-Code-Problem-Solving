class Spreadsheet:

    def __init__(self, rows: int):
        self.ss={}
        for i in range(1,rows+1):
            self.ss[i]=[0]*26


    def conv(self,cell):
        col=ord(cell[0])-ord('A')
        row=int(cell[1::])
        return row,col

    def setCell(self, cell: str, value: int) -> None:
        row,col=self.conv(cell)
        self.ss[row][col]=value

    def resetCell(self, cell: str) -> None:
        row,col=self.conv(cell)
        self.ss[row][col]=0

    def getValue(self, formula: str) -> int:
        formula=formula[1::]
        formula=formula.split("+")
        num1=0
        num2=0
        if not formula[0][0].isdigit():
            row,col=self.conv(formula[0])
            num1=self.ss[row][col]
        else:
            num1=int(formula[0])
        if not formula[1][0].isdigit():
            row,col=self.conv(formula[1])
            num2=self.ss[row][col]
        else:
            num2=int(formula[1])
        return num1+num2

# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)
