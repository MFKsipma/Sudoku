import time
from datetime import timedelta
start_time = time.monotonic()




testPuzzle = ['.', '8', '.', '.', '3', '.', '4', '.', '.',
              '.', '.', '.', '.', '5', '.', '.', '.', '1',
              '.', '.', '.', '.', '.', '4', '5', '8', '.',
              '.', '5', '7', '.', '.', '2', '.', '9', '.',
              '9', '.', '.', '.', '.', '.', '.', '.', '4',
              '.', '3', '.', '4', '.', '.', '6', '5', '.',
              '.', '7', '9', '2', '.', '.', '.', '.', '.',
              '5', '.', '.', '.', '6', '.', '.', '.', '.',
              '.', '.', '6', '.', '4', '.', '.', '2', '.']

sudokuMap = testPuzzle


def clone(inputList):
    newlist = []
    for i in inputList:
        if type(i) == list:
            newlist.append(clone(i))
        else:
            newlist.append(i)
    return newlist


#sudokuMap = ["."] * 81

def sudokuPrint(sudokuMap):
    printMap = " _ _ _ _ _ _ _ _ _ _ _ _ _\n"
    for i in range(27):
        printMap += " |"
        for j in sudokuMap[i * 3: i * 3 + 3]:
            printMap += " " + j

        if i % 3 == 2:
            printMap += " |\n"

        if i % 9 == 8 and i != 26:
            printMap += " | - - - + - - - + - - - |\n"
    printMap += " ‾ ‾ ‾ ‾ ‾ ‾ ‾ ‾ ‾ ‾ ‾ ‾ ‾"
    print(printMap)


# same row/block test
def logic1(sudokuMap, solveMap):
    testSolveMap = clone(solveMap)
    for Y in range(9):
        for X in range(9):
            if sudokuMap[X + Y * 9] != ".":
                solveMap[X + Y * 9] = []
                continue
            for numbers in testSolveMap[X + Y * 9]:
                # horizontal test
                if numbers in sudokuMap[Y * 9: Y * 9 + 9]:
                    solveMap[X + Y * 9].remove(numbers)
                    continue

                # vertical test
                if numbers in sudokuMap[X::9]:
                    solveMap[X + Y * 9].remove(numbers)
                    continue
                """
                # block test
                blockCoordinates = ((X // 3) + ((Y // 3) * 27))
                # row one of block
                if numbers in sudokuMap[blockCoordinates: blockCoordinates + 3]:
                    solveMap[X + Y * 9].remove(numbers)
                    continue
                # row two of block
                if numbers in sudokuMap[blockCoordinates + 9: blockCoordinates + 3 + 9]:
                    solveMap[X + Y * 9].remove(numbers)
                    continue
                # row one of block
                if numbers in sudokuMap[blockCoordinates + 18: blockCoordinates + 3 + 18]:
                    solveMap[X + Y * 9].remove(numbers)
                """


# same row/block test, 15% slower :(
def logic1test(sudokuMap, solveMap):
    testSolveMap = clone(solveMap)
    for i in range(81):
        if sudokuMap[i] != ".":
            solveMap[i] = []
            continue
        for numbers in testSolveMap[i]:
            # horizontal test
            if numbers in sudokuMap[i // 9 * 9: i // 9 * 9 + 9]:
                solveMap[i].remove(numbers)
                continue

            # vertical test
            if numbers in sudokuMap[i % 9::9]:
                solveMap[i].remove(numbers)
                continue

            # block test
            blockCoordinates = i // 27 * 27 + i % 9 // 3 * 3
            # row one of block
            if numbers in sudokuMap[blockCoordinates: blockCoordinates + 3]:
                solveMap[i].remove(numbers)
                continue
            # row two of block
            if numbers in sudokuMap[blockCoordinates + 9: blockCoordinates + 3 + 9]:
                solveMap[i].remove(numbers)
                continue
            # row three of block
            if numbers in sudokuMap[blockCoordinates + 9: blockCoordinates + 3 + 9]:
                solveMap[i].remove(numbers)


def mapFiller(sudokuMap, solveMap):
    for i in range(81):
        if len(solveMap[i]) == 1:
            sudokuMap[i] = solveMap[i][0]
    return sudokuMap

sudokuPrint(sudokuMap)

solveMap = [["1", "2", "3", "4", "5", "6", "7", "8", "9"] for i in range(81)]

for i in range(5000):
    logic1test(sudokuMap, solveMap)
    mapFiller(sudokuMap, solveMap)
    #sudokuPrint(sudokuMap)
print(solveMap)
sudokuPrint(sudokuMap)

end_time = time.monotonic()
print(timedelta(seconds=end_time - start_time))