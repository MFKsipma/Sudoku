import numpy as np
import random
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

testPuzzle00 = [['1', '1', '1', '1', '1', '1', '1', '1', '1'],
              ['1', '1', '1', '1', '1', '1', '1', '1', '1'],
              ['1', '1', '1', '1', '1', '1', '1', '1', '1'],
              ['1', '1', '1', '1', '1', '1', '1', '1', '1'],
              ['1', '1', '1', '1', '1', '1', '1', '1', '1'],
              ['1', '1', '1', '1', '1', '1', '1', '1', '1'],
              ['1', '1', '1', '1', '1', '1', '1', '.', '.'],
              ['1', '1', '1', '1', '1', '1', '.', '.', '.'],
              ['1', '1', '1', '1', '1', '1', '.', '.', '.']]

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

testPuzzle2 = [['.', '8', '.', '.', '3', '.', '4', '.', '.'],
              ['.', '.', '.', '.', '5', '.', '.', '.', '1'],
              ['.', '.', '.', '.', '.', '4', '.', '8', '.'],
              ['.', '5', '7', '.', '1', '2', '.', '9', '.'],
              ['9', '.', '.', '.', '.', '.', '.', '.', '4'],
              ['1', '3', '.', '4', '.', '.', '6', '5', '.'],
              ['.', '7', '9', '2', '.', '.', '.', '.', '.'],
              ['5', '.', '.', '1', '6', '.', '.', '.', '.'],
              ['.', '1', '6', '3', '4', '.', '.', '2', '.']]

testPuzzle3 = [['.', '1', '2', '3', '4', '5', '6', '7', '.'],
              ['.', '.', '8', '.', '.', '.', '.', '.', '.'],
              ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
              ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
              ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
              ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
              ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
              ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
              ['.', '.', '.', '.', '.', '.', '.', '.', '.']]


testPuzzle4 = [['.', '.', '.', '.', '.', '.', '.', '.', '.'],
              ['1', '2', '3', '.', '.', '.', '7', '8', '9'],
              ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
              ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
              ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
              ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
              ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
              ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
              ['.', '.', '.', '.', '.', '.', '.', '.', '.']]


# convert oude map naar nieuwe map
testPuzzle = testPuzzle00

emptyMap = testPuzzle1

finishedMaps = []
duplicateForks = []

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


def cubeGen(sudokuMap):
    cubeMap = []
    for Y in range(3):
        for X in range(3):
            cubeMap.append(sudokuMap[Y * 3: Y * 3 + 3, X * 3: X * 3 + 3])
    return cubeMap


#check over een hele lijn heen en haal alles uit die lijn
def numberLogic(sudokuMap, solveMap, cubeMap, cubeSolve):
    for Y in range(9):
        for testNumber in range(9):
            if testNumber + 1 in sudokuMap[Y]:
                solveMap[Y, :, testNumber] = 0
            if testNumber + 1 in sudokuMap[:, Y]:
                solveMap[:, Y, testNumber] = 0
            if testNumber + 1 in cubeMap[Y]:
                cubeSolve[Y][:, :, testNumber] = 0


