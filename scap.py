import numpy as np
import timeit
henk = np.full(81, 0, dtype="int8").reshape(9, 9)
henk[8, 8] = 2
henk[7, 7] = 2
print(np.any(henk))

print(len(np.nonzero(henk)))
print(henk)
print(np.nonzero(henk))
boer = np.nonzero(henk)
#print([boer[0][0]])
#print(henk[boer])
henk[boer] = 3
print(henk)

#"""
kaas = np.full(9, 0, dtype="int8")
kaas[8] = 2
melk = [0, 0, 0, 0, 0, 0, 0, 0, 2]

#print(melk.count(0))
print(timeit.timeit("melk.count(0)", number=100000, globals=globals()))
print(timeit.timeit("[0, 0, 0, 0, 0, 0, 0, 0, 2].count(0)", number=100000))
print(timeit.timeit("np.nonzero(kaas)", number=100000, globals=globals()))
#"""