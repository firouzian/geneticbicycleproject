# -*- coding: utf-8 -*-
"""
Created on Sun Mar 12 00:38:56 2017

@author: user-guest
"""
#lalalala

class User_Parameters(object):
    """Parameters set by the User in relation to the physics of the bicycles"""
    def __init__(self,x_min,y_min,x_max,y_max,SC_max):
        self.x_min = x_min
        self.y_min = y_min  
        self.x_max = x_max
        self.y_max = y_max
        self.SC_max = SC_max