def testNumberLogic(solveMap, Y, X, number):
    solveMap[Y, X] = 0
    solveMap[Y, :, number] = 0
    solveMap[:, X, number] = 0
    solveMap[Y//3*3: Y//3*3 + 3, X//3*3: X//3*3 + 3, number] = 0

# scant om te zien of 1 getal er maar 1 keer kan staan in een rij/colom/cubes
def numberLogic2(sudokuMap, solveMap):
    noChangesCounter = 81
    for Y in range(9):
        for number in range(9):
            # horizontal
            possibleNumbers = np.nonzero(solveMap[Y, :, number])
            if len(possibleNumbers[0]) == 1:
                sudokuMap[Y, possibleNumbers[0][0]] = solveMap[Y, possibleNumbers[0][0], number]
                testNumberLogic(solveMap, Y, possibleNumbers[0][0], number)
                noChangesCounter += -1

            # vertical
            possibleNumbers = np.nonzero(solveMap[:, Y, number])
            if len(possibleNumbers[0]) == 1:
                sudokuMap[possibleNumbers[0][0], Y] = solveMap[possibleNumbers[0][0], Y, number]
                testNumberLogic(solveMap, possibleNumbers[0][0], Y, number)
                noChangesCounter += -1

            # block
            possibleNumbers = np.nonzero(solveMap[cube[Y][0]: cube[Y][0] + 3, cube[Y][1]: cube[Y][1] + 3, number])
            if len(possibleNumbers[0]) == 1:
                sudokuMap[cube[Y][0] + possibleNumbers[0][0], cube[Y][1] + possibleNumbers[1][0]] = number + 1
                testNumberLogic(solveMap, cube[Y][0] + possibleNumbers[0][0], cube[Y][1] + possibleNumbers[1][0], number)
                noChangesCounter += -1

    return noChangesCounter

# werkt alleen nog voor regel 1-3
def numberLogic3(sudokuMap, solveMap, cubeMap, cubeSolve):
    for rowOrColumn in range(3):
        for number in range(9):
            for cubeNumber in range(3):

                # horizontal
                # checks if row is already solved
                if len(np.nonzero(solveMap[rowOrColumn])) > 0:

                    # checks if the tested number is already in the row
                    if number + 1 in sudokuMap[rowOrColumn]:
                        continue

                    # checks if the tested number only fits in cubeSolve[(cube + 2) %3] cube's row
                    # if (number + 1 not in cubeSolve[(cubeNumber + 0) % 3][rowOrColumn] and
                    if (number + 1 not in cubeSolve[cubeNumber][rowOrColumn] and
                            number + 1 not in cubeSolve[(cubeNumber + 1) % 3][rowOrColumn]):

                        cubeSolve[(cubeNumber + 2) %3][(rowOrColumn + 1) % 3, :, number] = 0
                        cubeSolve[(cubeNumber + 2) %3][(rowOrColumn + 2) % 3, :, number] = 0


# kijkt of er nog 1 mogelijkheid over is op een plaats (moet na numberLogic)
def mapFiller(sudokuMap, solveMap):
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




def sudokuSolver(sudokuMap, solveMap, options):
    cubeMap = cubeGen(sudokuMap)
    cubeSolve = cubeGen(solveMap)
    if len(duplicateForks) // 1000 == len(duplicateForks) / 1000:
        print(len(duplicateForks))
    while True:
        noChangesCounter = 0
        numberLogic(sudokuMap, solveMap, cubeMap, cubeSolve)
        noChangesCounter += mapFiller(sudokuMap, solveMap)
        noChangesCounter += numberLogic2(sudokuMap, solveMap)
        # sudokuPrint(sudokuMap)
        # print(noChangesCounter)
        if 0 not in sudokuMap:
            for maps in finishedMaps:
                if (maps == sudokuMap).all():
                    return
            finishedMaps.append(sudokuMap)
            # print("Map completed")
            # sudokuPrint(sudokuMap)
            if options == "generate":
                return sudokuPrint(generatedMap)
            break

        if noChangesCounter == 162:
            # print("Map incomplete")
            if options == False:
                sudokuPrint(sudokuMap)
                print(solveMap)
                break
            elif options == True:
                forkLevel = 2
                while forkLevel < 10:
                    for Y in range(9):
                        for X in range(9):
                            if np.count_nonzero(solveMap[Y, X]) == forkLevel:
                                for testNumbers in solveMap[Y, X]:
                                    if testNumbers == 0:
                                        continue
                                    testSudokuMap = np.copy(sudokuMap)
                                    testSudokuMap[Y, X] = testNumbers
                                    duplicate = False
                                    for maps in duplicateForks:
                                        if (maps == testSudokuMap).all() == True:
                                            print(maps == testSudokuMap)
                                            duplicate = True
                                            break
                                    if duplicate == False:
                                        duplicateForks.append(testSudokuMap)
                                        testSolveMap = np.copy(solveMap)
                                        testNumberLogic(testSolveMap, Y, X, testNumbers - 1)
                                        sudokuSolver(testSudokuMap, testSolveMap, True)
                    forkLevel += 1
                break
            elif options == "generate":
                newNumberPlaced = False
                while not newNumberPlaced:
                    Y = random.randrange(9)
                    X = random.randrange(9)
                    if sudokuMap[Y, X] == 0:
                        ohNoTheLoops = 0
                        while not newNumberPlaced:
                            newNumber = random.randrange(9)
                            if solveMap[Y, X, newNumber] != 0:
                                sudokuMap[Y, X] = solveMap[Y, X, newNumber]
                                generatedMap[Y, X] = solveMap[Y, X, newNumber]
                                testNumberLogic(solveMap, Y, X, newNumber)
                                numberLogic(sudokuMap, solveMap, cubeMap,cubeSolve)
                                mapFiller(sudokuMap, solveMap)
                                newNumberPlaced = True
                            ohNoTheLoops += 1
                            if ohNoTheLoops == 50:
                                break
                            # print("stuck in a loop")
                            # print(solveMap)
                            sudokuPrint(sudokuMap)
                            print(Y)
                            print(X)
                            # print(cubeMap[0])

def display():
    return puzzleConvert(testPuzzle)

# cProfile
# numberLogicInit(sudokuMap, solveMap)
# sudokuSolver(sudokuMap, solveMap, True)

generatedMap = puzzleConvert(emptyMap)

emptyMap = puzzleConvert(emptyMap)

# sudokuSolver(emptyMap, solveMap, "generate")


# ff wat testen
# sudokuMap = puzzleConvert(testPuzzle3)
# cubeMap = cubeGen(sudokuMap)
# cubeSolve = cubeGen(solveMap)
# # numberLogic(sudokuMap, solveMap, cubeMap, cubeSolve)
# # mapFiller(sudokuMap, solveMap)
# sudokuPrint(sudokuMap)

#nog een test
sudokuMap = puzzleConvert(testPuzzle4)
cubeMap = cubeGen(sudokuMap)
cubeSolve = cubeGen(solveMap)
numberLogicInit(sudokuMap, solveMap)
numberLogic(sudokuMap, solveMap, cubeMap, cubeSolve)
mapFiller(sudokuMap, solveMap)
numberLogic3(sudokuMap, solveMap, cubeMap, cubeSolve)
print(solveMap)
sudokuPrint(sudokuMap)


# cube nog aan passen