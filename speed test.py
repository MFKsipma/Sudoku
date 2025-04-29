import numpy as np

import time
from datetime import timedelta
start_time = time.monotonic()

blabla = np.array([[[1, 2, 3, 4, 5, 6, 7, 8, 9]] * 9] * 9, dtype="int8")



blabla[0, :, 1] = 0

#for i in range(10000):
#    henk = 2 in blabla
#print(henk)

for i in range(10000):
    henk = np.isin(blabla, 2)
print(True in henk)

end_time = time.monotonic()
print(timedelta(seconds=end_time - start_time))