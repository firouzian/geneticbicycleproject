
'''
This program reads an input file whith the position of the objects over time 
and generetes the animation of that. The objects are 2 masses and 2 wheels, all 
joined by springs. It also takes a ground string from another file. 
'''

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from ground import Create_Ground
from user_parameters import User_Parameters
from scipy.misc import imread
import matplotlib.cbook as cbook
# -------------------Set User Parameters Values--------------------------- 
# (we can ask this by command line, but first is easier to just hardcode it)

# Box in wich the bicycle can appear in the first generation of genes
x_min = 0
y_min = 0
x_max = 10
y_max = 10
# Max value of the Spring Constant for the first generation of genes 
SC_max = 50
# Parameters for the Ground in wich the bicycle will move
amplitude = 0
slope = -0.1

UP=User_Parameters(x_min, y_min, x_max, y_max, SC_max,amplitude,slope)


# ------------------------ANIMATION----------------------------------
# The data of the position of each element in the graph is generated 
# by the Physics function and stored in a file.
f = open('Positions.txt','r') 
i = 0
all_file = []
for line in f: 
    words = line.split()
    all_file.append(words)
    i+=1
f.close()


# Each line refers to the coordinate of a certain object
M1_x = all_file[0]
M1_y = all_file[1]
M2_x = all_file[2]
M2_y = all_file[3]
W1_x = all_file[4] 
W1_y = all_file[5]
W2_x = all_file[6]
W2_y = all_file[7]


# Create the Ground in wich the Bicycle will move
GR = Create_Ground(UP)
GR_x = []
GR_y = []
for l in range(len(GR)):
    GR_x.append(GR[l][0])
    GR_y.append(GR[l][1])


# Initialize the figure and all the graphics in it 
fig, ax = plt.subplots()
ax.set_xlim(-2, 20)
ax.set_xlabel('Distance: d')
ax.set_ylim(-5, 2), ax.set_yticks([])
# A scatter for the differents objects
scat = ax.scatter([],[], c = ('black','black','grey','grey'), alpha=0.9)
# A line for the springs
line, = ax.plot([], [], '-', lw=2, alpha=0.9)
# A line for the ground
line2, = ax.plot([], [], '-', lw=4, c='black', alpha=1)


# Back Image (IT CAN BE CHANGED)
img = imread('image.png')


# We define the state of the graph for given [i] value
def animate(i):
    # Defines the values of the line plot (we want lines between every object)
    otherx = [M1_x[i], M2_x[i], W1_x[i], W2_x[i], M1_x[i], W1_x[i], W2_x[i], M2_x[i]]
    othery = [M1_y[i], M2_y[i], W1_y[i], W2_y[i], M1_y[i], W1_y[i], W2_y[i], M2_y[i]]
    line.set_data(otherx, othery)
    
    # Defines the values of the scatter plot
    thisx = [M1_x[i], M2_x[i], W1_x[i], W2_x[i]]
    thisy = [M1_y[i], M2_y[i], W1_y[i], W2_y[i]]
    scat.set_offsets(np.column_stack((thisx, thisy))) 
    scat.set_sizes(np.asarray([150.,150.,1500.,1500.]))
    
    # Defines the values of the line plot for ground    
    line2.set_data(GR_x, GR_y)
    
    return scat, line, line2


# Animation function iterates over [i] and refresh the screen with a different scatter plot
# after a given interval of time
fig.ani = animation.FuncAnimation(fig, animate, np.arange(1, len(M1_x)),interval=50, blit=False)


# Show the back image and the animation over it
plt.imshow(img, zorder=0, extent=[-2, 20, -5, 2], alpha=0.7)
plt.show()