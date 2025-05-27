import numpy as np
#import cProfile
#import timeit

import time
from datetime import timedelta
start_time = time.monotonic()

testPuzzle0 = [['.', '.', '.', '.', '9', '.', '.', '.', '.'],
              ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
              ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
              ['1', '1', '1', '.', '.', '.', '1', '1', '1'],
              ['9', '.', '.', '.', '.', '.', '.', '.', '.'],
              ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
              ['.', '.', '.', '1', '.', '.', '.', '.', '.'],
              ['.', '.', '.', '1', '.', '.', '.', '.', '.'],
              ['.', '.', '.', '1', '.', '.', '.', '.', '.']]

testPuzzle = [['.', '8', '.', '.', '3', '.', '4', '.', '.'],
              ['.', '.', '.', '.', '5', '.', '.', '.', '1'],
              ['.', '.', '.', '.', '.', '4', '5', '8', '.'],
              ['.', '5', '7', '.', '.', '2', '.', '9', '.'],
              ['9', '.', '.', '.', '.', '.', '.', '.', '4'],
              ['.', '3', '.', '4', '.', '.', '6', '5', '.'],
              ['.', '7', '9', '2', '.', '.', '.', '.', '.'],
              ['5', '.', '.', '.', '6', '.', '.', '.', '.'],
              ['.', '.', '6', '.', '4', '.', '.', '2', '.']]


# convert oude map naar nieuwe map
kaas = np.zeros((9, 9), "int8")

#testPuzzle = testPuzzle0

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
# dit moet buiten recursive
def numberLogicInit(sudokuMap, solveMap):
    for Y in range(9):
        for X in range(9):
            if sudokuMap[Y, X] != 0:
                solveMap[Y, X] = 0

# nodig voor logica, cube[nummer][y-as = 0, x-as = 1]
cube = []
for Y in range(3):
    for X in range(3):
        cube.append([Y *3, X * 3])

#check over een hele lijn heen en haal alles uit die lijn
def numberLogic(sudokuMap, solveMap):
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

def testNumberLogic(solveMap, Y, X, number):
    solveMap[Y, X] = 0
    solveMap[Y, :, number] = 0
    solveMap[:, X, number] = 0
    solveMap[Y//3*3: Y//3*3 + 3, X//3*3: X//3*3 + 3, number] = 0

def numberLogic2(sudokuMap, solveMap):
    # scant 3 rijen tegelijk om te zien of 1 getal er maar 1 keer kan staan
    for Y in range(9):
        #print(solveMap[Y * 3: Y * 3 + 3, :])
        #print("hoi")
        # non zero = skip ?
        for number in range(9):
            #print(solveMap[Y * 3: Y * 3 + 3, :, number])
            #print("hoi")
            #"""
            # horizontal
            possibleNumbers = np.nonzero(solveMap[Y, :, number])
            if len(possibleNumbers[0]) == 1:
                sudokuMap[Y, possibleNumbers[0][0]] = solveMap[Y, possibleNumbers[0][0], number]
                testNumberLogic(solveMap, Y, possibleNumbers[0][0], number)
            #     """
            #     print("hor")
            #     print(Y)
            #     print(possibleNumbers[0][0])
            #     print(number + 1)
            #     print(possibleNumbers)
            #     print(solveMap[:, possibleNumbers[0][0], number])
            #     sudokuMap[Y, possibleNumbers[0][0]] = solveMap[Y, possibleNumbers[0][0], number]
            #     solveMap[Y, possibleNumbers[0][0]] = 0
            #     # verticaal moet dit nummer ook uitgesloten worden op deze positie
            #     solveMap[:, possibleNumbers[0][0], number] = 0
            #     print(solveMap[Y, :, number])
            #     """

            # vertical
            possibleNumbers = np.nonzero(solveMap[:, Y, number])
            if len(possibleNumbers[0]) == 1:
                sudokuMap[possibleNumbers[0][0], Y] = solveMap[possibleNumbers[0][0], Y, number]
                testNumberLogic(solveMap, possibleNumbers[0][0], Y, number)
            #     """
            #     print("vert")
            #     print(Y)
            #     print(possibleNumbers[0][0])
            #     print(number + 1)
            #     print(possibleNumbers)
            #     sudokuMap[possibleNumbers[0][0], Y] = solveMap[possibleNumbers[0][0], Y, number]
            #     solveMap[possibleNumbers[0][0], Y] = 0
            #     # horizontaal moet dit nummer ook uitgesloten worden op deze positie
            #     solveMap[possibleNumbers[0][0], :, number] = 0
            #     print(solveMap[:, Y, number])
            #     """
            # block
            possibleNumbers = np.nonzero(solveMap[cube[Y][0]: cube[Y][0] + 3, cube[Y][1]: cube[Y][1] + 3, number])
            if len(possibleNumbers[0]) == 1:
                sudokuMap[cube[Y][0] + possibleNumbers[0][0], cube[Y][1] + possibleNumbers[1][0]] = number + 1
                print(possibleNumbers)
                testNumberLogic(solveMap, cube[Y][0] + possibleNumbers[0][0], cube[Y][1] + possibleNumbers[1][0], number)
                """
                print("block")
                print(Y)
                print(possibleNumbers[0][0])
                print(number + 1)
                print(possibleNumbers)
                sudokuMap[cube[Y][0] + possibleNumbers[0][0], cube[Y][1] + possibleNumbers[1][0]] = number + 1
                # moet andere logica nog uit sluiten
                """


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


numberLogicInit(sudokuMap, solveMap)

sudokuPrint(sudokuMap)

for i in range(5):
    numberLogic(sudokuMap, solveMap)
    #print(solveMap)
    mapFiller(sudokuMap)
    numberLogic2(sudokuMap, solveMap)
    #print("----------------------------")
    #print(solveMap)
    sudokuPrint(sudokuMap)

def display():
    return sudokuMap

# cProfile

# je was bezich met logica 2