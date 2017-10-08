import numpy as np
from numpy.random import random, randint, normal, shuffle

x = np.random.rand(20)
x2 = (x*1.5)+0.5 
x3 = np.ndarray.tolist(x2)
print(x3.pop())