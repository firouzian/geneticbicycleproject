#!/usr/bin/env python

import numpy as np
import math
import matplotlib.pyplot as plt

plt.axis([0,10,0,10])
plt.ion()
plt.show()

mass = 1.0
mass_inv = 1.0/mass
g = 10
p_y = 10
p_x = 10
v_y = 0
v_x = 0
radius = 1
young = 10000
wind = 0.001

t_i = 0.0
t_f = 10.0
dt  = 0.0001
t_steps = int((t_f-t_i)/dt)

my_array =[[], []]

#f = open("hight.txt",'w')
#ff = open("time.txt",'w')

for i in range (t_steps):
    xi = p_y - radius
    f_y = -mass*g
    f_x = -mass*wind
    if xi<0:
       f_y = f_y - xi*young    
    a_y = f_y * mass_inv
    a_x = f_x * mass_inv
    v_y = v_y + a_y*dt
    v_x = v_x + a_x*dt
    p_y = p_y + v_y*dt + (a_y*dt*dt)*0.5
    p_x = p_x + v_x*dt + (a_x*dt*dt)*0.5
    t = t_i+i*dt
    if i%1000 == 0:
      # print t, p_y        
       plt.scatter(t,p_y)
       plt.pause(0.02)
     # plt.scatter(t,p_x)
     # plt.pause(0.02)
   # my_array[0].append(p_x)
    my_array[1].append(p_y)
   
print my_array[0]
print my_array[1]
                   
                    

    #np.save(f ,h )
#    f.write("%s\n" % h)
#    f.write(str(h))

 
    #print "hit to ground"    
    #ff.write("%s\n" % t)
    #ff.write(str(t))
    #f.write( h )
    
    #print h
    #print t
plt.show(block=True)