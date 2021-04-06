import math
import numpy as np

c = np.array([-37.5, -37.5, -22.8, -20.8, -20.8, -33, -3, -3, -6, -12, -16.8, -30.5])
d = np.array([0,90,90,96.5,106.5,130,130,100,98,97,90,0])

theta = 45

#tx = c * math.cos(math.radians(theta))
#tz = c * math.sin(math.radians(theta))

#for i in range(len(tx)):
#	print(tx[i], d[i] , tz[i])


e = np.array([-20.8])

f = e * math.cos(math.radians(theta))
g = e * math.sin(math.radians(theta))

for i in range(len(f)):
	print(f[i],g[i])
