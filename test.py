testPuzzle0 = [['1', '2', '3', '4', '5', '6', '7', '8', '.'],
              ['.', '.', '.', '.', '.', '.', '.', '9', '.'],
              ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
              ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
              ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
              ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
              ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
              ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
              ['.', '.', '.', '.', '.', '.', '.', '.', '.']]

testPuzzle4 = [['.', '8', '.', '.', '3', '.', '4', '.', '.'],
              ['.', '.', '.', '.', '5', '.', '.', '.', '1'],
              ['.', '.', '.', '.', '.', '4', '5', '8', '.'],
              ['.', '5', '7', '.', '.', '2', '.', '9', '.'],
              ['9', '.', '.', '.', '.', '.', '.', '.', '4'],
              ['.', '3', '.', '4', '.', '.', '6', '5', '.'],
              ['.', '7', '9', '2', '.', '.', '.', '.', '.'],
              ['5', '.', '.', '.', '6', '.', '.', '.', '.'],
              ['.', '.', '6', '.', '4', '.', '.', '2', '.']]

def clone(inputList):
    newlist = []
    for i in inputList:
        if type(i) == list:
            newlist.append(clone(i))
        else:
            newlist.append(i)
    return newlist


def sudokuPrint(sudokuMap):
    print("_ _ _ _ _ _ _ _ _ _ _ _ _")
    for i in range(9):
        if i == 3 or i == 6:
            print("| - - - + - - - + - - - |")
        line = "|"
        for j in range(9):
            if j == 3 or j == 6:
                line += " |"
            line += " " + sudokuMap[i][j]
        line += " |"
        print(line)
    print("‾ ‾ ‾ ‾ ‾ ‾ ‾ ‾ ‾ ‾ ‾ ‾ ‾")


def vertical(sudokuMap):
    verticalMap = []
    for i in range(9):
        verticalMap.append([])
    for i in range(9):
        for j in range(9):
            verticalMap[i].append(sudokuMap[j][i])
    return verticalMap


def block(sudokuMap):
    blockMap = []
    for i in range(9):
        blockMap.append([])
    mapCounter = 0
    for bigBlockY in range(3):
        for bigBlockX in range(3):
            for smallBlockY in range(3):
                for smallBlockX in range(3):
                    blockMap[mapCounter].append(sudokuMap[bigBlockY * 3 + smallBlockY][bigBlockX * 3 + smallBlockX])
            mapCounter += 1
    return blockMap


def numberLogic(sudokuMap, solveMap):
    newSolveMap = clone(solveMap)
    verticalMap = vertical(sudokuMap)
    blockMap = block(sudokuMap)
    for Y in range(9):
        for X in range(9):
            if sudokuMap[Y][X] in "123456789":
                newSolveMap[Y][X] = [sudokuMap[Y][X]]
                continue
            for numbers in solveMap[Y][X]:
                # test if the number is in horizontal rows
                if numbers in sudokuMap[Y]:
                    newSolveMap[Y][X].remove(numbers)
                # test if the number is in vertical rows
                elif numbers in verticalMap[X]:
                    newSolveMap[Y][X].remove(numbers)
                # test if the number is in blocks
                elif numbers in blockMap[(X // 3) + ((Y // 3) * 3)]:
                    newSolveMap[Y][X].remove(numbers)
    return newSolveMap

def mapFiller(sudokuMap, solveMap):
    for Y in range(9):
        for X in range(9):
            if len(solveMap[Y][X]) == 1:
                sudokuMap[Y][X] = solveMap[Y][X][0]
    return sudokuMap

sudokuMap = testPuzzle0

solveMap = [[["1", "2", "3", "4", "5", "6", "7", "8", "9"] for i in range(9)] for j in range(9)]

solveMap = numberLogic(sudokuMap, solveMap)
mapFiller(sudokuMap, solveMap)
sudokuPrint(sudokuMap)