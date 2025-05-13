import numpy as np

import time
from datetime import timedelta
start_time = time.monotonic()

"""
blabla = np.array([[[1, 2, 3, 4, 5, 6, 7, 8, 9]] * 9] * 9, dtype="int8")

blabla[0, :, 1] = 0

#for i in range(10000):
#    henk = 2 in blabla
#print(henk)

for i in range(10000):
    henk = np.isin(blabla, 2)
print(True in henk)
"""

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
sudokuMap = np.array(kaas)


# print(sudokuMap)

def sudokuPrint(sudokuMap):
    printMap = " _ _ _ _ _ _ _ _ _ _ _ _ _\n"
    for i in range(27):
        printMap += " |"
        for j in sudokuMap[i * 3: i * 3 + 3]:
            printMap += " " + str(j)

        if i % 3 == 2:
            printMap += " |\n"

        if i % 9 == 8 and i != 26:
            printMap += " | - - - + - - - + - - - |\n"
    printMap += " ‾ ‾ ‾ ‾ ‾ ‾ ‾ ‾ ‾ ‾ ‾ ‾ ‾"
    print(printMap)


# sudokuPrint(sudokuMap)
#"""
for i in range(1000):
    solveMap = np.array([[[1, 2, 3, 4, 5, 6, 7, 8, 9]] * 9] * 9, dtype="int8")
    
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

for i in range(1000):
    solveMap = np.array([[[1, 2, 3, 4, 5, 6, 7, 8, 9]] * 9] * 9, dtype="int8")


    #cube = []

    #for Y in range(3):
    #    for X in range(3):
    #        cube.append([Y * 3, X * 3])

    for Y in range(9):
        if not np.any(solveMap[Y]):
            print("hoi")
            continue
        for testNumber in range(9):
            if testNumber + 1 in sudokuMap[Y]:
                solveMap[Y, :, testNumber] = 0
            if testNumber + 1 in sudokuMap[:, Y]:
                solveMap[:, Y, testNumber] = 0
            #if testNumber + 1 in sudokuMap[cube[Y][0]:cube[Y][0] + 3, cube[Y][1]:cube[Y][1] + 3]:
            #    solveMap[cube[Y][0]:cube[Y][0] + 3, cube[Y][1]:cube[Y][1] + 3, testNumber] = 0
print(solveMap)
"""
end_time = time.monotonic()
print(timedelta(seconds=end_time - start_time))

#timeit van python gebruiken