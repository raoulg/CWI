import numpy as np
from numpy.random import random, randint, normal, shuffle

# x = np.random.rand(20)
# x2 = (x*1.5)+0.5 
# x3 = np.ndarray.tolist(x2)

# gistTimeRand = np.random.rand(40) # 40 trials
# gistTimeWiden = gistTimeRand*3+2 # gist tijd tussen 2 en 5 sec
# gistTimeList = np.ndarray.tolist(gistTimeWiden) # use with pop
# gistTime = gistTimeList.pop()
# print(gistTimeList)
# print(gistTime)

directionRand = np.random.random_integers(0, 1, size = 20)
# print(directionRand)
directionWiden = directionRand*2-1
print(directionWiden)