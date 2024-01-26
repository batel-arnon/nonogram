from Line import Line, grade, solve_line

class Board:
    lines = []
    colums = []
    def __init__(self, w, h):
        self.wid = w
        self.hig = h
        self.allBoard = []
        for i in range(h):
            lines = []
            for j in range(w):
                lines.append(0)
            self.allBoard.append(lines)

    def set_numbers(self, is_row, arr):
        if (is_row):
            self.lines.append(arr)
        else:
            self.colums.append(arr)
    def print_whats_we_have(self):
        print(self.wid, self.hig)
        print(self.lines)
        print(self.colums)
    def draw_board(self):
        for j in range(self.hig):
            for i in range(self.wid):
                if self.allBoard[j][i] == -1:
                    print(" ", end="")
                elif self.allBoard[j][i] == 1:
                    print((chr(0x2B1B)), end="")
                else:
                    print("?", end="")
            print()
    def check_row(self ,rowNum,row):
        nums = []
        count = 0
        for i in range(0, self.wid):
            if row[i] == ' ':
                if count != 0:
                    nums.append(count)
                count = 0
            else:
                count = count + 1
        if count != 0:
            nums.append(count)
        return nums == self.lines[rowNum]

    def check_col(self, col_num):
        nums = []
        count = 0
        for i in range(0, self.hig):
            if self.allBoard[i][col_num] == ' ':
                if count != 0:
                    nums.append(count)
                count = 0
            else:
                count = count + 1
        if count != 0:
            nums.append(count)
        return nums == self.colums[col_num]

    # def fillRow(self,rowNum):
    #     inp=self.lines[rowNum]
    #
    #     testRow=[]
    #     for i in range(1,self.wid):
    #         testRow.append(' ')

    def get_best(self, all_lines):
        all_lines.sort(key=grade, reverse=True)
        print("best numbers:", all_lines[0].numbers)
        print("best grade:", grade(all_lines[0]))
        return all_lines[0:1]

    def fill_board(self):
        rows = []
        columns = []
        lines_to_work_on = []
        for i in range(len(self.allBoard)):
            result_line = self.allBoard[i]
            numbers_line = self.lines[i]
            l = Line(result_line, numbers_line, -1, i)
            rows.append(l)
            lines_to_work_on.append(l)
        for i in range(len(self.allBoard[0])):
            result_line = []
            for j in range(len(self.allBoard)):
                result_line.append(self.allBoard[j][i])
            numbers_line = self.colums[i]
            l = Line(result_line, numbers_line, i, -1)
            columns.append(l)
            lines_to_work_on.append(l)
        while len(lines_to_work_on) > 0:
            line = self.get_best(lines_to_work_on)
            solve_line(line)
            if line[0].row_number < 0:
                for j in range(len(line[0].content)):
                    self.allBoard[j][line[0].columns_number] = line[0].content[j]
                for j in range(len(rows)):
                    rows[j].content[line[0].columns_number] = line[0].content[j]
            else:
                for j in range(len(columns)):
                    columns[j].content[line[0].row_number] = line[0].content[j]
            if not line[0].has_zeros():
                lines_to_work_on.remove(line[0])
            self.draw_board()

#    arr.sort(key=grade)
