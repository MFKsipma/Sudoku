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

testPuzzle5 = [['.', '.', '.', '.', '.', '.', '1', '.', '2'],
              ['.', '.', '.', '.', '.', '6', '.', '.', '.'],
              ['.', '.', '.', '.', '.', '.', '3', '.', '.'],
              ['.', '.', '.', '.', '.', '.', '.', '6', '.'],
              ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
              ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
              ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
              ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
              ['.', '.', '.', '.', '.', '.', '.', '.', '.']]

testPuzzle6 = [['.', '2', '3', '4', '5', '6', '7', '8', '.'],
              ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
              ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
              ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
              ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
              ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
              ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
              ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
              ['.', '.', '.', '.', '.', '.', '.', '.', '1']]

testPuzzle7 = [['.', '.', '.', '.', '.', '.', '.', '.', '.'],
              ['1', '2', '3', '.', '.', '.', '7', '8', '9'],
              ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
              ['.', '.', '.', '.', '1', '1', '.', '.', '.'],
              ['.', '.', '.', '.', '2', '2', '.', '.', '.'],
              ['.', '.', '.', '.', '3', '3', '.', '.', '.'],
              ['.', '.', '.', '.', '7', '7', '.', '.', '.'],
              ['.', '.', '.', '.', '8', '8', '.', '.', '.'],
              ['.', '.', '.', '.', '9', '9', '.', '.', '.']]

testPuzzle8 = [['.', '1', '.', '.', '.', '.', '.', '.', '.'],
              ['.', '2', '.', '.', '.', '.', '.', '.', '.'],
              ['.', '3', '.', '.', '.', '.', '.', '.', '.'],
              ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
              ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
              ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
              ['.', '7', '.', '.', '.', '.', '.', '.', '.'],
              ['.', '8', '.', '.', '.', '.', '.', '.', '.'],
              ['.', '9', '.', '.', '.', '.', '.', '.', '.']]

testPuzzle9 = [['.', '.', '.', '.', '.', '.', '.', '.', '.'],
              ['.', '.', '.', '.', '.', '.', '7', '8', '9'],
              ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
              ['4', '4', '4', '.', '.', '.', '.', '.', '.'],
              ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
              ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
              ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
              ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
              ['.', '.', '.', '.', '.', '.', '.', '.', '.']]

testPuzzle10 = [['1', '2', '3', '4', '5', '6', '7', '8', '9'],
              ['4', '5', '6', '.', '.', '.', '.', '.', '.'],
              ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
              ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
              ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
              ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
              ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
              ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
              ['.', '.', '.', '.', '.', '.', '.', '.', '.']]

testPuzzle11 = [['.', '.', '.', '.', '.', '.', '1', '.', '.'],
              ['1', '3', '7', '.', '.', '.', '2', '8', '9'],
              ['.', '.', '.', '.', '.', '.', '3', '.', '.'],
              ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
              ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
              ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
              ['.', '.', '.', '.', '.', '.', '7', '.', '.'],
              ['.', '.', '.', '.', '.', '.', '8', '.', '.'],
              ['.', '.', '.', '.', '.', '.', '9', '.', '.']]

