#sudokuMap = [[["."] for i in range(9)] for j in range(9)]

#https://news.nd.edu/news/notre-dame-researcher-helps-make-sudoku-puzzles-less-puzzling/

testPuzzle = [['8', '.', '.', '4', '.', '6', '.', '.', '7'],
              ['.', '.', '.', '.', '.', '.', '4', '.', '.'],
              ['.', '1', '.', '.', '.', '.', '6', '5', '.'],
              ['5', '.', '9', '.', '3', '.', '7', '8', '.'],
              ['.', '.', '.', '.', '7', '.', '.', '.', '.'],
              ['.', '4', '8', '.', '2', '.', '1', '.', '3'],
              ['.', '5', '2', '.', '.', '.', '.', '9', '.'],
              ['.', '.', '1', '.', '.', '.', '.', '.', '.'],
              ['3', '.', '.', '9', '.', '2', '.', '.', '5']]

testPuzzle2 = [['8', '.', '.', '4', '.', '6', '.', '.', '7'],
              ['.', '.', '.', '.', '1', '.', '4', '1', '.'],
              ['.', '1', '.', '.', '.', '.', '6', '5', '.'],
              ['5', '.', '9', '.', '3', '1', '7', '8', '.'],
              ['.', '.', '1', '.', '7', '.', '.', '.', '.'],
              ['.', '4', '8', '.', '2', '.', '1', '.', '3'],
              ['.', '5', '2', '1', '.', '.', '.', '9', '.'],
              ['.', '.', '.', '.', '.', '.', '.', '.', '1'],
              ['.', '.', '7', '9', '.', '2', '.', '.', '5']]

testPuzzle3 = [['.', '8', '7', '5', '6', '4', '3', '2', '.'],
              ['2', '.', '.', '.', '.', '.', '.', '.', '.'],
              ['3', '.', '.', '.', '.', '.', '.', '.', '.'],
              ['4', '.', '.', '.', '.', '.', '.', '.', '.'],
              ['5', '.', '.', '.', '.', '.', '.', '.', '.'],
              ['6', '.', '.', '.', '.', '.', '5', '.', '.'],
              ['7', '.', '.', '.', '.', '.', '.', '.', '.'],
              ['8', '.', '.', '.', '.', '.', '.', '.', '.'],
              ['1', '2', '3', '.', '5', '6', '7', '8', '9']]

sudokuMap = testPuzzle3

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
                line+= " |"
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

def numberLogic(solveMap):
    newSolveMap = clone(solveMap)
    print(sudokuMap[5][7])
    print(sudokuMap[5])
    for Y in range(9):
        for X in range(9):
            if sudokuMap[Y][X] in "123456789":
                # test
                newSolveMap[Y][X] = [sudokuMap[Y][X]]
                # / test
                continue
            for numbers in solveMap[Y][X]:
                # test if the number is in horizontal rows
                if numbers in sudokuMap[Y]:
                    if Y == 5 and X == 0:
                        print(numbers)
                    newSolveMap[Y][X].remove(numbers)
                    if Y == 5 and X == 0:
                        print(newSolveMap[Y][X])
                # test if the number is in vertical rows
                elif numbers in verticalMap[X]:
                    newSolveMap[Y][X].remove(numbers)
                # test if the number is in blocks
                elif numbers in blockMap[(X // 3) + ((Y // 3) * 3)]:
                    newSolveMap[Y][X].remove(numbers)
    return newSolveMap

def numberLogic2(solveMap):
    newSolveMap = clone(solveMap)
    for Y in range(9):
        for X in range(9):
            if sudokuMap[Y][X] in "123456789":
                # test
                newSolveMap[Y][X] = [sudokuMap[Y][X]]
                # / test
                continue
            for numbers in solveMap[Y][X]:
                # test if the number is unique in horizontal rows
                numberInRow = 0
                for X2 in solveMap[Y]:
                    if numbers in X2:
                        numberInRow += 1
                if numberInRow == 1:
                    newSolveMap[Y][X] = [numbers]
                    # ff kijken of break werkt
                    break
                # test if the number is unique in vertical rows
                #"""
                vertSolveMap = vertical(solveMap)
                numberInRow = 0
                for Y2 in vertSolveMap[X]:
                    if numbers in Y2:
                        numberInRow += 1
                if numberInRow == 1:
                    newSolveMap[Y][X] = [numbers]
                    # ff kijken of break werkt
                    break
                #"""
                # test if the number is unique in blocks
                #is this actually needed ?
                """
                blockSolveMap = block(solveMap)
                numberInRow = 0
                for blocks in blockSolveMap[(X // 3) + ((Y // 3) * 3)]:
                    if numbers in blocks:
                        numberInRow += 1
                if numberInRow == 1:
                    newSolveMap[Y][X] = [numbers]
                    # ff kijken of break werkt
                    break
                """
    return newSolveMap

def mapFiller(sudokuMap, solveMap):
    for Y in range(9):
        for X in range(9):
            if len(solveMap[Y][X]) == 1:
                #print(solveMap[Y][X])

                #print(Y)
                #print(X)
                sudokuMap[Y][X] = solveMap[Y][X][0]
                #print(sudokuMap[Y][X])



verticalMap = vertical(sudokuMap)
blockMap = block(sudokuMap)
solveMap = [[["1", "2", "3", "4", "5", "6", "7", "8", "9"] for i in range(9)] for j in range(9)]

#for i in range(9):
#    for j in range(9):
#        print(solveMap[i][j])
#print("----")

sudokuPrint(sudokuMap)

solveMap = numberLogic(solveMap)

#for i in range(9):
#    for j in range(9):
#        print(solveMap[i][j])
#print("----")




mapFiller(sudokuMap, solveMap)
sudokuPrint(sudokuMap)
#print(sudokuMap[5][7])

#test
"""
solveMap = numberLogic2(solveMap)

for i in range(9):
    for j in range(9):
        print(solveMap[i][j])
print("----")




mapFiller(sudokuMap, solveMap)
sudokuPrint(sudokuMap)
"""
#/test

for i in range(9):
    for j in range(9):
        print(solveMap[i][j])
print("-----")



for i in range(25):
    verticalMap = vertical(sudokuMap)
    blockMap = block(sudokuMap)
    solveMap = numberLogic(solveMap)
    # test
    #verticalMap = vertical(sudokuMap)
    #blockMap = block(sudokuMap)
    solveMap = numberLogic2(solveMap)
    # /test
    mapFiller(sudokuMap, solveMap)
    sudokuPrint(sudokuMap)

