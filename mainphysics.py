#!/usr/bin/env python

import allobjects as aob
import numpy as np
import itertools as it
import matplotlib.pyplot as plt
import ground


def run_all (gene, UP):

    t_i = 0.0
    t_f = 10.0
    dt  = 0.001

    mass_wheel = 1.0
    mass_parti = 100.0

    rad1  = 1.0
    rad2  = 1.0

    torque_1 = 1000.0
    torque_2 = 1000.0

    young_const   = 10000
    ground_dissip = 50.0
    spring_dissip = 5.0


# ===================
    the_ground = ground.Create_Ground(UP)

    a = aob.AllObjects (the_ground)

    spring_const = gene.SC

    pos_wheel_1 = np.array ([gene.W1_x, gene.W1_y],float)
    pos_wheel_2 = np.array ([gene.W2_x, gene.W2_y],float)
    pos_parti_1 = np.array ([gene.M1_x, gene.M1_y],float)
    pos_parti_2 = np.array ([gene.M2_x, gene.M2_y],float)

    a.add_wheel (mass_wheel, pos_wheel_1, rad1, torque_1)
    a.add_wheel (mass_wheel, pos_wheel_2, rad2, torque_2)
    a.add_wheel (mass_parti, pos_parti_1)
    a.add_wheel (mass_parti, pos_parti_2)

    a.set_spring_const (spring_const)
    a.set_young_const (young_const )
    a.set_gr_dissip_const (ground_dissip)
    a.set_dissip_const ( spring_dissip )

    a.make_ground()

    a.set_springs() # assigns the rest distances of strings

    initial_position = a.wheel_list[0].position[0]

    t_steps = int((t_f-t_i)/dt)
    for i in range (t_steps):
        a.update()
        t = t_i+i*dt
        if a.ground_hit:
            dist = a.wheel_list[0].position[0] - initial_position
            return dist, gene

    dist = a.wheel_list[0].position[0] - initial_position
    return dist, gene

##-------------------------------------
##-------------------------------------
##-------------------------------------


if __name__ == '__main__':

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

    rad1  = 3.0
    rad2  = 1.0

    torque1 = 3000.0

    position1 = np.array ([3.,5.],float)
    position2 = np.array ([4.,9.],float)
    position3 = np.array ([8.,4.],float)
    position4 = np.array ([11.,10.],float)

    a.add_wheel (mass1,position1,rad1, torque1)
    a.add_wheel (mass2,position2)
    a.add_wheel (mass2,position3,rad1, torque1)
    a.add_wheel (mass2,position4)

    a.set_spring_const (50.0)
    a.set_young_const (10000.0 )
    a.set_gr_dissip_const (50.0)
    a.set_dissip_const (1.1)
#---------
    a.make_ground()
#---------

    a.set_springs() # assigns the rest distances of strings

    initial_position = a.wheel_list[0].position[0]

    for i in range (t_steps):
        a.update()
        if a.ground_hit:
            print 'ground hit'
            print a.wheel_list[0].position[0] - initial_position
            exit()
    
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
            plt.axis([0.0,50,0,50])
            plt.scatter(x1,y1)
            plt.scatter(x2,y2)
            plt.scatter(x3,y3)
            plt.scatter(x4,y4)  
                     
            plt.pause(0.005)
        
        
        
    plt.show(block=False)
