#!/usr/bin/env python

import numpy as np 

# in this class defined wheel property:mass,position,radius,velocity
# and the particle considered as wheel with zero radius

class Wheel():
	def __init__ (self, m=1.0,position=[1.0,1.0],radius=1.0,velocity=[0.0,0.0]):
		print 'wheel is created'
		self.mass = m
		self.position =np.array(position,float)
		self.radius = radius
		self.velocity = np.array(velocity,float)
		self.acceleration = np.array([0.,0.],float)
		self.force = np.array([0.,0.],float)
	def __str__ (self):
		print self.mass,self.position,self.radius,self.velocity
		return 'hahaha'
        def integrate(self,dt):
            self.velocity = self.velocity + self.acceleration*dt
            self.position = self.position + self.velocity*dt + (self.acceleration*dt*dt)*0.5
            

if __name__=='__main__':
	w1 = Wheel(5.,[2,3],2.0,[0.3,0.4])
	print w1.mass
	print w1.position
	w1.position=[3.,4.]
 	print w1.position       
	print w1.position[0]
	w1.position[0]=7.5
        print w1	

