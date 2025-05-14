import numpy as np

import time
from datetime import timedelta
start_time = time.monotonic()


testPuzzle = [['.', '8', '.', '.', '3', '.', '4', '.', '.'],
              ['.', '.', '.', '.', '5', '.', '.', '.', '1'],
              ['.', '.', '.', '.', '.', '4', '5', '8', '.'],
              ['.', '5', '7', '.', '.', '2', '.', '9', '.'],
              ['9', '.', '.', '.', '.', '.', '.', '.', '4'],
              ['.', '3', '.', '4', '.', '.', '6', '5', '.'],
              ['.', '7', '9', '2', '.', '.', '.', '.', '.'],
              ['5', '.', '.', '.', '6', '.', '.', '.', '.'],
              ['.', '.', '6', '.', '4', '.', '.', '2', '.']]

print(testPuzzle[0])
# convert oude map naar nieuwe map
kaas = np.zeros((9, 9), "int8")

for Y in range(9):
    for X in range(9):
        if testPuzzle[Y][X] == ".":
            continue
        else:
            kaas[Y, X] = int(testPuzzle[Y][X])
print(kaas)
#sudokuMap = np.array(kaas)

sudokuMap = kaas

#print(sudokuMap)

def sudokuPrint(sudokuMap):
    printMap = " _ _ _ _ _ _ _ _ _ _ _ _ _\n"
    for i in range(9):
        for k in range(3):
            printMap += " |"
            for j in range(3):
                if sudokuMap[i, (k * 3) + j] == 0:
                    printMap += "  "
                else:
                    printMap += " " + str(sudokuMap[i, (k * 3) + j])

        printMap += " |\n"

        if i % 3 == 2 and i != 8:
            printMap += " | - - - + - - - + - - - |\n"
    printMap += " ‾ ‾ ‾ ‾ ‾ ‾ ‾ ‾ ‾ ‾ ‾ ‾ ‾"
    print(printMap)

#sudokuPrint(sudokuMap)

solveMap = np.array([[[1, 2, 3, 4, 5, 6, 7, 8, 9]] * 9] * 9, dtype="int8")

"""
for Y in range(9):
    for X in range(9):
        if not np.any(solveMap[Y, X]):
            print("hoi")
            continue
        for testNumber in range(9):
            if solveMap[Y, X, testNumber] == 0:
                continue
            # Horizontal
            if solveMap[Y, X, testNumber] in sudokuMap[Y]:
                solveMap[Y, X, testNumber] = 0
            # Vertical
            if solveMap[Y, X, testNumber] in sudokuMap[:, X]:
                solveMap[Y, X, testNumber] = 0


print(solveMap)
"""

#check over een hele lijn heen en haal alles uit die lijn
def numberLogic(sudokuMap, solveMap):
    cube = []
    for Y in range(3):
        for X in range(3):
            cube.append([Y *3, X * 3])

    for Y in range(9):
        #if not np.any(solveMap[Y]):
        #    print("hoi")
        #    continue
        for testNumber in range(9):
            if testNumber + 1 in sudokuMap[Y]:
                solveMap[Y, :, testNumber] = 0
            if testNumber + 1 in sudokuMap[:, Y]:
                solveMap[:, Y, testNumber] = 0
            if testNumber + 1 in sudokuMap[cube[Y][0]:cube[Y][0] + 3, cube[Y][1]:cube[Y][1] + 3]:
                solveMap[cube[Y][0]:cube[Y][0] + 3, cube[Y][1]:cube[Y][1] + 3, testNumber] = 0
#print(solveMap)

#dit werkt nog niet
def mapFiller(sudokuMap):
    for Y in range(9):
        for X in range(9):
            if sudokuMap[Y, X] != 0:
                continue
            possibleNumbers = np.nonzero(solveMap[Y, X])
            if len(possibleNumbers[0]) == 1:
                number = possibleNumbers[0][0]
                #print(number)
                #print(possibleNumbers)
                #sudokuMap[Y, X] = solveMap[Y, X, possibleNumbers]
                #sudokuMap[Y, X] = solveMap[Y, X, number]
                sudokuMap[Y, X] = solveMap[Y, X, possibleNumbers[0][0]]

sudokuPrint(sudokuMap)

for i in range(20):
    numberLogic(sudokuMap, solveMap)
    #print(solveMap)
    mapFiller(sudokuMap)
    sudokuPrint(sudokuMap)

# cProfile