# convert oude map naar nieuwe map
# testPuzzle = testPuzzle00

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
def numberLogic2(sudokuMap, solveMap, cubeMap, cubeSolve):
    noChangesCounter = 81
    for i in range(9):
        for number in range(9):
            # horizontal
            possibleNumbers = np.nonzero(solveMap[i, :, number])
            if len(possibleNumbers[0]) == 1:
                sudokuMap[i, possibleNumbers[0][0]] = solveMap[i, possibleNumbers[0][0], number]
                testNumberLogic(solveMap, i, possibleNumbers[0][0], number)
                noChangesCounter += -1

            # vertical
            possibleNumbers = np.nonzero(solveMap[:, i, number])
            if len(possibleNumbers[0]) == 1:
                sudokuMap[possibleNumbers[0][0], i] = solveMap[possibleNumbers[0][0], i, number]
                testNumberLogic(solveMap, possibleNumbers[0][0], i, number)
                noChangesCounter += -1

            # block
            # possibleNumbers = np.nonzero(solveMap[cube[i][0]: cube[i][0] + 3, cube[i][1]: cube[i][1] + 3, number])
            # if len(possibleNumbers[0]) == 1:
            #     sudokuMap[cube[i][0] + possibleNumbers[0][0], cube[i][1] + possibleNumbers[1][0]] = number + 1
            #     testNumberLogic(solveMap, cube[i][0] + possibleNumbers[0][0], cube[i][1] + possibleNumbers[1][0], number)
            #     noChangesCounter += -1

            # block 2
            possibleNumbers = np.nonzero(cubeSolve[i][:, :, number])
            if len(possibleNumbers[0]) == 1:
                cubeMap[i][possibleNumbers[0][0], possibleNumbers[1][0]] = number + 1
                y = possibleNumbers[0][0] + (i // 3) * 3
                x = possibleNumbers[1][0] + (i % 3) * 3
                testNumberLogic(solveMap, y, x, number)
                noChangesCounter += -1

    return noChangesCounter


#excludes numbers from the same cube in other rows/columns if they only fit in the cube's tested row/column
def numberLogic3(sudokuMap, solveMap, cubeMap, cubeSolve):
    for cubeNumber in range(9):
        # columns and rows consisting of 3 rows
        for rowOrColumn in range(3):
            # rowOrColumn += threeRowOrColumn
            for number in range(9):


                # horizontal
                # checks if row is already solved
                if len(np.nonzero(solveMap[(cubeNumber // 3) * 3 + rowOrColumn])) > 0:

                    # checks if the tested number is already in the row
                    if number + 1 in sudokuMap[(cubeNumber // 3) * 3 + rowOrColumn]:
                        continue

                    # checks if the tested number only fits in cubeSolve[(cubeNumber // 3) * 3 + ((cubeNumber + 2) % 3)] cube's row and not in the other rows of that cube
                    if (number + 1 not in cubeSolve[(cubeNumber // 3) * 3 + ((cubeNumber + 0) % 3)][rowOrColumn] and
                            number + 1 not in cubeSolve[(cubeNumber // 3) * 3 + ((cubeNumber + 1) % 3)][rowOrColumn]):
                        cubeSolve[(cubeNumber // 3) * 3 + ((cubeNumber + 2) % 3)][(rowOrColumn + 1) % 3, :, number] = 0
                        cubeSolve[(cubeNumber // 3) * 3 + ((cubeNumber + 2) % 3)][(rowOrColumn + 2) % 3, :, number] = 0


                # vertical
                # checks if row is already solved
                if len(np.nonzero(solveMap[:, (cubeNumber % 3) * 3 + rowOrColumn])) > 0:

                    # checks if the tested number is already in the row
                    if number + 1 in sudokuMap[:, (cubeNumber % 3) * 3 + rowOrColumn]:
                        continue

                    # checks if the tested number only fits in cubeSolve[(cubeNumber + 6) % 9] cube's column and not in the other columns of that cube
                    if (number + 1 not in cubeSolve[(cubeNumber + 0) % 9][:, rowOrColumn] and
                            number + 1 not in cubeSolve[(cubeNumber + 3) % 9][:, rowOrColumn]):
                        cubeSolve[(cubeNumber + 6) % 9][:, (rowOrColumn + 1) % 3, number] = 0
                        cubeSolve[(cubeNumber + 6) % 9][:, (rowOrColumn + 2) % 3, number] = 0


# stops the option for numbers in a cube, if thus those numbers have to be placed in a different cube
def numberLogic4(sudokuMap, solveMap, cubeMap, cubeSolve):
    # for cubeNumber in range(9):
    #     # columns and rows consisting of 3 rows
    #     for rowOrColumn in range(3):
    #         # tests if there are only 3 possible numbers in a cube row
    #         if (np.count_nonzero(cubeMap[cubeNumber][rowOrColumn]) == 0 and
    #                 np.count_nonzero(cubeSolve[cubeNumber][rowOrColumn]) == 9):
    #             # removes possible number from other cubes of the same row
    #             for number in range(9):
    #                 if cubeSolve[cubeNumber][rowOrColumn, 0, number] != 0:
    #                     print("het gebeurt")
    #                     cubeSolve[(cubeNumber // 3) * 3 + ((cubeNumber + 1) % 3)][rowOrColumn, :, number] = 0
    #                     cubeSolve[(cubeNumber // 3) * 3 + ((cubeNumber + 2) % 3)][rowOrColumn, :, number] = 0
    for cubeNumber in range(9):
        # columns and rows consisting of 3 rows
        for rowOrColumn in range(3):
            # tests if there are only 3 possible numbers in a cube row
            if (np.count_nonzero(cubeMap[cubeNumber][rowOrColumn]) == 0 and
                    len(np.unique(cubeSolve[cubeNumber][rowOrColumn])) == 4):
                # removes possible number from other cubes of the same row
                for number in range(9):
                    if cubeSolve[cubeNumber][rowOrColumn, 0, number] != 0:
                        cubeSolve[(cubeNumber // 3) * 3 + ((cubeNumber + 1) % 3)][rowOrColumn, :, number] = 0
                        cubeSolve[(cubeNumber // 3) * 3 + ((cubeNumber + 2) % 3)][rowOrColumn, :, number] = 0


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



def sudokuChecker(sudokuMap, cubeMap):
    # if 0 in sudokuMap:
    #     print("invalid sudoku")
    #     return
    for rowOrColumnOrCube in range(9):
        if len(np.unique(sudokuMap[rowOrColumnOrCube])) != 9:
            print(f"invalid sudoku. row {rowOrColumnOrCube}")
            return
        if len(np.unique(sudokuMap[:, rowOrColumnOrCube])) != 9:
            print(f"invalid sudoku. column {rowOrColumnOrCube}")
            return
        if len(np.unique(cubeMap[rowOrColumnOrCube])) != 9:
            print(f"invalid sudoku. cube {rowOrColumnOrCube}")
            return
    print("valid map")





def sudokuSolver(sudokuMap, solveMap, options):
    cubeMap = cubeGen(sudokuMap)
    cubeSolve = cubeGen(solveMap)
    if len(duplicateForks) // 10 == len(duplicateForks) / 10:
        print(len(duplicateForks))
    while True:
        noChangesCounter = 0
        numberLogic(sudokuMap, solveMap, cubeMap, cubeSolve)
        noChangesCounter += mapFiller(sudokuMap, solveMap)
        noChangesCounter += numberLogic2(sudokuMap, solveMap, cubeMap, cubeSolve)
        numberLogic3(sudokuMap, solveMap, cubeMap, cubeSolve)
        numberLogic4(sudokuMap, solveMap, cubeMap, cubeSolve)
        # sudokuPrint(sudokuMap)
        # print(noChangesCounter)
        if 0 not in sudokuMap:
            if options != "menyTest":
                for maps in finishedMaps:
                    if (maps == sudokuMap).all():
                        return
            finishedMaps.append(sudokuMap)
            # print("Map completed")
            sudokuPrint(sudokuMap)
            sudokuChecker(sudokuMap, cubeMap)
            if options == "generate":
                return sudokuPrint(generatedMap)
            break

        #noChangeCounter aanpassen als je mapfiller weer gaat gebruiken naar 162
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
            # logica 3 nodig
            elif options == "menyTest":
                for Y in range(9):
                    for X in range(9):
                        if np.count_nonzero(solveMap[Y, X]) > 1:
                            for testNumbers in solveMap[Y, X]:
                                if testNumbers == 0:
                                    continue
                                testSudokuMap = np.copy(sudokuMap)
                                testSudokuMap[Y, X] = testNumbers
                                testSolveMap = np.copy(solveMap)
                                testNumberLogic(testSolveMap, Y, X, testNumbers - 1)

                                # dit kan weer weg V
                                duplicateForks.append(testSudokuMap)

                                print(solveMap)
                                print("--------------------------")
                                print((testSolveMap))
                                sudokuPrint(sudokuMap)
                                sudokuSolver(testSudokuMap, testSolveMap, "menyTest")
                            return

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


generatedMap = puzzleConvert(emptyMap)
#
emptyMap = puzzleConvert(emptyMap)

# sudokuSolver(emptyMap, solveMap, "generate")

sudokuMap = puzzleConvert(testPuzzle1)
numberLogicInit(sudokuMap, solveMap)
sudokuSolver(sudokuMap, solveMap, "menyTest")


# ff wat testen
# sudokuMap = puzzleConvert(testPuzzle3)
# cubeMap = cubeGen(sudokuMap)
# cubeSolve = cubeGen(solveMap)
# # numberLogic(sudokuMap, solveMap, cubeMap, cubeSolve)
# # mapFiller(sudokuMap, solveMap)
# sudokuPrint(sudokuMap)

#nog een test numberlogic3
# sudokuMap = puzzleConvert(testPuzzle11)
# cubeMap = cubeGen(sudokuMap)
# cubeSolve = cubeGen(solveMap)
# numberLogicInit(sudokuMap, solveMap)
# numberLogic(sudokuMap, solveMap, cubeMap, cubeSolve)
# mapFiller(sudokuMap, solveMap)
# numberLogic3(sudokuMap, solveMap, cubeMap, cubeSolve)
# print(solveMap)
# sudokuPrint(sudokuMap)


# cube nog aan passen

#nog een test numberlogic 2
# counter = 0
# sudokuMap = puzzleConvert(testPuzzle5)
# numberLogicInit(sudokuMap, solveMap)
# cubeMap = cubeGen(sudokuMap)
# cubeSolve = cubeGen(solveMap)
# while counter < 5:
#     counter += 1
#     numberLogic(sudokuMap, solveMap, cubeMap, cubeSolve)
#     # mapFiller(sudokuMap, solveMap)
#     numberLogic2(sudokuMap, solveMap, cubeMap, cubeSolve)
# print(solveMap[:3])
# sudokuPrint(sudokuMap)


#nog een test numberlogic4
# sudokuMap = puzzleConvert(testPuzzle10)
# cubeMap = cubeGen(sudokuMap)
# cubeSolve = cubeGen(solveMap)
# numberLogicInit(sudokuMap, solveMap)
# numberLogic(sudokuMap, solveMap, cubeMap, cubeSolve)
# mapFiller(sudokuMap, solveMap)
# print(solveMap[1:3])
# numberLogic4(sudokuMap, solveMap, cubeMap, cubeSolve)
# print("--------------------------")
# print(solveMap[1:3])
# sudokuPrint(sudokuMap)



#nog een test sudokuChecker
# sudokuMap = puzzleConvert(testPuzzle10)
# cubeMap = cubeGen(sudokuMap)
# cubeSolve = cubeGen(solveMap)
# numberLogicInit(sudokuMap, solveMap)
# numberLogic(sudokuMap, solveMap, cubeMap, cubeSolve)
# mapFiller(sudokuMap, solveMap)
# # numberLogic4(sudokuMap, solveMap, cubeMap, cubeSolve)
# # print(solveMap[0:3])
# sudokuChecker(sudokuMap, cubeMap)
# sudokuPrint(sudokuMap)





#mapFiller niet nodig !?
