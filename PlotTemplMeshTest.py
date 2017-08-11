#! /usr/bin/env python
#
# An inflated brain mesh read from face and vertex text files
#
# AS

from matplotlib import pyplot as plt
import numpy as np

fi = 'faces.txt'
vi = 'verts.txt'


# load faces as int32 (i4)
def loadf(x):
	o = np.loadtxt(open(x, "rb"), delimiter=",", dtype="i4", skiprows=0)
	return [o]
# load vertices as float (f8)
def loadv(x):
	o = np.loadtxt(open(x, "rb"), delimiter=",", dtype="f8", skiprows=0)
	return [o]

f = loadf(fi)
v = loadv(vi)

# get the numpy arrays from list
f = f[0]
v = v[0]


limits = [v.min(), v.max()]
cmap   = 'coolwarm'

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d', xlim=limits, ylim=limits)
ax.view_init(elev=90, azim=-90)
ax.set_axis_off()

# note faces are [f-1] so that max(f) < len(v)
p3dcollec = ax.plot_trisurf(v[:, 0], v[:, 1], v[:, 2],
                            triangles=f-1, linewidth=0.,
                            antialiased=False,
                            color='white')

