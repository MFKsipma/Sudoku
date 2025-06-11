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

testPuzzle1 = [['.', '.', '.', '.', '.', '.', '.', '.', '.'],
              ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
              ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
              ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
              ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
              ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
              ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
              ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
              ['.', '.', '.', '.', '.', '.', '.', '.', '.']]

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
testPuzzle = testPuzzle1
def puzzleConvert(testPuzzle):
    convertedMap = np.zeros((9, 9), "int8")
    for Y in range(9):
        for X in range(9):
            if testPuzzle[Y][X] == ".":
                continue
            else:
                convertedMap[Y, X] = int(testPuzzle[Y][X])
    return convertedMap

sudokuMap = puzzleConvert(testPuzzle)


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
        cube.append([Y * 3, X * 3])

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

# scant 3 rijen tegelijk om te zien of 1 getal er maar 1 keer kan staan
def numberLogic2(sudokuMap, solveMap):
    noChangesCounter = 81
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
                noChangesCounter += -1
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
                noChangesCounter += -1
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
                #print(possibleNumbers)
                testNumberLogic(solveMap, cube[Y][0] + possibleNumbers[0][0], cube[Y][1] + possibleNumbers[1][0], number)
                noChangesCounter += -1
                """
                print("block")
                print(Y)
                print(possibleNumbers[0][0])
                print(number + 1)
                print(possibleNumbers)
                sudokuMap[cube[Y][0] + possibleNumbers[0][0], cube[Y][1] + possibleNumbers[1][0]] = number + 1
                # moet andere logica nog uit sluiten
                """
    return noChangesCounter


#dit werkt nog niet
def mapFiller(sudokuMap):
    noChangesCounter = 81
    for Y in range(9):
        for X in range(9):
            if sudokuMap[Y, X] != 0:
                continue
            possibleNumbers = np.nonzero(solveMap[Y, X])
            if len(possibleNumbers[0]) == 1:
                sudokuMap[Y, X] = solveMap[Y, X, possibleNumbers[0][0]]
                noChangesCounter += -1
                continue
    return noChangesCounter


numberLogicInit(sudokuMap, solveMap)

def sudokuSolver(sudokuMap, solveMap, options):
    while True:
        noChangesCounter = 0
        numberLogic(sudokuMap, solveMap)
        noChangesCounter += mapFiller(sudokuMap)
        noChangesCounter += numberLogic2(sudokuMap, solveMap)
        sudokuPrint(sudokuMap)
        print(noChangesCounter)
        if noChangesCounter == 162:
            print("Map incomplete")
            if options == False:
                break
            else:
                break
        if 0 not in sudokuMap:
            print("Map completed")
            break


def display():
    return puzzleConvert(testPuzzle)

# cProfile

sudokuSolver(sudokuMap, solveMap, True)