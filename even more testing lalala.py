import numpy as np
henk = np.zeros((9, 9, 9), "int8")
henk[:] = 8
print(henk)
print(np.nonzero(henk))