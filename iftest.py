import numpy as np
switch = 0
yRange = np.arange(0.0, 800) # 60 fps, 6 sec = 360 frames. 720 frames voor 120fps.
xFramerate = yRange/60
xCos1 = np.ndarray.tolist((150*np.cos(xFramerate*np.pi)))


print(len(xCos1))
for i in range(1,len(xCos1)):
  print(xCos1.pop())
