#sudokuMap = [[["."] for i in range(9)] for j in range(9)]

#https://news.nd.edu/news/notre-dame-researcher-helps-make-sudoku-puzzles-less-puzzling/

testPuzzle0 = [['.', '.', '.', '.', '.', '.', '.', '.', '.'],
              ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
              ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
              ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
              ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
              ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
              ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
              ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
              ['.', '.', '.', '.', '.', '.', '.', '.', '.']]

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

testPuzzle4 = [['.', '8', '.', '.', '3', '.', '4', '.', '.'],
              ['.', '.', '.', '.', '5', '.', '.', '.', '1'],
              ['.', '.', '.', '.', '.', '4', '5', '8', '.'],
              ['.', '5', '7', '.', '.', '2', '.', '9', '.'],
              ['9', '.', '.', '.', '.', '.', '.', '.', '4'],
              ['.', '3', '.', '4', '.', '.', '6', '5', '.'],
              ['.', '7', '9', '2', '.', '.', '.', '.', '.'],
              ['5', '.', '.', '.', '6', '.', '.', '.', '.'],
              ['.', '.', '6', '.', '4', '.', '.', '2', '.']]

testPuzzle5 = [['7', '.', '.', '.', '3', '.', '4', '.', '.'],
              ['.', '.', '.', '.', '5', '.', '.', '.', '1'],
              ['.', '.', '.', '.', '.', '4', '5', '8', '.'],
              ['.', '5', '7', '.', '.', '2', '.', '9', '.'],
              ['9', '.', '.', '.', '.', '.', '.', '.', '4'],
              ['.', '3', '.', '4', '.', '.', '6', '5', '.'],
              ['.', '7', '9', '2', '.', '.', '.', '.', '.'],
              ['5', '.', '.', '.', '6', '.', '.', '.', '.'],
              ['.', '.', '6', '.', '4', '.', '.', '2', '.']]

#sudokuMap = testPuzzle5


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


def numberLogic2(sudokuMap, solveMap):
    newSolveMap = clone(solveMap)
    for Y in range(9):
        for X in range(9):
            if sudokuMap[Y][X] in "123456789":
                newSolveMap[Y][X] = [sudokuMap[Y][X]]
                continue
            for numbers in solveMap[Y][X]:
                # test if the number is unique in horizontal rows
                numberInRow = 0
                for X2 in solveMap[Y]:
                    if numbers in X2:
                        numberInRow += 1
                if numberInRow == 1:
                    newSolveMap[Y][X] = [numbers]
                    break
                # test if the number is unique in vertical rows
                vertSolveMap = vertical(solveMap)
                numberInRow = 0
                for Y2 in vertSolveMap[X]:
                    if numbers in Y2:
                        numberInRow += 1
                if numberInRow == 1:
                    newSolveMap[Y][X] = [numbers]
                    break
                # test if the number is unique in blocks
                #"""
                blockSolveMap = block(solveMap)
                numberInRow = 0
                for blocks in blockSolveMap[(X // 3) + ((Y // 3) * 3)]:
                    if numbers in blocks:
                        numberInRow += 1
                if numberInRow == 1:
                    newSolveMap[Y][X] = [numbers]
                    # ff kijken of break werkt
                    break
                #"""
    return newSolveMap


def mapFiller(sudokuMap, solveMap):
    for Y in range(9):
        for X in range(9):
            if len(solveMap[Y][X]) == 1:
                sudokuMap[Y][X] = solveMap[Y][X][0]
    return sudokuMap


def recursionTest(sudokuMap, printFirstSolved, completedMaps):
    solveMap = [[["1", "2", "3", "4", "5", "6", "7", "8", "9"] for i in range(9)] for j in range(9)]
    running = True

    # when stuck, forkLevel will guess numbers with the least possibilities first
    forkLevel = 2

    while True:
        progressionTest = clone(sudokuMap)
        solveMap = numberLogic(sudokuMap, solveMap)
        sudokuMap = mapFiller(sudokuMap, solveMap)
        solveMap = numberLogic2(sudokuMap, solveMap)
        sudokuMap = mapFiller(sudokuMap, solveMap)

        # ugly test if it is solved
        solved = 0
        for Y in sudokuMap:
            if '.' in Y:
                solved = 1
                break
        if solved == 0:
            if printFirstSolved == True:
                sudokuPrint(sudokuMap)
                return False
            else:
                #sudokuPrint(sudokuMap)
                if sudokuMap in completedMaps:
                    continue
                else:
                    sudokuPrint(sudokuMap)
                    completedMaps.append(sudokuMap)
                    return completedMaps

        if sudokuMap == progressionTest:
            while forkLevel < 10:
                for Y in range(9):
                    for X in range(9):
                        if len(solveMap[Y][X]) == forkLevel:
                            for numbers in solveMap[Y][X]:
                                forkTest = clone(sudokuMap)
                                forkTest[Y][X] = numbers
                                completedMaps = recursionTest(forkTest, printFirstSolved, completedMaps)
                                if completedMaps == False:
                                    return False
                forkLevel += 1
            return completedMaps

printFirstSolved = False
recursionTest(testPuzzle0, printFirstSolved, [])