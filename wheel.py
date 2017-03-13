#!/usr/bin/env python

class Wheel():
	def __init__ (self, m=1.0,position=[1.0,1.0],radius=1.0,velocity=[0.0,0.0]):
		print 'wheel is created'
		self.mass = m
		self.position = position
		self.radius = radius
		self.velocity = velocity
		self.acceleration = [0.,0.]
		self.force = [0.,0.]
	def __str__ (self):
		print self.mass,self.position,self.radius,self.velocity
		return 'hahaha'

if __name__=='__main__':
	w1 = Wheel(5.,[2,3],2.0,[0.3,0.4])
	print w1.mass
	print w1.position
	w1.position=[3.,4.]
 	print w1.position       
	print w1.position[0]
	w1.position[0]=7.5
        print w1	

