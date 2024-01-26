
class Line:
    def __init__(self, content,numbers,columns_number,row_number):
        self.content = content
        self.numbers = numbers
        self.columns_number = columns_number
        self.row_number = row_number
        self.fine = 1
        self.options=[]
    def hasZeros(self):
        for i in range(len(self.content)):
            if self.content[i]==0:
                return True
        return False


def buildOptions(numbers,content,options,start):
    if len(numbers) == 1 and len(content) - start >= numbers[0]:
        arr=[]
        for i in range(0,len(content)):
            if i<start:
                arr.append(content[i])
            elif i<start+numbers[0]:
                arr.append(1)
            else:
                arr.append(-1)
        options.append(arr)
    if len(numbers) == 1 and len(content) - start > numbers[0]:
        content[start]=-1
        buildOptions(numbers, content, options,start+1)
    if len(numbers) > 1:
        minLenReq=sum(numbers)+len(numbers)-1
        if len(content) - start > minLenReq:
            content[start]=-1
            buildOptions(numbers, content, options, start + 1)
        if len(content) - start >= minLenReq:
            for i in range(start, start+numbers[0]):
                    content[i] = 1
            content[start+numbers[0]]=-1
            temp=[]
            for i in range(1,len(numbers)):
                temp.append(numbers[i])
            buildOptions(temp, content, options, start +numbers[0] + 1)

def merge(options):
    ret = []
    for i in range(len(options[0])):
        flag = True
        for j in range(len(options)):
            if options[0][i] != options[j][i]:
                flag = False
        if flag:
            ret.append(options[0][i])
        else:
            ret.append(0)
    return ret
def fillLine(newVals,contenet):
    for i in range(len(newVals)):
        if contenet[i]==0:
            contenet[i] = newVals[i]

def checkTheOptions(options,content):
    realOptions=[]
    for i in range(len(options)):
        flag = True
        for j in range(len(content)):
            if content[j] != options[i][j] and content[j] != 0:
                flag = False
        if flag:
            realOptions.append(options[i])
    return realOptions

def buldArr(conten):
    arr = []
    for i in range(len(conten)):
        arr.append(0)
    return arr

def solve10Line(lis):
    #l=Line([0,0,0,0,0,0,0,-1],[4,2])
    for i in range(len(lis)):
        l=lis[i]
        buildOptions(l.numbers,buldArr(l.content),l.options,0)
        #print(l.options)
        fillLine(merge(checkTheOptions(l.options,l.content)),l.content)
        print(l.numbers, l.content)
        lis[0].fine += 10

def number_of_cells_needed(l:Line):
    number_of_cells_needed = 0
    for i in range(len(l.numbers)):
        number_of_cells_needed = number_of_cells_needed + l.numbers[i]
    number_of_cells_needed = number_of_cells_needed + len(l.numbers) -1
    return number_of_cells_needed;

def grade(l:Line):
    grade = number_of_cells_needed(l) - 2 * len(l.numbers) - l.fine # fine on long list of small numbers
    return grade + 80 - len(l.content)  # fine to start with the shortest: rows or columns.

