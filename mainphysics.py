#!/usr/bin/env python

import allobjects as aob
import numpy as np
import itertools as it
import matplotlib.pyplot as plt


plt.axis([-10,10,0,30])
plt.ion()
plt.show()


t_i = 0.0
t_f = 10.0
dt  = 0.001
g=10
t_steps = int((t_f-t_i)/dt)

a = aob.AllObjects()

#--------
mass1 = 1.0
mass2 = 1.0

rad1  = 1.0
rad2  = 1.0

position1 = np.array ([3.,5.],float)
position2 = np.array ([4.,9.],float)
position3 = np.array ([8.,4.],float)
position4 = np.array ([11.,10.],float)

a.add_wheel (mass1,position1,rad1)
a.add_wheel (mass2,position2,rad2)
a.add_wheel (mass2,position3,rad1)
a.add_wheel (mass2,position4,rad1)

a.set_spring_const (50.0)
a.set_young_const (10000.0 )
a.set_dissip_const (50.0)
#---------
a.make_ground()
#---------

a.set_springs() # assigns the rest distances of strings

for i in range (t_steps):
    a.update()
    
    t = t_i+i*dt
    if i%100 == 0:
        y1 = a.wheel_list[0].position[1]
        x1 = a.wheel_list[0].position[0]
        
        y2 = a.wheel_list[1].position[1]
        x2 = a.wheel_list[1].position[0]
        
        y3 = a.wheel_list[2].position[1]
        x3 = a.wheel_list[2].position[0]
        
        y4 = a.wheel_list[3].position[1]
        x4 = a.wheel_list[3].position[0]
        #plt.scatter(t,y1)
        #plt.scatter(t,y2)

        plt.cla()
        plt.axis([0.0,20,0,20])
        plt.scatter(x1,y1)
        plt.scatter(x2,y2)
        plt.scatter(x3,y3)
        plt.scatter(x4,y4)  
                     
        plt.pause(0.01)
        
        
        
plt.show(block=False)
