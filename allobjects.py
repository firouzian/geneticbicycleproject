import numpy as np
import itertools as it
import wheel 
#import ground


#in this class define all object needed: wheel- particle-spring and ground
# at this class define update the position and velocity and claculate force

class AllObjects(object):
    def __init__(self):
        print "AllObjects"
        self.wheel_list = []
        self.spring_list = {}
        self.dt = 0.001
        self.spring_const = 1.0
        self.young_const = 1.0
        self.dissip_const = 0.0
        self.gravity = 10.
#        w1 = wheel.Wheel()
#        self.wheel_list.append(w1)
        
    def update(self):
        self.calculate_forces() 
        self.update_positions()
       # return None
        
    def set_springs(self):
        for w in list(it.combinations_with_replacement(self.wheel_list,2)):
            if w[0] != w[1]:
                i = self.wheel_list.index(w[0])
                j = self.wheel_list.index(w[1])
                x0 = np.linalg.norm(w[0].position - w[1].position)
                self.spring_list[(i,j)] = x0
                #print self.spring_list
            

            
    def calc_spring_force (self,i,j):
            ff = np.array([0.,0.],float)
            w_i = self.wheel_list[i]
            w_j = self.wheel_list[j]
            direct = w_i.position - w_j.position 
            direct_dist = np.linalg.norm ( direct )
            inv_direct_dist=1.0/direct_dist
            direct_norm = direct*inv_direct_dist
            xi = direct_dist -   self.spring_list[(i,j)] 
            force = xi * self.spring_const
            ff = force * direct_norm
            w_i.add_force ( -ff )
            w_j.add_force ( +ff )                  
    
    def calculate_forces(self):
        for w_i in self.wheel_list:
            w_i.force = 0.

        
        self.calc_spring_force (0,1)
        self.calc_spring_force (0,2)
        self.calc_spring_force (0,3)
        self.calc_spring_force (1,2)        
        self.calc_spring_force (1,3)
        self.calc_spring_force (2,3)
            
        for w_i in self.wheel_list:
            force_mg = - w_i.mass * self.gravity
            xi = w_i.position[1] - w_i.radius
            xi_dot = w_i.velocity[1]
            force_gr = 0
            if  xi < 0: 
                force_gr = - xi * 10000 - self.dissip_const*xi_dot
            ff = np.array([0.,0.],float)
            ff[1] = force_mg + force_gr
            w_i.add_force ( ff )
            #print w_i.force
            
            
       # return None
            
    def update_positions (self):
        for w in self.wheel_list:
            w.integrate (self.dt)
       # return None 
    
    def add_wheel(self,mass,position,radius):
        w = wheel.Wheel(mass,position,radius)
        self.wheel_list.append(w)
        
    def make_ground(self):
        return None
    
    def set_spring_const(self,sp):
        self.spring_const = sp
    
    def set_young_const(self,sp):
        self.young_const = sp
    
    def set_dissip_const(self,sp):
        self.dissip_const = sp
        
    def print_wheel(self,i):
        print self.wheel_list[i].position
        
