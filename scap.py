import numpy as np
henk = np.full(81, 0, dtype="int8").reshape(9, 9)
henk[8, 8] = 2
henk[7, 7] = 2
print(np.any(henk))

print(len(np.nonzero(henk)))
print(henk)