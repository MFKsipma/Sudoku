import numpy as np
import random

# print(random.randrange(100))
henk = np.zeros((9, 9, 9), "int8")
# # henk[3:5, :] = 8
# henk[2,3,4] = 8
# henk[1,2,3] = 8
# print(henk)
# print(np.nonzero(henk))
# print(np.flatnonzero(henk))
# print(np.ndarray.nonzero(henk))
# print(np.count_nonzero(henk))
#
# kaas = np.copy(henk)
melk = np.zeros((9, 9, 9), "int8")
# henk[:] = 8
# # print(henk)
# print(kaas)
# print((henk == melk).all())

kaas = np.zeros((9, 9, 9), "int8")
kaas[4, 5, 3] = 2
kaas[2, 3, 1] = 2
# print(np.nonzero(kaas))

# cubeNumber = 8
# print((cubeNumber // 3) * 3 + ((cubeNumber + 0) % 3))
# print((cubeNumber // 3) * 3 + ((cubeNumber + 1) % 3))
# print((cubeNumber // 3) * 3 + ((cubeNumber + 2) % 3))

# print(np.count_nonzero(kaas))

# print(len(np.unique(kaas)))

# print(np.count_nonzero(kaas))
# print(np.unique(kaas))

blabla = np.ones((4,4), "int8")
# print(blabla)

blabla[2] = 0

print(blabla[2:])
print("hoi")
print(blabla[2:][blabla[2:] != 0])

# print(blabla)
for i in range(20):
    print(random.randrange(9))