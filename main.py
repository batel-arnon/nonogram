from Board import Board

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def getInput():
    return 12
def getInput4():
    b=Board(45,35)
    b.setNumbers(True,[1,8,34])
    b.setNumbers(True, [10,5,6,2])
    b.setNumbers(True, [11,4,12,4,1, 1])
    b.setNumbers(True, [10,4,12, 4, 2])
    b.setNumbers(True, [8,26,2,2,1])
    b.setNumbers(True,[7,2,9,3,1,1,1,1])
    b.setNumbers(True, [5,1,1,8,13,2,2,1,1])
    b.setNumbers(True, [4,2,7,3,1,6,2,4,2])
    b.setNumbers(True, [4,1,7,2,1,7,1,2,1,2])
    b.setNumbers(True, [5,9,3,1,6,1,1,1,2])
    b.setNumbers(True, [6,10,13,1,2,1,1])
    b.setNumbers(True, [6,9,7,1,2,1,4,1])
    b.setNumbers(True, [5,9,8,1,1,1,4,2])
    b.setNumbers(True, [3,4,6,2,1,1,1,2,1,4,2])
    b.setNumbers(True, [1,3,5,1,1,8,1,4,2])
    b.setNumbers(True, [1, 2, 1, 5,2,1,7,1,2])
    b.setNumbers(True,[1,3,3,1,13,2,2])
    b.setNumbers(True, [1,5,3,1,1,3,2])
    b.setNumbers(True, [1,6,2,1,17,2])
    b.setNumbers(True, [1,8,1,4,6,6,2])
    b.setNumbers(True, [1,10,1,17,3,1])
    b.setNumbers(True,[1,10,1,1,4,2,1])
    b.setNumbers(True, [1,8,1,1,18,1,3])
    b.setNumbers(True, [1,7,1,1,2,1,1,3])
    b.setNumbers(True, [1,5,1,1,2,1,1,3])
    b.setNumbers(True,[1,4,1,1,2,5,4,1,1,3])
    b.setNumbers(True, [1,2,1,2,1,1,8])
    b.setNumbers(True, [1,1,1,2,5,4,1,5])
    b.setNumbers(True, [3,1,2,2,3])
    b.setNumbers(True, [2,5,15,1,1])
    b.setNumbers(True,[1,1,3])
    b.setNumbers(True, [3,1,15,1,1,1])
    b.setNumbers(True, [6,1,1,1,1,1,1,3,5])
    b.setNumbers(True, [12,1,1,1,1,1,2,1,1])
    b.setNumbers(True, [12,1,1,1,1,1,1,2,3])

    b.setNumbers(False, [1,11,5,1])
    b.setNumbers(False, [13,2,2,1])
    b.setNumbers(False, [14,1,5,1,2])
    b.setNumbers(False, [14,1,9,1,2])
    b.setNumbers(False, [7,4,1,11,1,2])
    b.setNumbers(False, [6,1,2,13,3])
    b.setNumbers(False, [9,2,10,2,3])
    b.setNumbers(False, [5,3,8,1,4])
    b.setNumbers(False, [4,1,4,6,5])
    b.setNumbers(False, [4,2,1,1,2,4,4])
    b.setNumbers(False, [2,4,4,2,3])
    b.setNumbers(False, [1,4,4,9,2])
    b.setNumbers(False, [13,1])
    b.setNumbers(False, [14,1])
    b.setNumbers(False, [16,2,1])
    b.setNumbers(False, [3,27])
    b.setNumbers(False, [2,12,1,1,1,1])
    b.setNumbers(False, [1,12,1,1,1,1])
    b.setNumbers(False, [1,12,1,1,1,2,1])
    b.setNumbers(False, [1,2,1,1,1,1])
    b.setNumbers(False, [1,1,11,11,2,1])
    b.setNumbers(False, [1,1,8,2,11,1,1])
    b.setNumbers(False, [1,1,2,4,1,1,5,1,2,1])
    b.setNumbers(False, [1,1,1,1,3,1,5,3,1,1,1])
    b.setNumbers(False, [1,1,1,1,4,2,3,1,1,1,1,2,1])
    b.setNumbers(False, [1,3,2,4,1,1,3,1,1,1,1,1,1])
    b.setNumbers(False, [1,3,1,1,7,1,1,1,1,1,1,2,1])
    b.setNumbers(False, [1,3,5,1,3,1,1,1,3,1,1,2])
    b.setNumbers(False, [1,3,6,4,1,1,1,1,3])
    b.setNumbers(False, [1,3,5,3,1,1,1,1,2])
    b.setNumbers(False, [1,3,5,1,3,1,1,1,1,2])
    b.setNumbers(False, [1,3,6,4,3,1,1])
    b.setNumbers(False, [1,3,11,3,1,1,1,1])
    b.setNumbers(False, [1,3,3,1,1,1,1])
    b.setNumbers(False, [1,4,6,1,1,1])
    b.setNumbers(False, [1,6,7,1,1,1])
    b.setNumbers(False, [2,18,1,1])
    b.setNumbers(False, [3,7])
    b.setNumbers(False, [21,1,1,3])
    b.setNumbers(False, [5,3,17,2,1,1])
    b.setNumbers(False, [4,1,1,1,4,1,2,3,1])
    b.setNumbers(False, [2,2,3,5,6,1,1,1])
    b.setNumbers(False, [1,1,2,7,3])
    b.setNumbers(False, [2,1,5,3,7])
    b.setNumbers(False, [6,3,4,1,4])

    b.print()
    b.drawBoard()
    b.fillBoard()
    b.drawBoard()
    # b.fillBoard()
    # b.drawBoard()
    # b.fillBoard()
    # b.drawBoard()
    # b.fillBoard()
    # b.drawBoard()
    # b.fillBoard()
    # b.drawBoard()
    # b.fillBoard()
    # b.drawBoard()

def getInput2():
    b = Board(10,10)
    b.setNumbers(True,[2,1])
    b.setNumbers(True,[2,1])
    b.setNumbers(True, [2,3])
    b.setNumbers(True,[8])
    b.setNumbers(True,[2,2,2])
    b.setNumbers(True,[1,2,1])
    b.setNumbers(True,[6])
    b.setNumbers(True,[1,1])
    b.setNumbers(True,[4])
    b.setNumbers(True,[10])

    b.setNumbers(False,[1])
    b.setNumbers(False,[3,1])
    b.setNumbers(False,[4,1,1])
    b.setNumbers(False,[4,4])
    b.setNumbers(False,[1,4,2])
    b.setNumbers(False,[5,2])
    b.setNumbers(False,[1,2,4])
    b.setNumbers(False,[4,1,1])
    b.setNumbers(False,[3,1])
    b.setNumbers(False,[1])

    b.print()
    b.drawBoard()
    b.fillBoard()
    b.drawBoard()

def getInput3():
    b = Board(5,5)
    b.setNumbers(True, [5])
    b.setNumbers(True, [1,1])
    b.setNumbers(True, [1,1])
    b.setNumbers(True, [1,1])
    b.setNumbers(True, [5])

    b.setNumbers(False, [5])
    b.setNumbers(False, [1, 1])
    b.setNumbers(False, [1, 1])
    b.setNumbers(False, [1,1])
    b.setNumbers(False, [5])

    b.print()
    b.drawBoard()
    b.fillBoard()
    b.drawBoard()
# Press the green button in the gutter to run the script.

getInput2()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/