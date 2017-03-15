import numpy as np
import itertools as it
import wheel 


#in this class define all object needed: wheel- particle-spring and ground
# at this class define update the position and velocity and claculate force

class AllObjects(object):
    def __init__(self,ground=[(-10.0,5.0),(10.0,0.0),(50.0,5.0)]):
        print "AllObjects"
        self.wheel_list = []
        self.spring_list = {}
        self.dt = 0.001
        self.spring_const = 1.0
        self.young_const = 1.0
        self.dissip_const = 0.0
        self.gr_dissip_const = 0.0
        self.gravity = 10.
        self.ground_tuple = ground     # list of tuples
        self.ground_array = []   # list of numpy array
        self.ground_parallel = [] # vector parallel to each section of the ground
        self.ground_normal = []
        self.ground_hit = False
        
    def update(self):
        self.calculate_forces() 
        self.update_positions()

        
    def set_springs(self):
        no_wheels = len (self.wheel_list)
        for i in range (no_wheels):
            for j in range (i+1,no_wheels):
                xi_i = np.linalg.norm(self.wheel_list[i].position - self.wheel_list[j].position)
                self.spring_list[(i,j)] = xi_i
            
    def calc_spring_force (self,i,j):
            ff = np.array([0.,0.],float)
            w_i = self.wheel_list[i]
            w_j = self.wheel_list[j]
            d_p = w_i.position - w_j.position
            d_v = w_i.velocity - w_j.velocity
            norm_d_p = np.linalg.norm ( d_p )
            norm_d_v = np.linalg.norm ( d_v )
            inv_norm_d_p = 1.0 / norm_d_p
            dir_vec = d_p * inv_norm_d_p
            xi = norm_d_p - self.spring_list[(i,j)] 
            force = xi * self.spring_const - d_v * self.dissip_const
            force_vec = force * dir_vec
            w_i.add_force ( -force_vec )
            w_j.add_force ( +force_vec )                  
    
    def calculate_forces(self):
        for w_i in self.wheel_list:
            w_i.force = 0.

        no_wheels = len (self.wheel_list)
        for i in range (no_wheels):
            for j in range (i+1,no_wheels):
                self.calc_spring_force (i,j)

        self.calc_gravity_force()
        self.calc_ground_force()
#        self.calc_flat_ground_force()



    def calc_gravity_force (self):
        for w_i in self.wheel_list:
            force_mg = - w_i.mass * self.gravity
            force_vec = np.array([0.,0.],float)
            force_vec[1] = force_mg
            w_i.add_force ( force_vec )


    def calc_ground_force (self):
        gr = self.ground_array
        gr_len = len(gr)
        for w_i in self.wheel_list:
            p_i = w_i.position
            r_i = w_i.radius
            for j in range(gr_len - 1):
                vec1 = p_i - gr[j]
                vec2 = self.ground_parallel[j]
                dot_vec1_2 = np.dot (vec1, vec2)
                vec3 = dot_vec1_2 * vec2
                p_x = gr[j] + vec3
                vec4 = self.ground_normal[j]      
                dot_vec1_4 = np.dot (vec1, vec4)

                p_l = gr[j] - (r_i * vec2)
                p_r = gr[j+1] + (r_i * vec2)

                dis_x  = np.linalg.norm (p_x - p_l)
                dis_j0 = np.linalg.norm (gr[j] - p_l)
                dis_j1 = np.linalg.norm (gr[j+1] - p_l)
                dis_j2 = np.linalg.norm (p_r - p_l)

                xi = 0
                if 0.0 < dis_x and dis_x <= dis_j0:
                    r_ii = np.sqrt((r_i*r_i) - (r_i-dis_x)*(r_i-dis_x))
                    xi = dot_vec1_4 - r_ii
                if dis_j0 < dis_x and dis_x <= dis_j1:
                    xi = dot_vec1_4 - r_i
                if dis_j1 < dis_x and dis_x <= dis_j2:
                    r_ii = np.sqrt((r_i*r_i) - (dis_j1-dis_x)*(dis_j1-dis_x))
                    xi = dot_vec1_4 - r_ii

                if xi < 0:
                    force = -xi * self.young_const * vec4
                    if w_i.torque>0:
                        force += -xi*w_i.torque * vec2
                    w_i.add_force (force)
                    if r_i == 0:
                        self.ground_hit = True

                
    def calc_flat_ground_force (self):
        for w_i in self.wheel_list:
            xi = w_i.position[1] - w_i.radius
            xi_dot = w_i.velocity[1]
            force_gr = 0
            if  xi < 0: 
                force_gr = - xi * 10000 - self.gr_dissip_const * xi_dot
                if w_i.radius == 0:
                    self.ground_hit = True
            force_vec = np.array([0.,0.],float)
            force_vec[1] = force_gr
            w_i.add_force ( force_vec )
           

            
    def update_positions (self):
        for w in self.wheel_list:
            w.integrate (self.dt)

    
    def add_wheel(self,mass,position,radius=0,torque=0):
        w = wheel.Wheel(mass,position,radius,torque)
        self.wheel_list.append(w)
        
    def make_ground(self):
        for g in self.ground_tuple:
            g_a = np.array([g[0],g[1]],float)
            self.ground_array.append (g_a)
        gr = self.ground_array
        for i in range(len(gr) - 1):
            d_p = gr[i+1] - gr[i]
            norm_d_p = np.linalg.norm (d_p)
            d_p = d_p / norm_d_p
            self.ground_parallel.append (d_p)
            d_n = np.array([-d_p[1],d_p[0]],float)
            if d_n[1] < 0:
                d_n *= -1.0         #makes the normal upward
            self.ground_normal.append (d_n)


    
    def set_spring_const(self,sp):
        self.spring_const = sp
    
    def set_young_const(self,sp):
        self.young_const = sp
    
    def set_dissip_const(self,sp):
        self.dissip_const = sp

    def set_gr_dissip_const(self,sp):
        self.gr_dissip_const = sp       

    def print_wheel(self,i):
        print self.wheel_list[i].position
        
