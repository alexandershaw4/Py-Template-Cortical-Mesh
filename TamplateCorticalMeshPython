#! /usr/bin/env python
#
#
# AS

from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import nibabel as nb
from nibabel import gifti


g = 'cortex_20484.surf.gii'

v, f = gifti.read(g).getArraysFromIntent(1008)[0].data, \
       gifti.read(g).getArraysFromIntent(1009)[0].data


limits = [v.min(), v.max()]
cmap   = 'coolwarm'

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d', xlim=limits, ylim=limits)
ax.view_init(elev=0, azim=0)
ax.set_axis_off()

p3dcollec = ax.plot_trisurf(v[:, 0], v[:, 1], v[:, 2],
                            triangles=f, linewidth=0.,
                            antialiased=False,
                            color='white')
