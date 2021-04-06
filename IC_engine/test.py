import numpy as np

f = open("temp_2","r")

lines = f.readlines()
x = []
y = []
z = []

for i in lines:
	x.append(i.split('   ')[0])

for i in lines:
	y.append(i.split('   ')[1])

for i in lines:
	z.append(i.split('   ')[2])

f.close()

xl = [float(i) for i in x]
yl = [float(i) for i in y]
zl = [float(i) for i in z]

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.scatter(xl,yl,zl)

plt.show()