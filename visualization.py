#!/usr/bin/env python
import matplotlib.pyplot as mpl

# enable animation mode
mpl.ion()

# define the figure hierarchy (figure holds axes)
figure = mpl.figure()
axes = figure.add_subplot('111',aspect='equal')
axes.set_xlim(-2,7)
axes.set_ylim(-2,7)

# add a patch to the axis
ball = mpl.Circle((0,0), radius=2)
axes.add_patch(ball)

# shift the ball's position
for i in range(50):
        ball.center = (i/10.,i/15.)
        mpl.draw()

# afterwards, switch to zoomable GUI mode
mpl.ioff()
mpl.show()
