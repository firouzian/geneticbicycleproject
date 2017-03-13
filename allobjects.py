import wheel 
import ground
import particle

class AllObjects(object):
    def __init__(self):
        print "AllObjects"
        self.wheel_list=[]
        self.particle_list=[]
        self.spring_list=[]
        self.dt=0.001
        self.spring_const=1.0
#        w1 = wheel.Wheel()
#        self.wheel_list.append(w1)
        
    def update(self):
        self.calculate_forces()
        self.update_positions()
        return None
    
    def calculate_forces(self):
        return None
    
    def update_positions(self):
        for w in self.wheel_list:
            w.integrate(self.dt)
        return None
    
    def add_wheel(self,mass,position,radius):
        w = wheel.Wheel(mass,position,radius)
        wheel_list.append(w)
    def add_particle(self,mass,position):
        p = particle.Particle(mass,position)
        particle_list.append(p)
        
    def make_ground(self):
        return None
    
    def add_spring(self,sp):
        self.spring_const = sp
        
    