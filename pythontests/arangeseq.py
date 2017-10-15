import numpy as np
list = np.arange(0.5, 1.3, 0.1) # snelheden tussen 0.5 en 1.2, in stappen van 0.1
xvelWiden = np.repeat(list, 4) # repeat voor 4 objecten
x = xvelWiden[::-1]
xvelList = np.ndarray.tolist(xvelWiden)

print(x)
