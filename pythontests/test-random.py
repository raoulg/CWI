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

# directionRand = np.random.random_integers(0, 1, size = 20)
# # print(directionRand)
# directionWiden = directionRand*2-1
# print(directionWiden)

# 
# rowList = np.ndarray.tolist(rowAr)
# print(rowList)
# print(np.shuffle(rowList))


# rowCond1 = rowSh[0:20]
# rowCond2 = rowSh[21:41]
# rowCond3 = rowSh[42:62]

# xposList = [-250, 250] # initial list
# rowInit = np.arange(80)
# xposRep = np.repeat(xposList, 10) # repeat for 120 gist images
# print(type(xposRep))
# print(type(rowInit))

# xpos = np.ndarray.tolist(xposRep) # change objecttype to use .pop
# rowAr = np.ndarray.tolist(rowInit)
# print(xpos)
# print(rowAr)

# x = shuffle(xpos)
# y = shuffle(rowAr)
# print(x)
# print(y)

rowAr = np.arange(80)
rowList = np.ndarray.tolist(rowAr)
shuffle(rowList)
rowCond1Full = rowList[0:20]
rowCond2Full = rowList[21:41]
rowCond3Full = rowList[42:62]
print(rowCond1Full)
print(rowCond2Full)
print(rowCond3Full)
# print(type(rowCond1Full.pop()))
# # rowCond2 = rowCond2Full.pop()
# # rowCond3 = rowCond3Full.pop()
# print(slice(5, 6))
# print(random(4)*10)

# print(np.random.random_integers(0, 1, size = 10))

