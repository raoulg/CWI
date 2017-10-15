import numpy as np
list = np.arange(0.5, 1.3, 0.1) # snelheden tussen 0.5 en 1.2, in stappen van 0.1
xvelWiden = np.repeat(list, 4) # repeat voor 4 objecten
apnd = xvelWiden[0]
print(xvelWiden)
print(apnd)
#x1 = xvelWiden[::-1]
#x = np.append(x1, apnd)
#print(x)