# The plot server must be running
# Go to http://localhost:5006/bokeh to view this plot

from __future__ import division

import numpy as np

from bokeh.plotting import *

N = 20
img = np.empty((N,N), dtype=np.uint32)
view = img.view(dtype=np.uint8).reshape((N, N, 4))
for i in range(N):
    for j in range(N):
        view[i, j, 0] = int(i/N*255)
        view[i, j, 1] = 158
        view[i, j, 2] = int(j/N*255)
        view[i, j, 3] = 255

output_server("image_rgba")

p = figure(x_range=[0,10], y_range=[0,10])
p.image_rgba(image=[img], x=[0], y=[0], dw=[10], dh=[10])

show(p)  # open a browser
