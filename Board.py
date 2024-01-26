from Line import Line, grade, solve10Line

class Board:
    lines = []
    colums = []
    def __init__(self, w, h):
        self.wid = w
        self.hig = h
        self.all = []
        for i in range(h):
            inr=[]
            for j in range(w):
                inr.append(0)
            self.all.append(inr)

    def setNumbers(self ,isRow ,arr):
        if (isRow):
            self.lines.append(arr)
        else:
            self.colums.append(arr)
    def print(self):
        print(self.wid ,self.hig)
        print(self.lines)
        print(self.colums)
    def drawBoard(self):
        for j in range(self.hig):
            #print("line",j)
            for i in range(self.wid):
                if self.all[j][i]==-1:
                    print (" " ,end="")
                elif self.all[j][i]==1:
                    print("$", end="")
                else:
                    print("?",end="")
            print()
    def checkRow(self ,rowNum,row):
        nums =[]
        count =0
        for i in range(0 ,self.wid):
            if row[i]==' ':
                if count!=0:
                    nums.append(count)
                count = 0
            else:
                count =count +1
        if count != 0:
            nums.append(count)
        return nums==self.lines[rowNum]

    def checkCol(self ,colNum):
        nums =[]
        count =0
        for i in range(0 ,self.hig):
            if self.all[i][colNum]==' ':
                if count!=0:
                    nums.append(count)
                count = 0
            else:
                count=count +1
        if count != 0:
            nums.append(count)
        return nums==self.colums[colNum]

    # def fillRow(self,rowNum):
    #     inp=self.lines[rowNum]
    #
    #     testRow=[]
    #     for i in range(1,self.wid):
    #         testRow.append(' ')

    def getBest(self, allLines):
        allLines.sort(key=grade,reverse=True)
        print("best numbers:",allLines[0].numbers)
        print("best grade:",grade(allLines[0]))
        return allLines[0:1]

    def fillBoard(self):
        #while True:
        rows = []
        columns = []
        linestoworkon=[]
        for i in range(len(self.all)):
            result_line = self.all[i]
            numbers_line=self.lines[i]
            l=Line(result_line, numbers_line, -1, i)
            rows.append(l)
            linestoworkon.append(l)
        for i in range (len(self.all[0])):
            result_line=[]
            for j in range(len(self.all)):
                result_line.append(self.all[j][i])
            numbers_line = self.colums[i]
            l = Line(result_line, numbers_line,i,-1)
            columns.append(l)
            linestoworkon.append(l)
        #for i in range(8):
        while len(linestoworkon) > 0:
            line = self.getBest(linestoworkon)
            solve10Line(line)
            if line[0].row_number<0:
                for j in range(len(line[0].content)):
                    self.all[j][line[0].columns_number]=line[0].content[j]
                for j in range(len(rows)):
                    rows[j].content[line[0].columns_number]=line[0].content[j]
            else:
                for j in range(len(columns)):
                    columns[j].content[line[0].row_number]=line[0].content[j]
            if not line[0].hasZeros():
                linestoworkon.remove(line[0])
            self.drawBoard()

#    arr.sort(key=grade)
