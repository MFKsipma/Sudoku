import numpy as np

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

kaas = []
for i in testPuzzle:
    if i == ".":
        kaas.append(0)
    else:
        kaas.append(int(i))

sudokuMap = np.array(kaas)


#sudokuMap = np.array([0] * 81)
#henk = np.array([[0] * 9] * 9)



#henk[1][1] = 3

#print(henk)

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

sudokuPrint(sudokuMap)

boek = np.array([0, 1, 0])
map = np.copy(boek)
print(boek[boek == 0])
print(boek)
print(map)

henk = np.array([[0] * 9] * 9)
henk[:, 1] = 5
print(henk)
#print(np.sum(henk, axis=1))
henk[3] = 4
print(henk)
print(np.where(henk[:, 1] == 4))
print(np.argwhere(henk == 4))

blabla = np.array([[[1, 2, 3, 4, 5, 6, 7, 8, 9]] * 9] * 9, dtype="int8")

#print(blabla)

#blabla = blabla[0, :, 1]

blabla[0, :, 1] = 0
blabla[0, :, 3] = False

print(2 in blabla)

#print(np.isin(blabla[:,2], 2, kind="table" ))

print(blabla)

print(blabla[0, 0, 0] == True)